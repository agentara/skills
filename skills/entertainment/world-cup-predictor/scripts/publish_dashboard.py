#!/usr/bin/env python3
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from replay_history import append_replay_frame


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
    tmp.replace(path)


def normalize_predictions(data):
    data.setdefault("mode", "agent-native-subagents")
    data.setdefault("updated_at", datetime.now(timezone.utc).isoformat())
    data.setdefault("simulation", {"method": "codex-subagent-synthesis"})
    data.setdefault("predicted_champion", None)
    data.setdefault("matches", [])
    data.setdefault("groups", [])
    data.setdefault("outrights", [])
    data.setdefault("narrative", [])
    return data


def load_locked_results(path):
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("results", data if isinstance(data, list) else [])


def locked_key(result):
    if result.get("match_id"):
        return f"id:{result['match_id']}"
    return "teams:" + "|".join(sorted(result.get("teams", [])))


def settle_match(match, result):
    settled = dict(match)
    settled["status"] = "finished"
    settled["market_type"] = "settled"
    settled["final_score"] = result.get("final_score")
    settled["result_source"] = result.get("source")
    settled["locked_at"] = result.get("locked_at")
    settled["round"] = result.get("round", settled.get("round"))
    settled["group"] = result.get("group", settled.get("group"))
    settled["teams"] = result.get("teams", settled.get("teams", []))
    return settled


def apply_locked_results(predictions, locked_results):
    by_id = {locked_key(result): result for result in locked_results}
    settled_ids = set()
    matches = []
    for match in predictions.get("matches", []):
        keys = [f"id:{match.get('match_id')}", "teams:" + "|".join(sorted(match.get("teams", [])))]
        result = next((by_id[key] for key in keys if key in by_id), None)
        if result:
            matches.append(settle_match(match, result))
            settled_ids.add(locked_key(result))
        else:
            match.setdefault("status", "scheduled")
            matches.append(match)
    for result in locked_results:
        key = locked_key(result)
        if key not in settled_ids:
            matches.append(settle_match({
                "match_id": result.get("match_id"),
                "agent_role": "merged",
                "generated_at": result.get("locked_at"),
                "market_type": "settled",
                "teams": result.get("teams", []),
                "probabilities": {},
                "confidence": "high",
                "simulation": {"predicted_score": result.get("final_score", {}), "halftime_score": {"home": 0, "away": 0}, "timeline": [], "momentum": []},
                "evidence": [{"claim": "Finished match result locked; no prediction required.", "source": result.get("source", ""), "timestamp": result.get("locked_at", "")}],
                "risks": []
            }, result))
    predictions["matches"] = matches
    predictions["locked_results_count"] = len(locked_results)
    return predictions


def main():
    parser = argparse.ArgumentParser(description="Publish agent-native prediction data to the live dashboard.")
    parser.add_argument("--predictions", required=True, help="Path to dashboard prediction JSON produced by the main agent")
    parser.add_argument("--out", default=str(ROOT / "assets" / "dashboard" / "data"))
    parser.add_argument("--locked-results", default=str(ROOT / "assets" / "dashboard" / "data" / "locked-results.json"))
    parser.add_argument("--stage", default="agent-native-update")
    parser.add_argument("--message", default="Published subagent prediction update")
    parser.add_argument("--progress", type=float, default=0.5)
    parser.add_argument("--complete", action="store_true")
    args = parser.parse_args()

    out = Path(args.out)
    predictions = normalize_predictions(json.loads(Path(args.predictions).read_text(encoding="utf-8")))
    predictions = apply_locked_results(predictions, load_locked_results(Path(args.locked_results)))
    predictions["updated_at"] = datetime.now(timezone.utc).isoformat()
    write_json(out / "predictions.json", predictions)
    live_state = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "stage": args.stage,
        "message": args.message,
        "progress": max(0, min(1, args.progress)),
        "featured": {
            "matches": len(predictions.get("matches", [])),
            "champion": predictions.get("predicted_champion")
        },
        "complete": args.complete,
        "error": False
    }
    write_json(out / "live-state.json", live_state)
    append_replay_frame(out, predictions=predictions, live_state=live_state)
    print(f"Published {len(predictions.get('matches', []))} matches to {out}")


if __name__ == "__main__":
    main()
