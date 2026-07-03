# Trading Strategy

## Mission
Beat the S&P 500 over the challenge window. Stocks only — no options, ever.

## Capital & Constraints
- Starting capital: ~$10,000
- Platform: Alpaca PAPER (simulated; switch to live after the bot proves out)
- Instruments: Stocks ONLY
- PDT limit: 3 day trades per 5 rolling days (account < $25k)

## Core Rules
1. NO OPTIONS — ever
2. 75-85% deployed
3. 5-6 positions at a time, max 20% each
4. 10% trailing stop on every position as a real GTC order
5. Cut losers at -7% manually
6. Tighten trail: 7% at +15%, 5% at +20%
7. Never within 3% of current price; never move a stop down
8. Max 3 new trades per week
9. Follow sector momentum
10. Exit a sector after 2 consecutive failed trades
11. Patience > activity
12. **Forced-Action Protocol** — if 2+ consecutive Fridays close with deployment <75% AND 0/3 weekly trade slots used, the following Monday is a mandatory-action session: either deploy on the single highest-conviction Leading-quadrant uncorrelated ETF OR log an explicit per-ticker disqualifying risk for each Leading-quadrant candidate in that day's research entry. "Preserve slots for cleaner setups" is NOT an acceptable standalone disqualifier. Position sizing under this rule still respects all other rules (3, 5, 8, 9, 10).
    - **12a. Disqualifier-freshness clause** (added 2026-06-13 after 2-week recycled-disqualifier pattern Mon 6/01 + Mon 6/08): if the Path-B per-ticker disqualifier set is >50% verbatim from the prior week's Path-B entry, the trigger is NOT satisfied. Path A (deployment on the single highest-conviction Leading-quadrant uncorrelated ETF) becomes the default. Each disqualifier must be rooted in this week's tape and reference a catalyst, print, or RRG shift from the current week.
    - **12b. Intra-week flush trigger** (added 2026-06-13; oversold-prong RELAXED 2026-07-03 after Tue 6/23 + Mon 6/29 near-misses): if a held position closes within $3 of its GTC trail OR ≤2% above its manual -7% cut AND a Leading-quadrant ETF is oversold (>1.5 standard deviations below 21-EMA OR closes in the lower 15% of its 20-day range OR closes within 2% of its 20-day low), the next session is a mandatory Path-A scan regardless of weekly cap status. Path-B disqualification still permitted but must clear the 12a freshness bar AND the 12c catalyst-specificity bar.
    - **12c. Path-A Default-Flip clause** (added 2026-07-03 after 4 review-cycle deferral + Mon 6/29 fresh-Path-B no-action outcome): if Rule 12 triggers AND a Leading-quadrant uncorrelated ETF has a same-week catalyst-confirmed thesis — defined as any of: (i) FOMC / PCE / NFP / CPI / ISM print with directional read, (ii) geopolitical resolution signature (ceasefire signed, deal completed, sanction change), (iii) DJIA or sector-composition change, (iv) RRG quadrant transition confirmed by weekend/premarket read — then Path A (deployment on the single highest-conviction such ETF) is the DEFAULT. Path B remains permitted but each disqualifier must specifically address the catalyst-confirmed thesis — generic risk factors ("chase risk," "wrong holding window," "single-day bounce") are NOT acceptable as standalone disqualifiers under 12c. Sizing under 12c respects all other rules; default deployment size is 10-15% of equity on first entry.
13. **Operational-Trigger Logging** (added 2026-07-03 after 2-week deferral + Mon 6/15 silent-passage of May 29 XLB partial-add trigger): any operational add-trigger or trim-trigger explicitly defined in a prior week's review — including but not limited to: hwm-break partial-adds, RRG-Velocity-red trim mandates, pivot-level breaks — requires explicit Y/N logging in the research entry for the trigger day, with rationale. Silent passage of a known operational trigger is an unforced procedural error and must be flagged in the next weekly review.

## Research Tooling
- Perplexity API has returned 401 invalid_api_key for 35+ consecutive sessions (since 2026-04-28). Treated as a permanent structural blocker.
- **WebSearch is the formal primary research path going forward.** Do not log "fell back to WebSearch" as a per-day status — it is the default.

## Entry Checklist
- Specific catalyst?
- Sector in momentum?
- Stop level (7-10% below entry)
- Target (min 2:1 R:R)
