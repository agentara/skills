import json
from datetime import datetime, timezone
from pathlib import Path


REPLAY_LIMIT = 240


def read_json(path, fallback):
    path = Path(path)
    if not path.exists():
        return fallback
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return fallback


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
    tmp.replace(path)


def summarize_frame(predictions, live_state):
    return {
        "matches": len(predictions.get("matches", [])),
        "champion": predictions.get("predicted_champion"),
        "progress": live_state.get("progress", 0)
    }


def build_replay_frame(predictions, live_state, sources):
    captured_at = live_state.get("updated_at") or predictions.get("updated_at") or datetime.now(timezone.utc).isoformat()
    stage = live_state.get("stage") or "dashboard-update"
    return {
        "id": f"{captured_at}:{stage}",
        "captured_at": captured_at,
        "label": live_state.get("message") or stage,
        "summary": summarize_frame(predictions, live_state),
        "live": live_state,
        "predictions": predictions,
        "sources": sources
    }


def append_replay_frame(data_dir, predictions=None, live_state=None, sources=None):
    data_dir = Path(data_dir)
    predictions = predictions if predictions is not None else read_json(data_dir / "predictions.json", {"matches": [], "outrights": []})
    live_state = live_state if live_state is not None else read_json(data_dir / "live-state.json", {"stage": "Board Closed", "message": "", "progress": 0})
    sources = sources if sources is not None else read_json(data_dir / "source-log.json", {"sources": []})

    replay_path = data_dir / "replay.json"
    replay = read_json(replay_path, {"version": 1, "generated_at": datetime.now(timezone.utc).isoformat(), "frames": []})
    frames = [frame for frame in replay.get("frames", []) if isinstance(frame, dict)]
    frame = build_replay_frame(predictions, live_state, sources)

    if frames and frames[-1].get("id") == frame["id"]:
        frames[-1] = frame
    else:
        frames.append(frame)

    replay["version"] = 1
    replay["generated_at"] = datetime.now(timezone.utc).isoformat()
    replay["frames"] = frames[-REPLAY_LIMIT:]
    write_json(replay_path, replay)
    return frame
