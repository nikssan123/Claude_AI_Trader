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

## Entry Checklist
- Specific catalyst?
- Sector in momentum?
- Stop level (7-10% below entry)
- Target (min 2:1 R:R)
