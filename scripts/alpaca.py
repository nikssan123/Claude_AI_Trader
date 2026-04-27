#!/usr/bin/env python3
"""Alpaca API wrapper. All trading API calls go through here.

Usage: python scripts/alpaca.py <subcommand> [args...]

Subcommands:
  account                       equity, cash, buying_power, daytrade_count
  positions                     all open positions w/ unrealized P&L
  position SYM                  single position
  quote SYM                     latest bid/ask (uses data.alpaca.markets)
  orders [status]               default status=open
  order '<json>'                POST new order
  cancel ORDER_ID
  cancel-all
  close SYM                     market-sell entire position
  close-all
"""
import json
import os
import sys
import urllib.error
import urllib.parse
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


def require(name):
    val = os.environ.get(name)
    if not val:
        print(f"{name} not set in environment", file=sys.stderr)
        sys.exit(1)
    return val


def call(method, url, headers, body=None):
    data = body.encode("utf-8") if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        msg = e.read().decode("utf-8", errors="replace")
        print(f"alpaca HTTP {e.code}: {msg}", file=sys.stderr)
        sys.exit(1)


USAGE = (
    "Usage: python scripts/alpaca.py "
    "<account|positions|position|quote|orders|order|cancel|cancel-all|close|close-all> [args]"
)


def main():
    load_env()
    api_key = require("ALPACA_API_KEY")
    secret = require("ALPACA_SECRET_KEY")
    api = os.environ.get("ALPACA_ENDPOINT", "https://paper-api.alpaca.markets/v2")
    data = os.environ.get("ALPACA_DATA_ENDPOINT", "https://data.alpaca.markets/v2")

    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret,
    }

    args = sys.argv[1:]
    if not args:
        print(USAGE, file=sys.stderr)
        sys.exit(1)
    cmd, rest = args[0], args[1:]

    def need(arg_name):
        if not rest:
            print(f"usage: {cmd} {arg_name}", file=sys.stderr)
            sys.exit(1)
        return rest[0]

    if cmd == "account":
        out = call("GET", f"{api}/account", headers)
    elif cmd == "positions":
        out = call("GET", f"{api}/positions", headers)
    elif cmd == "position":
        sym = need("SYM")
        out = call("GET", f"{api}/positions/{urllib.parse.quote(sym)}", headers)
    elif cmd == "quote":
        sym = need("SYM")
        out = call("GET", f"{data}/stocks/{urllib.parse.quote(sym)}/quotes/latest", headers)
    elif cmd == "orders":
        status = rest[0] if rest else "open"
        out = call("GET", f"{api}/orders?status={urllib.parse.quote(status)}", headers)
    elif cmd == "order":
        body = need("'<json>'")
        h = {**headers, "Content-Type": "application/json"}
        out = call("POST", f"{api}/orders", h, body=body)
    elif cmd == "cancel":
        oid = need("ORDER_ID")
        out = call("DELETE", f"{api}/orders/{urllib.parse.quote(oid)}", headers)
    elif cmd == "cancel-all":
        out = call("DELETE", f"{api}/orders", headers)
    elif cmd == "close":
        sym = need("SYM")
        out = call("DELETE", f"{api}/positions/{urllib.parse.quote(sym)}", headers)
    elif cmd == "close-all":
        out = call("DELETE", f"{api}/positions", headers)
    else:
        print(USAGE, file=sys.stderr)
        sys.exit(1)

    print(out)


if __name__ == "__main__":
    main()
