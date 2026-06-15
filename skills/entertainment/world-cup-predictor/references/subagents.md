# Subagents

Dispatch focused agents so each prediction has independent evidence before synthesis.

## group-stage

Prompt: Act as one subagent per group: `group-a` through `group-l`. Analyze exactly one four-team group, including locked results, remaining group matches, group table, advancement probabilities, tactical themes, team news, market signals, weather, travel/rest, and qualification incentives. Return JSON with `role`, `group`, `generated_at`, `table`, and `matches`; each match packet must match `prediction-schema.json`. Do not predict matches outside the assigned group.

## knockout-match

Prompt: Act as one subagent per knockout match. Analyze exactly one match in the current bracket round: Round of 32, Round of 16, Quarterfinal, Semifinal, Third-place Match, or Final. Use prior returned match packets, group tables, rest/travel, venue, market/news/weather signals, penalties, goalkeeper profiles, and game-state incentives. Return one `prediction-schema.json` packet with `market_type` set to `advance` for knockout matches. Do not predict any later-round match.

## final-match subagent

Prompt: Act as the final-match subagent. Analyze only the Final after both semifinal winners are fixed. Return one final prediction packet plus a concise champion rationale. The final-match subagent is the only subagent that names the final champion from a played-through bracket path.

## tactics

Prompt: Analyze the tactical matchup for the assigned World Cup match. Focus on formations, pressing, buildup, transitions, set pieces, defensive vulnerabilities, likely substitutions, and game-state sensitivity. Return JSON matching `prediction-schema.json` with `agent_role` set to `tactics`. Include a simulated match process with tactical momentum swings, likely chance types, goal windows, cards, substitutions, and a predicted score.

## markets

Prompt: Collect bookmaker odds, exchange prices, and Polymarket markets relevant to the assigned World Cup match or outright path. Normalize implied probabilities, note overround/liquidity, and identify market movement. Return JSON matching `prediction-schema.json` with `agent_role` set to `markets`. Convert totals, both-teams-to-score, scorer, card, and handicap markets into a conservative simulated scoreline and event likelihoods when those markets are available.

## team-news

Prompt: Gather injuries, suspensions, lineup reports, manager comments, travel/rest issues, and card risks for the assigned World Cup match. Separate confirmed facts from rumors. Return JSON matching `prediction-schema.json` with `agent_role` set to `team-news`. Include how injuries, fatigue, humidity, heat, travel, and suspension risk change the simulated match process.

## data-model

Prompt: Build a statistical prior for the assigned World Cup match from ratings, recent form, goal rates, tournament state, rest, venue, and locked results. Return calibrated probabilities and explain assumptions. Return JSON matching `prediction-schema.json` with `agent_role` set to `data-model`. Include expected goals, predicted score distribution, halftime score, and simulated event rates for goals, cards, substitutions, and late-game pressure.

## synthesis

Prompt: Combine the available role outputs for the assigned World Cup match. Resolve conflicts, keep uncertainty visible, produce final probabilities, final predicted score, halftime score, key event timeline, and alternate scenarios. Return JSON matching `prediction-schema.json` with `agent_role` set to `synthesis`.

## Handoff Rules

- Pass raw source URLs and timestamps, not only summaries.
- Do not let one agent see another agent's conclusion unless it is the `synthesis` agent.
- Ask agents to mark missing data explicitly.
- Keep every agent output as an artifact for dashboard traceability.
- Group-stage work uses one subagent per group. Knockout work uses one subagent per knockout match. Do not spawn later-round match subagents before prior-round winners are fixed.
- Keep simulated events probabilistic. A minute value may be a window such as `31-45+`, not a false exact minute.
- Separate `environmental_factors` from tactical notes so heat, humidity, altitude, rest, travel, and injury effects remain visible on the dashboard.
