---
id: 01M1VWXJHG8WX96MQDC6H6NSNN
title: "Survival odds come from life tables, not a Gaussian"
repo: public
tags: [reference, health]
created: 2026-09-06
updated: 2026-09-06
---

# Survival odds come from life tables, not a Gaussian

**Scope:** How to estimate the probability of reaching a given age, and why the
obvious normal-distribution shortcut is wrong. Excludes cause-specific mortality
and individual risk modelling.

## Conclusion

**Read survival probabilities off a published life table. Never fit a Gaussian to
lifespan.**

Lifespan is strongly **right-skewed**: infant and young-adult deaths cluster in
the left tail while the right tail stretches past 90. A symmetric normal misfits
it badly. Worked failure, below, understated the true value by 16 percentage
points.

Two consequences that trip people up:

1. **Mean life expectancy at birth is well below the 50%-survival age.** For
   Chinese men, life expectancy at birth is ~75 yet roughly **50% reach 80**.
   "Average lifespan 75" and "half of men reach 80" are both true and entirely
   consistent — early deaths drag the *mean* below the *median*. If you reason
   from life expectancy at birth to "my odds of reaching 80", you will be wrong,
   and wrong in the pessimistic direction.
2. **Life-table survival counts deaths from *all* causes**, accidents included.
   These are not "death from natural causes only" figures.

## Verify

```
US male (authoritative, checkable):
  SSA actuarial life table — https://www.ssa.gov/oact/STATS/table4c6.html
  Read l_x / 100,000 at the age of interest.
  Age 80 ≈ 0.57, age 85 ≈ 0.43, age 90 ≈ 0.20.
US female:
  NCHS United States Life Tables —
  https://www.cdc.gov/nchs/products/life_tables.htm
China:
  China NBS — https://www.stats.gov.cn
  No exact period table was located; the figures below are unverified.
```

## Figures — treat as unverified approximations

These came from an unnamed "latest life tables" and were never traced to a
specific table or vintage. **Verify against an official source before relying on
any of them.** They are recorded because the *shape* is instructive, not because
the digits are trustworthy.

| Age reached | CN men | CN women | US men | US women |
|---|---|---|---|---|
| 50 | 93% | 96% | 94% | 97% |
| 60 | 84% | 90% | 87% | 92% |
| 70 | 71% | 80% | 77% | 84% |
| 75 | 55% | 70% | 64% | 75% |
| 80 | ~50% | ~68% | ~57% | — |
| 85 | ~31% | ~50% | ~43% | — |
| 90 | ~10% | ~28% | ~20% | — |
| 100 | near 0 | near 0 | — | — |

In this set, **US figures exceed Chinese ones at every age and both sexes**
(male at 80: ~57% vs ~50%).

## Failures

- **A Gaussian with mean 75 and sd 12 gave P(reach 80) ≈ 34% for Chinese men,
  against ~50% from life tables.** Two compounding errors: the distribution is
  right-skewed rather than normal, and the ad-hoc sd of 12 was itself too high.
  The shortcut is not merely imprecise — it is biased low, because a symmetric
  distribution cannot represent a population that loses mass early and then
  survives long.

## Rejected

| Option | Reason |
|---|---|
| Gaussian lifespan model | Lifespan is right-skewed; the fit understates survival to advanced ages by a wide margin |
| Deriving "exceeds X% of peers at age 80" from mean life expectancy alone | Impossible without age-specific mortality data. Life expectancy at birth is a single summary statistic and carries no distributional information |

## Open

- Which authoritative Chinese table (census-based, or an insurance-industry
  table) reproduces the CN column is unresolved.
- US female survival past 75 and survival to 100 were never given as numbers.
