# Research Protocol

## Required Inputs

For each match, gather and timestamp:

- Tournament state: group table, locked results, fixture date, venue, rest days, travel path.
- Team strength: Elo/SPI-like rating, FIFA ranking as a weak prior, recent competitive form, expected lineup quality.
- Availability: injuries, suspensions, card risk, rotation hints, manager comments.
- Tactical matchup: formations, pressing intensity, buildup routes, transition defense, set-piece edge, goalkeeper and penalty profiles.
- Market data: bookmaker 1X2, Asian handicap/total if useful, exchange odds, Polymarket match/group/champion markets where liquid.
- Environment: venue, kickoff time, temperature, humidity, heat index, rain/wind, altitude, surface, expected roof status, rest days, and travel load.
- Context: crowd/home effects, motivation, qualification incentives, rotation incentives.

## Match-Flow Simulation

Every agent must return a simulated match process, not only a final probability. Make it feel like a FIFA game simulation while keeping it source-grounded:

- predicted scoreline and halftime score;
- goal events with minute window, scorer profile if known, assist/source pattern, and probability;
- key events such as cards, VAR, injuries, fatigue drops, substitutions, set-piece chances, goalkeeper saves, tactical switches, and late pressure;
- momentum by phase: 0-15, 16-30, 31-45+, 46-60, 61-75, 76-90+;
- environmental effects, especially hot or humid U.S./Mexico summer venues, altitude, long travel, and short rest;
- injury/fitness effects, including players likely to start but fade early.

Do not invent named scorers when lineup information is weak. Use role labels such as `primary striker`, `left winger`, or `set-piece center back` and flag the uncertainty.

## Probability Handling

1. Convert decimal odds with `1 / odds`.
2. Remove bookmaker overround by dividing each implied probability by the market total.
3. Compare sources at the same event level. Do not mix 90-minute 1X2 with advancement odds.
4. Use market consensus as the base rate when data is current and liquid.
5. Adjust only for explicit evidence. Record the adjustment reason and magnitude.

## Data Failure Handling

- Treat connector failures, empty API responses, missing API keys, and low/zero-volume markets as stale-data warnings.
- If `signals.json` contains `fallback-required` market rows, manually inspect those URLs and capture the same fields required for normal market data.
- Never convert missing odds, missing lineups, or a slow subagent into a confident probability. Lower confidence and state the gap.
- Continue waiting for slow role subagents while publishing heartbeat status. Only synthesize a missing role after an explicit failure, unavailable subagent tooling, or a user request to stop waiting.

## Confidence Rubric

- `high`: multiple fresh sources agree, market is liquid, lineups/news are stable.
- `medium`: good source coverage but one important uncertainty remains.
- `low`: stale odds, missing team news, low liquidity, or major tactical disagreement.

## Output Expectations

Every prediction must include:

- probabilities that sum to 1 for the stated market;
- a match-flow simulation with predicted score, event timeline, and environmental factors;
- top evidence bullets with source URLs;
- one contrarian risk;
- confidence and stale-data warnings;
- timestamp in ISO 8601 format.
