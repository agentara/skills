#!/usr/bin/env python3
import argparse
import functools
import socket
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIRECTORY = ROOT / "assets" / "dashboard"


def port_is_available(port, host="127.0.0.1"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            probe.bind((host, port))
        except OSError:
            return False
    return True


def find_available_port(preferred_port, host="127.0.0.1", attempts=50):
    for port in range(preferred_port, preferred_port + attempts):
        if port_is_available(port, host):
            return port
    raise RuntimeError(f"No available port found from {preferred_port} to {preferred_port + attempts - 1}")


def main():
    parser = argparse.ArgumentParser(description="Start the World Cup dashboard in a long-running foreground server.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8789)
    parser.add_argument("--directory", default=str(DEFAULT_DIRECTORY))
    args = parser.parse_args()

    port = find_available_port(args.port, args.host)
    directory = Path(args.directory).resolve()
    handler = functools.partial(SimpleHTTPRequestHandler, directory=str(directory))
    server = ThreadingHTTPServer((args.host, port), handler)
    print(f"Dashboard serving {directory} at http://{args.host}:{port}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Dashboard server stopped.", flush=True)
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
