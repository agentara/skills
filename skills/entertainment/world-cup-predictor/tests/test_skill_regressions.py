import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class WorldCupSkillRegressionTests(unittest.TestCase):
    def test_seed_groups_use_current_draw_teams(self):
        groups = json.loads((ROOT / "references" / "worldcup-2026-groups.json").read_text(encoding="utf-8"))["groups"]
        by_group = {group["group"]: group["teams"] for group in groups}

        self.assertEqual(by_group["F"], ["Netherlands", "Japan", "Sweden", "Tunisia"])
        self.assertEqual(by_group["K"], ["Portugal", "DR Congo", "Uzbekistan", "Colombia"])
        self.assertNotIn("Play-off winner A", [team for teams in by_group.values() for team in teams])
        self.assertNotIn("Mali", [team for teams in by_group.values() for team in teams])

    def test_dashboard_flags_include_current_draw_teams(self):
        app_js = (ROOT / "assets" / "dashboard" / "app.js").read_text(encoding="utf-8")

        self.assertIn('"DR Congo": "🇨🇩"', app_js)
        self.assertIn('Sweden: "🇸🇪"', app_js)
        self.assertIn(r'England: "\u{1F3F4}\u{E0067}\u{E0062}\u{E0065}\u{E006E}\u{E0067}\u{E007F}"', app_js)
        self.assertIn(r'Scotland: "\u{1F3F4}\u{E0067}\u{E0062}\u{E0073}\u{E0063}\u{E0074}\u{E007F}"', app_js)
        self.assertNotIn('England: "🏴"', app_js)
        self.assertNotIn('Scotland: "🏴"', app_js)

    def test_final_live_state_refresh_preserves_complete_and_featured(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            state_path = Path(tmpdir) / "live-state.json"
            state_path.write_text(json.dumps({
                "updated_at": "2026-06-15T00:00:00+00:00",
                "stage": "final-synthesis",
                "message": "old",
                "progress": 1,
                "featured": {"matches": 104, "champion": "Spain"},
                "complete": True,
                "error": False
            }), encoding="utf-8")

            subprocess.run([
                sys.executable,
                str(ROOT / "scripts" / "set_live_state.py"),
                "--out", str(state_path),
                "--stage", "final-synthesis",
                "--message", "refreshing final copy",
                "--progress", "1"
            ], check=True, capture_output=True, text=True)

            refreshed = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertTrue(refreshed["complete"])
            self.assertEqual(refreshed["featured"], {"matches": 104, "champion": "Spain"})

    def test_publish_dashboard_appends_replay_frame(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out = Path(tmpdir)
            predictions_path = out / "partial.json"
            predictions_path.write_text(json.dumps({
                "updated_at": "2026-06-15T00:00:00+00:00",
                "mode": "agent-native-subagents",
                "predicted_champion": "Spain",
                "matches": [{
                    "match_id": "M104",
                    "round": "Final",
                    "teams": ["Spain", "England"],
                    "probabilities": {"Spain": 0.57, "England": 0.43},
                    "simulation": {"predicted_score": {"home": 2, "away": 1}, "timeline": []}
                }],
                "groups": [],
                "outrights": [{"team": "Spain", "probability": 0.18}],
                "narrative": ["Spain win the modal path."]
            }), encoding="utf-8")
            (out / "locked-results.json").write_text(json.dumps({"results": []}), encoding="utf-8")

            subprocess.run([
                sys.executable,
                str(ROOT / "scripts" / "publish_dashboard.py"),
                "--predictions", str(predictions_path),
                "--out", str(out),
                "--locked-results", str(out / "locked-results.json"),
                "--stage", "complete",
                "--message", "Final forecast published",
                "--progress", "1",
                "--complete"
            ], check=True, capture_output=True, text=True)

            replay = json.loads((out / "replay.json").read_text(encoding="utf-8"))
            self.assertEqual(replay["version"], 1)
            self.assertEqual(len(replay["frames"]), 1)
            frame = replay["frames"][0]
            self.assertEqual(frame["live"]["stage"], "complete")
            self.assertTrue(frame["live"]["complete"])
            self.assertEqual(frame["summary"], {"matches": 1, "champion": "Spain", "progress": 1})
            self.assertEqual(frame["predictions"]["matches"][0]["match_id"], "M104")

    def test_live_state_update_appends_replay_heartbeat(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out = Path(tmpdir)
            (out / "predictions.json").write_text(json.dumps({
                "updated_at": "2026-06-15T00:00:00+00:00",
                "matches": [{"match_id": "GS-A-1"}],
                "outrights": []
            }), encoding="utf-8")
            (out / "source-log.json").write_text(json.dumps({"generated_at": "seed", "sources": []}), encoding="utf-8")

            subprocess.run([
                sys.executable,
                str(ROOT / "scripts" / "set_live_state.py"),
                "--out", str(out / "live-state.json"),
                "--stage", "signal-collection",
                "--message", "Collected signals",
                "--progress", "0.1"
            ], check=True, capture_output=True, text=True)

            replay = json.loads((out / "replay.json").read_text(encoding="utf-8"))
            self.assertEqual(len(replay["frames"]), 1)
            frame = replay["frames"][0]
            self.assertEqual(frame["live"]["stage"], "signal-collection")
            self.assertEqual(frame["summary"], {"matches": 1, "champion": None, "progress": 0.1})
            self.assertEqual(frame["predictions"]["matches"][0]["match_id"], "GS-A-1")

    def test_polymarket_empty_response_returns_actionable_fallbacks(self):
        collect_signals = load_module(ROOT / "scripts" / "collect_signals.py")
        original_fetch_json = collect_signals.fetch_json
        try:
            collect_signals.fetch_json = lambda url: []
            rows = collect_signals.polymarket_markets("2026 FIFA World Cup winner odds")
        finally:
            collect_signals.fetch_json = original_fetch_json

        self.assertGreaterEqual(len(rows), 3)
        self.assertTrue(any(row.get("status") == "fallback-required" for row in rows))
        self.assertTrue(any("polymarket.com" in row.get("url", "") for row in rows))

    def test_dashboard_start_helper_selects_next_free_port(self):
        import socket

        start_dashboard = load_module(ROOT / "scripts" / "start_dashboard.py")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(("127.0.0.1", 0))
            server.listen()
            occupied_port = server.getsockname()[1]

            selected = start_dashboard.find_available_port(occupied_port)

        self.assertGreater(selected, occupied_port)
        self.assertTrue(start_dashboard.port_is_available(selected))

    def test_workflow_waits_for_slow_subagents_instead_of_interrupting(self):
        skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        workflow_text = (ROOT / "references" / "agent-native-workflow.md").read_text(encoding="utf-8")
        research_text = (ROOT / "references" / "research-protocol.md").read_text(encoding="utf-8")
        combined = "\n".join([skill_text, workflow_text, research_text])

        self.assertNotIn("interrupt once", combined)
        self.assertNotIn("interrupt it once", combined)
        self.assertIn("continue waiting", combined)
        self.assertIn("heartbeat", combined)
        self.assertIn("Only synthesize a missing role after an explicit failure", combined)

    def test_workflow_requires_replay_verification(self):
        skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("replay.json", skill_text)
        self.assertIn("replay controls", skill_text)
        self.assertIn("scripts/replay_history.py", skill_text)

    def test_workflow_uses_group_and_match_level_subagents(self):
        workflow_text = (ROOT / "references" / "agent-native-workflow.md").read_text(encoding="utf-8")
        subagents_text = (ROOT / "references" / "subagents.md").read_text(encoding="utf-8")
        combined = "\n".join([workflow_text, subagents_text])

        self.assertIn("one subagent per group", combined)
        self.assertIn("group-a", combined)
        self.assertIn("group-l", combined)
        self.assertIn("one subagent per knockout match", combined)
        self.assertIn("Round of 32", combined)
        self.assertIn("Round of 16", combined)
        self.assertIn("Quarterfinal", combined)
        self.assertIn("Semifinal", combined)
        self.assertIn("Third-place Match", combined)
        self.assertIn("Final", combined)
        self.assertIn("final-match subagent", combined)
        self.assertIn("Do not spawn later-round match subagents before prior-round winners are fixed", combined)
        self.assertNotIn("tactics-a-f", combined)
        self.assertNotIn("tactics-g-l", combined)
        self.assertNotIn("produce all 32 knockout matches", combined)


if __name__ == "__main__":
    unittest.main()
