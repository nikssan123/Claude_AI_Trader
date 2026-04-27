#!/usr/bin/env python3
"""Notification wrapper. Sends a message via a Discord webhook.

Usage:
  python scripts/discord.py "<subject>" "<body>"
  python scripts/discord.py "<subject>" -          # body from stdin

If DISCORD_WEBHOOK_URL is missing, the message is appended to a local
fallback file (NOTIFICATIONS.md) and the script exits 0. The agent
never crashes on missing notifier creds.
"""
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env"
FALLBACK = ROOT / "NOTIFICATIONS.md"

# Discord webhook content cap is 2000 chars. Leave room for the bold
# subject line + newline.
DISCORD_CONTENT_LIMIT = 2000


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
    if len(args) < 1 or not args[0].strip():
        print('usage: python scripts/discord.py "<subject>" "<body>"', file=sys.stderr)
        sys.exit(1)
    subject = args[0]

    if len(args) >= 2 and args[1] != "-":
        body = args[1]
    else:
        body = sys.stdin.read()

    if not body.strip():
        print("usage: body required (positional arg or stdin)", file=sys.stderr)
        sys.exit(1)

    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M %Z").strip()

    if not webhook_url:
        with FALLBACK.open("a", encoding="utf-8") as f:
            f.write(f"\n---\n## {stamp} — {subject} (fallback — Discord not configured)\n{body}\n")
        print("[discord fallback] appended to NOTIFICATIONS.md")
        print(body)
        sys.exit(0)

    content = f"**{subject}**\n{body}"
    if len(content) > DISCORD_CONTENT_LIMIT:
        content = content[: DISCORD_CONTENT_LIMIT - 1] + "…"

    payload = json.dumps({"content": content}).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "ai-trader-v2/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            # Discord returns 204 No Content on success — body is empty.
            data = resp.read().decode("utf-8")
            if data:
                print(data)
    except urllib.error.HTTPError as e:
        msg = e.read().decode("utf-8", errors="replace")
        print(f"discord HTTP {e.code}: {msg}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
