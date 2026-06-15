#!/usr/bin/env python3
import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


WEIGHTS = {
    "markets": 0.35,
    "data-model": 0.25,
    "tactics": 0.18,
    "team-news": 0.12,
    "synthesis": 0.10,
}


def load_packets(path):
    packets = []
    for file in sorted(Path(path).glob("*.json")):
        data = json.loads(file.read_text(encoding="utf-8"))
        if isinstance(data, list):
            packets.extend(data)
        else:
            packets.append(data)
    return packets


def normalize(probs):
    total = sum(float(v) for v in probs.values())
    if total <= 0:
        return probs
    return {k: round(float(v) / total, 4) for k, v in probs.items()}


def score_value(score, side):
    try:
        return int(score.get(side, 0))
    except (AttributeError, TypeError, ValueError):
        return 0


def weighted_score(packets, key):
    home_total = 0.0
    away_total = 0.0
    total_weight = 0.0
    for packet in packets:
        simulation = packet.get("simulation") or {}
        score = simulation.get(key) or {}
        role = packet.get("agent_role", "merged")
        weight = WEIGHTS.get(role, 0.05)
        home_total += score_value(score, "home") * weight
        away_total += score_value(score, "away") * weight
        total_weight += weight
    if not total_weight:
        return {"home": 0, "away": 0}
    return {"home": round(home_total / total_weight), "away": round(away_total / total_weight)}


def merge_simulation(packets):
    timeline = []
    momentum = []
    alternates = []
    for packet in packets:
        role = packet.get("agent_role", "unknown")
        simulation = packet.get("simulation") or {}
        for event in simulation.get("timeline", [])[:8]:
            merged_event = dict(event)
            merged_event["source_role"] = role
            timeline.append(merged_event)
        for phase in simulation.get("momentum", [])[:6]:
            merged_phase = dict(phase)
            merged_phase["source_role"] = role
            momentum.append(merged_phase)
        alternates.extend(simulation.get("alternate_scenarios", [])[:3])

    timeline.sort(key=lambda item: str(item.get("minute", "")))
    return {
        "predicted_score": weighted_score(packets, "predicted_score"),
        "halftime_score": weighted_score(packets, "halftime_score"),
        "timeline": timeline[:14],
        "momentum": momentum[:12],
        "alternate_scenarios": alternates[:6]
    }


def merge_match(match_id, packets):
    outcomes = sorted({k for p in packets for k in p.get("probabilities", {})})
    weighted = defaultdict(float)
    total_weight = 0.0
    evidence = []
    risks = []
    warnings = []
    environmental_factors = []

    for packet in packets:
        role = packet.get("agent_role", "merged")
        weight = WEIGHTS.get(role, 0.05)
        probs = normalize(packet.get("probabilities", {}))
        for outcome in outcomes:
            weighted[outcome] += probs.get(outcome, 0.0) * weight
        total_weight += weight
        evidence.extend(packet.get("evidence", [])[:3])
        risks.extend(packet.get("risks", [])[:2])
        warnings.extend(packet.get("stale_data_warnings", []))
        environmental_factors.extend(packet.get("environmental_factors", [])[:4])

    probabilities = normalize({k: v / total_weight for k, v in weighted.items()}) if total_weight else {}
    confidence = "medium"
    if warnings:
        confidence = "low"
    elif len(packets) >= 4:
        confidence = "high"

    return {
        "match_id": match_id,
        "round": packets[0].get("round"),
        "group": packets[0].get("group"),
        "agent_role": "merged",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "market_type": packets[0].get("market_type", "90m-1x2"),
        "teams": packets[0].get("teams", []),
        "probabilities": probabilities,
        "confidence": confidence,
        "simulation": merge_simulation(packets),
        "environmental_factors": environmental_factors[:8],
        "evidence": evidence[:8],
        "risks": risks[:5],
        "stale_data_warnings": sorted(set(warnings)),
        "source_roles": sorted({p.get("agent_role", "unknown") for p in packets})
    }


def main():
    parser = argparse.ArgumentParser(description="Merge World Cup subagent predictions.")
    parser.add_argument("--input", required=True, help="Directory containing agent JSON files")
    parser.add_argument("--out", required=True, help="Output predictions.json path")
    args = parser.parse_args()

    packets = load_packets(args.input)
    grouped = defaultdict(list)
    for packet in packets:
        grouped[packet["match_id"]].append(packet)

    merged = [merge_match(match_id, items) for match_id, items in sorted(grouped.items())]
    output = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "agent-native-subagents",
        "matches": merged,
        "groups": [],
        "outrights": []
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Merged {len(packets)} packets into {len(merged)} matches at {out}")


if __name__ == "__main__":
    main()
