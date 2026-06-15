---
name: world-cup-predictor
description: Predict FIFA World Cup matches, full tournament paths, and champion probabilities through Codex-native subagents that analyze live news, weather, injuries, markets, Polymarket, tactics, and tournament context while updating a real-time web dashboard. Use when asked to forecast World Cup games, predict the full World Cup outlook, compare match forecasts, or show prediction progress live in a browser.
---

# World Cup Predictor

## Overview

Use this skill to run an agent-native World Cup prediction room. The invoking Codex agent starts the web dashboard first, collects current signals, spawns subagents for independent analysis, and publishes each prediction update to the page as subagent results arrive.

Do not substitute deterministic, static, or hardcoded forecasts. The model reasoning must come from the current Codex agent and its subagents.

## Default Action

For broad requests such as "predict this World Cup", "predict the tournament path", "who will win", or "预测这一届世界杯走向":

1. Start the dashboard server first.
   - Run `python3 scripts/start_dashboard.py --port 8789` from the skill root in a long-running foreground tool session.
   - The helper chooses the next free port if 8789 is occupied. Report the printed URL.
   - Do not rely on shell backgrounding with `&`; some Codex shells clean up detached processes before the browser can connect.
2. Initialize the page state.
   - Run `scripts/bootstrap_worldcup.py --out assets/dashboard/data`.
   - Run `scripts/set_live_state.py --stage kickoff --message "Starting subagent World Cup prediction room" --progress 0.03`.
3. Lock finished results.
   - Verify official or reputable live score sources for already-finished matches.
   - Write them to `assets/dashboard/data/locked-results.json` with `scripts/sync_locked_results.py`.
   - Do not ask subagents to predict locked matches.
4. Collect current signals.
   - Run `scripts/collect_signals.py --out assets/dashboard/data/signals.json`.
   - If `signals.json` contains Polymarket rows with `status: "fallback-required"` or odds with `status: "missing ODDS_API_KEY"`, preserve those rows and have the market subagent manually inspect the listed public pages. Do not treat empty market data as zero probability.
   - Run `scripts/set_live_state.py --stage signal-collection --message "Collected news, markets, weather, and optional odds" --progress 0.10`.
5. Read `references/agent-native-workflow.md`, `references/research-protocol.md`, and `references/dashboard-data-contract.json`.
6. Spawn subagents using the layered workflow in `references/agent-native-workflow.md`.
   - Keep `markets` and `news-weather` as sidecar signal agents.
   - For the group stage, spawn one subagent per group (`group-a` through `group-l`).
   - For knockouts, spawn one subagent per current-round match and advance round by round until the Final.
   - The Final is predicted by one final-match subagent after semifinal winners are fixed.
7. As subagent results arrive, publish partial dashboard JSON with `scripts/publish_dashboard.py`.
   - If a subagent takes longer than the first wait, continue waiting in longer intervals and publish heartbeat live-state updates so the dashboard stays alive.
   - Do not interrupt slow role agents just to force a compact result. Only synthesize a missing role after an explicit failure, unavailable subagent tooling, or a user request to stop waiting.
8. Final output must include settled results plus forecasts for the remaining complete tournament path.
9. Publish final data with `scripts/publish_dashboard.py --complete`.
10. Run the local regression checks, then verify the dashboard and replay controls in the Browser plugin.

## Regression Checks

After publishing final dashboard data, run the local regression suite:

```bash
python3 -m unittest discover -s tests -v
```

If invoking from the repository root instead of the skill root, use:

```bash
python3 -m unittest discover -s world-cup-predictor/tests -v
```

These tests use Python's standard `unittest` framework. Do not require `pytest` unless a future dependency file explicitly adds it. Treat missing `pytest` as an environment/tooling issue, not a failed regression.

## Prediction Contract

- The web page is the live display surface. Keep it changing while work proceeds by updating `assets/dashboard/data/live-state.json` and `assets/dashboard/data/predictions.json`.
- Published prediction and live-state updates append snapshots to `assets/dashboard/data/replay.json`; preserve it through the run so the completed dashboard can replay the forecast room.
- Subagent reasoning is the prediction engine. Do not substitute deterministic ratings or hardcoded forecasts.
- Finished matches are settled results, not forecasts. Lock them before prediction and exclude them from subagent prediction scopes.
- Every match packet must include probabilities, predicted score, event timeline, momentum, evidence, risks, and environmental factors.
- The final dashboard JSON must match `references/dashboard-data-contract.json`.
- If subagent tools are unavailable, perform the same analysis in the main agent and state that parallelization was unavailable.

## Evidence Rules

- Date every source. The World Cup is live and information changes quickly.
- Separate observed results from forecasts. Already-played matches must be locked as facts.
- Flag missing or stale data instead of filling it with guesses.
- If a live data connector fails, use the explicit fallback URLs in `signals.json` and state the connector failure in the dashboard narrative.
- For Polymarket and odds, capture market title, URL, timestamp, liquidity/volume when visible, price, and normalized implied probability.
- For tactical claims, cite concrete matchups: press resistance, buildup shape, transition defense, set pieces, wide overloads, goalkeeper distribution, squad rotation, altitude/travel/rest, and suspension risk.
- For simulation claims, cite the factor behind each event when possible: heat fatigue, humidity-driven tempo drop, injury limitation, set-piece mismatch, bench depth, goalkeeper profile, or tactical change.

## Resources

- `references/agent-native-workflow.md`: default no-key workflow for Codex agents that spawn subagents.
- `references/research-protocol.md`: source checklist, probability calibration, and confidence rubric.
- `references/subagents.md`: role prompts and handoff contracts for subagents.
- `references/prediction-schema.json`: JSON contract for match-level agent outputs.
- `references/dashboard-data-contract.json`: JSON contract for dashboard-level tournament predictions.
- `references/worldcup-2026-groups.json`: bootstrap group snapshot.
- `scripts/bootstrap_worldcup.py`: create dashboard data scaffolding.
- `scripts/start_dashboard.py`: start the static dashboard on 8789 or the next free port.
- `scripts/collect_signals.py`: collect current news RSS, Polymarket, weather, and optional odds signals.
- `scripts/set_live_state.py`: update the dashboard broadcast strip.
- `scripts/replay_history.py`: append dashboard snapshots for post-run replay.
- `scripts/sync_locked_results.py`: maintain already-finished match results that should not be predicted.
- `scripts/publish_dashboard.py`: publish partial or final subagent-derived dashboard predictions.
- `scripts/merge_predictions.py`: merge role-specific match packets when subagents produce overlapping outputs.
- `scripts/validate_skill.sh`: create a local virtualenv, install validation dependencies, and run the official skill validator.
- `assets/dashboard/`: static live dashboard.
