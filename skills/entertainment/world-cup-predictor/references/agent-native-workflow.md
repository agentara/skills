# Agent-Native Workflow

Use this workflow whenever Codex runs `$world-cup-predictor`. It needs no user API key: the current agent and its subagents provide the model reasoning.

## Live Sequence

1. Start the dashboard server before prediction begins.
   - Run `python3 scripts/start_dashboard.py --port 8789` from the skill root in a long-running foreground session.
   - Use the printed URL; if 8789 is occupied, the helper selects the next free port.
   - Avoid shell backgrounding (`&`) because detached servers can be cleaned up in Codex sessions.
2. Bootstrap dashboard data and set `live-state.json` to `kickoff`.
3. Lock already-finished matches.
   - Verify current results from official FIFA pages or reputable live score sources.
   - Write settled matches to `assets/dashboard/data/locked-results.json`.
   - Use `scripts/sync_locked_results.py --add "match_id|round|group|home|away|home_score|away_score|source"` for individual results, or `--from-json` for a batch.
   - Exclude locked matches from prediction prompts.
4. Collect signals into `assets/dashboard/data/signals.json`.
   - If Polymarket rows contain `status: "fallback-required"` or odds contain `status: "missing ODDS_API_KEY"`, give those rows to the market subagent as explicit manual-check targets.
   - Empty market connector output is a stale-data warning, not evidence that no market exists.
5. Spawn sidecar signal subagents:
   - `markets`: Polymarket, bookmaker odds if available, market-implied contenders, and market uncertainty.
   - `news-weather`: injuries, suspensions, manager comments, travel, rest, heat, humidity, rain, altitude, and venue context.
6. Spawn group-stage prediction subagents: one subagent per group.
   - Dispatch `group-a`, `group-b`, `group-c`, `group-d`, `group-e`, `group-f`, `group-g`, `group-h`, `group-i`, `group-j`, `group-k`, and `group-l` in parallel.
   - Each group subagent owns its four-team group, all non-locked group matches in that group, the group table, advancement probabilities, tactical simulation, risks, and evidence.
   - Locked matches are facts passed into the relevant group subagent; they are not re-predicted.
7. After group subagents return, publish group-stage predictions and compute the Round of 32 bracket.
8. Run knockout prediction as a recursive round loop: one subagent per knockout match.
   - Spawn one subagent per knockout match in the current round only: Round of 32, then Round of 16, then Quarterfinal, then Semifinal, then Third-place Match, then Final.
   - Do not spawn later-round match subagents before prior-round winners are fixed by returned prediction packets.
   - Each knockout-match subagent receives the two qualified teams, path context, rest/travel, venue, sidecar market/news/weather signals, prior match packets, and must return one `prediction-schema.json` packet.
   - The Final must be predicted by exactly one final-match subagent, not folded into a broad tournament synthesis.
9. Update the dashboard while waiting:
   - use `scripts/set_live_state.py` for stage/progress messages;
   - publish partial JSON with `scripts/publish_dashboard.py` whenever a usable set of match packets is available.
   - If a subagent takes longer than the first wait, continue waiting in longer intervals and publish heartbeat messages such as `"Still waiting on group-h deep dive"` or `"Still waiting on Round of 16 match agent"` without changing completed predictions.
   - Do not interrupt slow subagents just to make them return compact JSON. Only synthesize a missing role after an explicit failure, unavailable subagent tooling, or a user request to stop waiting, and record that fallback in `narrative` or `stale_data_warnings`.
10. Publish the final dashboard JSON to `assets/dashboard/data/predictions.json` with `scripts/publish_dashboard.py --complete`.
11. Verify the page in the Browser plugin.

## Output Requirements

The final dashboard must contain:

- `matches`: 104 total matches:
  - 72 group-stage matches;
  - 16 Round of 32 matches;
  - 8 Round of 16 matches;
  - 4 quarterfinals;
  - 2 semifinals;
  - 1 third-place match;
  - 1 final.
- `groups`: predicted table/progression for all 12 groups.
- `outrights`: champion probabilities that sum approximately to 1 across listed contenders.
- `predicted_champion`: the top team from `outrights`.
- `narrative`: concise explanation of decisive factors.

Already-finished matches must appear with `status: "finished"`, `final_score`, and `result_source`; they should not contain active market odds. Remaining matches should use `status: "scheduled"` or `status: "live"`.

## Subagent Prompt Pattern

Give each subagent:

- the role and exact output scope;
- the relevant groups or market/news task;
- `references/research-protocol.md`;
- `references/prediction-schema.json`;
- current `assets/dashboard/data/signals.json`;
- instruction to output JSON only.

For group agents, request one group only: all six matches in that four-team group, excluding locked matches as forecasts. For knockout agents, request one match only. Do not ask any single subagent to predict an entire knockout round or bracket.

Use the corrected live draw snapshot in `references/worldcup-2026-groups.json`; do not reintroduce placeholder teams such as `Play-off winner A` or stale teams such as `Mali` unless a new official source proves the draw changed again.

## Publishing Pattern

After each useful subagent result, the main agent should assemble a partial dashboard file and run:

```bash
scripts/publish_dashboard.py \
  --predictions /path/to/partial-or-final-dashboard.json \
  --out assets/dashboard/data \
  --stage subagent-update \
  --message "Published latest subagent predictions" \
  --progress 0.45
```

For the final update, pass `--complete` and use a message naming the predicted champion.

After final publication, prefer `scripts/publish_dashboard.py --complete` for any narrative refresh. `scripts/set_live_state.py` preserves already-complete final state at progress 1, but publishing the full prediction file keeps `featured` metadata synchronized.
