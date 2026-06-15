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


def load_existing(path):
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def main():
    parser = argparse.ArgumentParser(description="Update dashboard live-state.json for agent-native prediction runs.")
    parser.add_argument("--out", default=str(ROOT / "assets" / "dashboard" / "data" / "live-state.json"))
    parser.add_argument("--stage", required=True)
    parser.add_argument("--message", required=True)
    parser.add_argument("--progress", type=float, default=0)
    parser.add_argument("--complete", action="store_true")
    parser.add_argument("--error", action="store_true")
    args = parser.parse_args()

    out = Path(args.out)
    existing = load_existing(out)
    preserve_final = bool(existing.get("complete")) and args.progress >= 1 and not args.error
    featured = existing.get("featured", {}) if preserve_final else {}

    state = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "stage": args.stage,
        "message": args.message,
        "progress": max(0, min(1, args.progress)),
        "featured": featured,
        "complete": args.complete or preserve_final,
        "error": args.error
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(state, indent=2), encoding="utf-8")
    append_replay_frame(out.parent, live_state=state)
    print(f"Updated live state: {args.stage}")


if __name__ == "__main__":
    main()
