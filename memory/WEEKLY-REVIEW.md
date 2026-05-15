# Weekly Review

Friday reviews appended here.
Template for each entry:

## Week ending YYYY-MM-DD

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $X |
| Ending portfolio | $X |
| Week return | ±$X (±X%) |
| S&P 500 week | ±X% |
| Bot vs S&P | ±X% |
| Trades | N (W:X / L:Y / open:Z) |
| Win rate | X% |
| Best trade | SYM +X% |
| Worst trade | SYM -X% |
| Profit factor | X.XX |

### Closed Trades
| Ticker | Entry | Exit | P&L | Notes |

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized | Stop |

### What Worked
- ...

### What Didn't Work
- ...

### Key Lessons
- ...

### Adjustments for Next Week
- ...

### Overall Grade: X

## Week ending 2026-05-01

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $10,000.00 |
| Ending portfolio | $10,013.34 |
| Week return | +$13.34 (+0.13%) |
| S&P 500 week | ~+1.12% (7,165 → ~7,245) |
| Bot vs S&P | -0.99% |
| Trades | 1 (W:0 / L:0 / open:1) |
| Win rate | n/a (no closed trades) |
| Best trade | XLB +0.90% (open) |
| Worst trade | XLB +0.90% (only position) |
| Profit factor | n/a |

### Closed Trades
| Ticker | Entry | Exit | P&L | Notes |
| — | — | — | — | None this week |

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized | Stop |
| XLB | $50.88 | $51.34 | +$13.34 (+0.90%) | $46.59 (10% trail, hwm $51.77) |

### What Worked
- Strict patience Mon-Wed: stayed 100% cash through stacked binaries (FOMC + Mag7 + GDP/PCE) — no premature loss.
- Entry timing on XLB: post-PCE pullback into $50.50-51.50 buy zone, not chasing.
- Sector selection: Materials in RRG Leading quadrant; avoided event-binary Energy and RRG-Lagging Tech despite Mag7 noise.
- 10% trailing GTC stop placed on entry per rule 4 — no manual babysitting required.
- Discipline on Friday: refused to chase AAPL gap; preserved 2/3 weekly trade slots.

### What Didn't Work
- Underdeployed: ~85% cash all week vs 75-85% target's lower bound; missed broad market +1.1% lift.
- Single position only — concentration in one sector ETF means tracking error on a strong tape.
- Lagged S&P by ~99 bps in a week where the index made new highs — pure opportunity cost.
- Perplexity API 401 every day — relying entirely on WebSearch fallback; no autonomous research path.
- Slow ramp: 4 days flat before first deployment is on the edge of "patience" vs "paralysis."

### Key Lessons
- Patience prevented losses but also prevented participation; in a melt-up tape, even 1-2 starter positions Mon/Tue would have closed the gap.
- Single-ETF deployment ≠ diversification; second uncorrelated leader (XLI/XLP) should have been a higher priority by Thursday.
- Catalyst-anchored entries (post-event) work — XLB entry was clean and immediately green.
- Perplexity outage is structural this week; need to fix key or formalize WebSearch as primary.

### Adjustments for Next Week
- Target 2-3 positions by Wed close, push deployment toward 75-80% (rule 2 floor).
- Add an uncorrelated Leading-quadrant name (XLI Industrials or XLP Staples) on first clean pullback.
- Re-verify PERPLEXITY_API_KEY validity Mon AM; if still 401, escalate via Discord alert.
- If XLB hits +15% (~$58.51), tighten trail to 7% per rule 6; not close yet.
- Hold the line on rule 8 (max 3 new trades/week) — quality > quantity.

### Overall Grade: C+
Capital preserved, one clean entry, all rules followed — but underdeployment cost ~1% vs benchmark in a record-high week. Discipline grade A; participation grade D.

## Week ending 2026-05-15

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $10,020.59 |
| Ending portfolio | $9,983.18 |
| Week return | -$37.41 (-0.37%) |
| S&P 500 week | ~+1.4% (SPX cleared 7,500 ATH Thu, gave a bit back Fri) |
| Bot vs S&P | ~-1.77% |
| Trades | 0 new (W:0 / L:0 / open:1 XLB carry-over) |
| Win rate | n/a (no closed trades) |
| Best trade | XLB +2.71% (Mon intra-week peak, only position) |
| Worst trade | XLB -1.14% (Fri close, only position) |
| Profit factor | n/a |

### Closed Trades
| Ticker | Entry | Exit | P&L | Notes |
| — | — | — | — | None this week |

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized | Stop |
| XLB | $50.88 | $50.30 | -$16.82 (-1.14%) | $47.49 (10% trail, hwm $52.77) |

### What Worked
- Trailing stop discipline: server-side GTC at $47.49 (hwm $52.77 set Wed of prior week) — held through Fri -2.65% flush, no panic action.
- Avoided every binary trap: Powell→Warsh Fed transition Fri, hot PPI Wed (+1.4% MoM), Iran ceasefire "life support" — zero exposure beyond XLB.
- No cyclical stacking: refused XLI add despite Leading-quadrant signal, recognizing correlation with held Materials.
- No Tech chase into NVDA next week: XLK flipped Leading mid-week but discipline preserved slots for post-print setup.
- 3/3 trade slots dry preserved heading into NVDA + WMT week.

### What Didn't Work
- Lagged S&P by ~1.77% in a week SPX cleared 7,500 ATH — second consecutive week of meaningful tracking error.
- XLB now red on cost (-1.14%); RRG flagged Materials losing relative momentum mid-week, did not act to trim or tighten ahead of Fri flush.
- Hot PPI Wed was a yellow flag for cyclicals (XLB inflation-sensitive) — recognized in research log but not actioned.
- Single-position concentration continues: 14.6% deployed, ~85% cash for THIRD straight week despite stated 75-85% deployment target.
- Perplexity 401 persists 15 sessions running — research path entirely WebSearch-dependent; no autonomous primary source.

### Key Lessons
- "Wait for clean setup" + "preserve slots" has compounded into 2 weeks of zero new entries; the rule reads as patience but the behavior is paralysis.
- Sector momentum decay (XLB RRG Velocity weakening) is itself a signal — not just an entry filter but a trim/risk-management input.
- Friday weekend gap risk goes both ways: avoiding fresh entries also means not de-risking when a position is fading into a stacked-binary close.
- Underdeployment beats the index in down weeks but bleeds in up weeks; the current 85% cash regime is structurally bearish against a melt-up tape.

### Adjustments for Next Week
- Mandatory action: by Wed close, either add 1-2 uncorrelated Leading-quadrant positions OR document explicit reason against (not "preserve slots" — must name the disqualifying risk).
- Watchlist priority post-NVDA print: SMH/XLK pullback to 21-EMA (Tech now Leading); XLE only if Iran tape resolves; XLI off the list (correlated with XLB).
- XLB manual -7% trigger at $47.32 ($50.88 × 0.93); set a calendar check at every -0.5% incremental drawdown. If RRG keeps deteriorating into Tue, consider trim half pre-NVDA.
- Re-verify PERPLEXITY_API_KEY Mon AM; if still 401, formally adopt WebSearch as primary in TRADING-STRATEGY.md.
- No strategy rule changes this week (only 3 weeks of data; need 2+ weeks of proven failure).

### Overall Grade: C-
Rules followed flawlessly, capital preserved within tolerance, no blowups. But two straight weeks of -1% to -2% tracking error in a melt-up tape is not "discipline" — it's a participation failure. XLB now red on cost after holding gains all week; risk-management instincts (trim on RRG decay + hot PPI) were available and not used. Discipline grade B+; participation/execution grade D.
