---
id: 01M1V6T6JSDB921PMCHBWH76DP
title: "Global $1M+ households: ~35-45M; ~57.5-60M individuals"
repo: public
tags: [reference, finance, volatile, import]
created: 2026-09-06
updated: 2026-09-06
source: chatgpt-export-2026-09-05
---

# Global $1M+ households: ~35-45M; ~57.5-60M individuals

**Source:** ChatGPT — https://gemini.google.com/app/4fb616879b9bb356
**Exported:** 2026-09-06T09:48:28.102Z
**Turns:** 2

**Scope:** Covers global counts of households/individuals with $1M+ USD net worth and the two counting standards (total assets vs investable assets); not investment advice, no per-country detail beyond the top 4.

## Conclusion

Answer to 'how many households worldwide exceed $1M USD': an estimated 35-45 million households. Institutions typically report individuals, not households: ~57.5-60 million adult millionaires, ~1% of the global adult population, holding ~40% of personal wealth. Top countries: US ~23.6M, China ~5.3M, Japan ~2.9M, Germany ~2.65M (US + China together >50% of the global total). Distribution: 90%+ of millionaires hold $1-5M (~52M 'everyday millionaires', wealth built from property appreciation, financial investment and accumulation); ultra-high-net-worth ($30M+) is ~250,000-600,000 people globally. The definition changes the count: UBS counts total net assets (real estate, equities, bonds, cash minus all liabilities, incl. primary residence); Capgemini/BCG count investable assets only (excludes primary residence and illiquid luxury assets), which yields ~25 million HNWI under the strict standard.

## Verify

```
curl -sL 'https://www.ubs.com/global/en/wealth-management/insights/global-wealth-report.html' | grep -oiE '[0-9.]+ ?(million|billion)' | head -n 10
Cross-check the top-4 ordering (US, China, Japan, Germany) against the latest UBS Global Wealth Report and Capgemini World Wealth Report country tables
```

## Facts

- Global millionaires (individuals): ~57.5-60 million, ~1% of global adult population, controlling ~40% of personal wealth
- Estimated 35-45 million households worldwide hold >$1M USD
- Country counts: US ~23.6M; China ~5.3M; Japan ~2.9M; Germany ~2.65M; US+China >50% of the global total
- 90%+ of millionaires are in the $1-5M band; ~52 million are 'everyday millionaires' whose wealth comes from property appreciation, financial investment and accumulation
- Ultra-high-net-worth ($30M+): ~250,000-600,000 people globally
- UBS methodology: total net assets = all assets (real estate, equities, bonds, cash) minus liabilities, including primary residence
- Capgemini/BCG methodology: investable assets only, excluding primary residence and illiquid luxury assets; yields ~25 million HNWI

## Rejected

| Option | Reason |
|---|---|
| Counting households directly as the headline metric | Institutions count adult individuals (HNWI) instead, because some households contain multiple millionaires; the household figure is a derived estimate (35-45M), not an official statistic |
| Investable-assets definition (Capgemini/BCG) as the headline count | Excludes primary residence and illiquid assets, yielding ~25M HNWI; it answers 'investable wealth >$1M', a different question from total net worth >$1M |

## Open

- The household-level count (35-45M) is an estimate; no institution publishes millionaires measured per household
- UHNW ($30M+) figure given as a wide range (250k-600k people); exact source year and figure not pinned down
- Figures were quoted without a specific report edition/year; should be re-anchored to the latest UBS Global Wealth Report before reuse

## References

- https://www.ubs.com/global/en/wealth-management/insights/global-wealth-report.html — UBS Global Wealth Report - source of total net assets methodology and country millionaire counts
- https://www.capgemini.com/insights/research-library/world-wealth-report/ — Capgemini World Wealth Report - source of the investable-assets HNWI definition (~25M)
- https://www.bcg.com — BCG Global Wealth Report - co-source of the investable-assets HNWI methodology

---

*Distilled from a 2-turn ChatGPT conversation by glm-5.3-flash. The transcript was not retained; the source URL above is the only route back to it.*
