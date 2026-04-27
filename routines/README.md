# Cloud Routines

Each `*.md` here is the verbatim prompt for one Claude Code cloud routine.
Paste the full contents into the routine's prompt field — do not paraphrase.
The env-var check block and commit-and-push step are load-bearing.

## Cron schedules (America/Chicago)

| Routine        | Cron            | When                                      |
|----------------|-----------------|-------------------------------------------|
| pre-market     | `0 6 * * 1-5`   | 06:00 weekdays                            |
| market-open    | `30 8 * * 1-5`  | 08:30 weekdays (market opens 08:30 CT)    |
| midday         | `0 12 * * 1-5`  | 12:00 weekdays (noon)                     |
| daily-summary  | `0 15 * * 1-5`  | 15:00 weekdays (market closes 15:00 CT)   |
| weekly-review  | `0 16 * * 5`    | 16:00 Fridays only                        |

## Per-routine env vars

All five routines need:

- `ALPACA_API_KEY`, `ALPACA_SECRET_KEY` (required)
- `ALPACA_ENDPOINT`, `ALPACA_DATA_ENDPOINT` (optional, default to live URLs)
- `PERPLEXITY_API_KEY` (required for pre-market and weekly-review;
  midday's optional intraday research falls back to WebSearch if missing)
- `PERPLEXITY_MODEL` (optional, defaults to `sonar`)
- `DISCORD_WEBHOOK_URL` (required for channel notifications;
  discord.py falls back to a local file if missing)

Set these as **routine environment variables** in the Claude Code cloud UI.
**Do NOT create a `.env` file in the cloud** — every prompt explicitly forbids
this because a runtime-created `.env` is either a secret leak (if pushed) or
wasted work (if not).

## Mandatory toggle

Enable **"Allow unrestricted branch pushes"** in each routine's environment
settings. Without this, `git push origin main` silently fails with a proxy
error. This is the number-one reason first-time setups break.

## What each run does

Each firing is an ephemeral container — clone, run, destroy. The container
reads memory from the latest `main`, calls the Python wrappers, writes new
memory, commits, pushes. If it doesn't push, the work evaporates.

The mental model: **the cloud runner is stateless. Git is the memory.**
If it's not in `main`, it didn't happen.

## Python runtime

The wrappers are stdlib-only — `urllib`, `json`, `os`, `pathlib`. No
`pip install` step is needed. Any container with Python 3 works.
