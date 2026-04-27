# AI Trader v2

An autonomous, cloud-scheduled stock trading agent built on top of Claude Code.
The agent reads its own memory, pulls live account state, decides on action,
places real orders if warranted, and commits everything back to Git. There is
no separate Python bot process — **Claude is the bot**. Each scheduled run is
a fresh LLM invocation reading a well-defined prompt.

## What this does

Five cron jobs fire each weekday, each one spinning up a fresh Claude Code
cloud container that clones this repo, reads memory, calls Alpaca / Perplexity
/ Discord through the wrapper scripts, writes new memory, commits and pushes,
and posts a notification to Discord.

| Job | Time (CT) | Purpose |
|-----|-----------|---------|
| Pre-market    | 06:00 weekdays | Research catalysts, write today's trade ideas |
| Market-open   | 08:30 weekdays | Execute planned trades, set 10% trailing stops |
| Midday        | 12:00 weekdays | Cut losers (-7%), tighten stops on winners |
| Daily-summary | 15:00 weekdays | EOD snapshot, Discord recap |
| Weekly-review | 16:00 Fridays  | Stats, lessons, letter grade |

## Trading mode

The bot is configured for **PAPER trading by default** — simulated orders
against a real Alpaca paper account. No real money is at risk.

`ALPACA_ENDPOINT` controls which Alpaca account this hits:

- **Paper (default):** `https://paper-api.alpaca.markets/v2`
- **Live:** `https://api.alpaca.markets/v2`

To switch to live later: change `ALPACA_ENDPOINT` to the live URL **and** swap
in your live API keys (paper and live use separate keys).

> **Live trading can lose money.** Only flip to live after the bot has proven
> itself in paper for at least a few weeks and you've audited its commits.
> Past paper performance does not guarantee live results.

## Wrapper scripts

All external API calls go through three Python scripts in `scripts/`. They
are stdlib-only — no `pip install` required, works in any container with
Python 3.

| Script | API | Notes |
|---|---|---|
| `alpaca.py`    | Alpaca v2 | Trading + market data |
| `perplexity.py` | Perplexity | Exits 3 if `PERPLEXITY_API_KEY` missing → caller falls back to WebSearch |
| `discord.py`   | Discord webhook | Channel notifications. Falls back to local `NOTIFICATIONS.md` if `DISCORD_WEBHOOK_URL` missing |

## Setup steps

1. Install the Claude Code CLI and open this directory.
2. Sign up for accounts: Alpaca (paper to start), Perplexity. Pick a
   Discord server + channel where you want notifications.
3. In Discord, create a webhook on the target channel: Channel settings →
   Integrations → Webhooks → New Webhook → Copy Webhook URL. The agent
   posts notifications by `POST`ing to that URL — no bot, no token to manage.
4. Copy `env.template` to `.env` and fill in real credentials.
   `.env` is already gitignored — never commit it.
5. Confirm Python 3 is available (`python --version` should print 3.x).
6. Sanity-check by reading `CLAUDE.md` and `memory/TRADING-STRATEGY.md`.

## Local smoke test with /portfolio

Open this directory in Claude Code and run:

```
/portfolio
```

You should see a clean account snapshot — equity, cash, buying power,
positions, open orders. If that prints without errors, the wrapper scripts
can read your `.env` and the Alpaca credentials are working.

If you see `ALPACA_API_KEY not set in environment`, your `.env` isn't being
loaded — check the file is in the repo root and not `.env.txt`.

To test the Discord notifier separately:

```
python scripts/discord.py "smoke test" "hello from the bot"
```

You should see the message in the Discord channel attached to your
webhook. If `DISCORD_WEBHOOK_URL` is missing, the message lands in
`NOTIFICATIONS.md` instead of crashing.

## Cloud routine setup

Once `/portfolio` works locally, configure the production scheduled runs.

### One-time prerequisites

1. **Install the Claude GitHub App** on the repo (least privilege — grant
   access only to this one repo).
2. **Enable "Allow unrestricted branch pushes"** in the routine's environment
   settings. Without this, `git push origin main` silently fails.
3. **Set environment variables on the routine** (NOT in a `.env` file in the
   cloud):
   - `ALPACA_API_KEY`, `ALPACA_SECRET_KEY` (required)
   - `ALPACA_ENDPOINT`, `ALPACA_DATA_ENDPOINT` (optional)
   - `PERPLEXITY_API_KEY` (required for research)
   - `PERPLEXITY_MODEL` (optional, defaults to `sonar`)
   - `DISCORD_WEBHOOK_URL` (notifications)

### Create each routine

For each of the five workflows in `routines/`:

1. In Claude Code cloud: **Routines → New Routine**.
2. Name it (e.g. "Trading bot pre-market").
3. Select this repository, branch `main`.
4. Add the env vars from prereq 3.
5. Toggle on **Allow unrestricted branch pushes**.
6. Set the cron and timezone (see `routines/README.md`).
7. Paste the contents of `routines/<workflow>.md` into the prompt field
   **verbatim** — do not paraphrase. The env-var check and commit-push
   step are load-bearing.
8. Save, then click **Run now** to test.

## Notification philosophy

Most bots are chatty. This one is not.

- **Pre-market**: silent unless something is genuinely urgent.
- **Market-open**: only if a trade was placed.
- **Midday**: only if action was taken.
- **Daily-summary**: always sends, one Discord message, < 15 lines.
- **Weekly-review**: always sends, one Discord message, headline numbers.

The cost of a missed notification is low (you can always run `/portfolio`).
The cost of a chatty bot is high — you stop reading the messages and miss
the one that mattered.

## Repository layout

```
.
├── CLAUDE.md              # Agent rulebook (auto-loaded every session)
├── README.md              # This file
├── env.template           # Template for local .env
├── .gitignore             # Excludes .env
├── .claude/commands/      # Local slash commands (manual / testing)
├── routines/              # Cloud routine prompts (the prod path)
├── scripts/               # Python API wrappers — only way to touch the outside world
└── memory/                # Agent's persistent state (committed to main)
```

## Safety

- The wrapper scripts are the only path to external APIs. Never call them directly.
- The `trade.md` slash command refuses any order that fails a strategy rule.
- Memory is in Git — every change is auditable, reversible via `git revert`.
