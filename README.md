# alphaengine

> An AI-powered architect for the Nifty 500. I built this as a grade 12
> project to teach myself how real software gets built — not how to
> predict stock prices, but how to engineer a working application
> from the ground up.

---

## What it does

AlphaEngine guides me through five stages of portfolio construction:

1. **Screen** the Nifty 500 by sector and technical filters
2. **Select** candidate stocks from the screener output
3. **Optimize** weights using Markowitz mean-variance optimization
4. **Simulate** outcomes via Monte Carlo (GBM + bootstrap)
5. **Explain** the portfolio in plain English using Claude

What it does *not* do: predict prices, place trades, or give financial
advice. It's a research tool, not an oracle.
