#!/usr/bin/env python3
"""Research wrapper. All market research goes through Perplexity.

Usage: python scripts/perplexity.py "<query>"

Exits with code 3 if PERPLEXITY_API_KEY is unset so callers can fall back
to native WebSearch.
"""
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env"


def load_env():
    if not ENV_FILE.exists():
        return
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        os.environ.setdefault(key.strip(), val.strip())


def main():
    load_env()
    args = sys.argv[1:]
    if not args or not args[0].strip():
        print('usage: python scripts/perplexity.py "<query>"', file=sys.stderr)
        sys.exit(1)
    query = args[0]

    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        print("WARNING: PERPLEXITY_API_KEY not set. Fall back to WebSearch.", file=sys.stderr)
        sys.exit(3)

    model = os.environ.get("PERPLEXITY_MODEL", "sonar")
    payload = json.dumps({
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a precise financial research assistant. Cite every claim. Be concise.",
            },
            {"role": "user", "content": query},
        ],
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.perplexity.ai/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            print(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        msg = e.read().decode("utf-8", errors="replace")
        print(f"perplexity HTTP {e.code}: {msg}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
