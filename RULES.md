# Vault rules

Canonical source: `public/RULES.md`. An identical copy is distributed to every
repo by `scripts/distribute.sh`. **Edit the canonical copy, then redistribute** —
never edit a copy in place.

Each repo's `AGENTS.md` holds only what is specific to that repo and defers here
for everything else.

---

## 1. The one commitment

Plain Markdown in git. Every other component must pass this test: *if it
disappeared tomorrow, would I lose information, or only convenience?* If
information — reject it.

Practical consequence: a note must be useful when read as a plain text file, by a
human, with no tooling. No dependence on a plugin, a database, or a link graph.

## 2. Which repo

### The test, in one question each

| Repo | Ask yourself | Scope |
|---|---|---|
| **public** | *Would I put this on a blog?* | Knowledge **you produced** that would help a stranger: decisions with their reasoning, procedures you verified, syntheses you made. General criteria, rules and practices. |
| **personal** | *Would I show this to a friend or relative?* | **The default.** Preferences and things specific to you: hobbies, tastes, schedules, memberships, the systems you run, how you *think* about money and health. |
| **private** | *Only my spouse — or nobody?* | Secrets: actual financial status, medical status, credentials, legal matters, and lifestyle that cannot be shared. |
| **business** | *Is this about work, a client, or an employer?* | Projects, engagements, OKRs, meetings, rates, and an employer's own systems. |

These questions are the primary test. Apply them first; the ladder below only
settles cases where two of them both seem to say yes.

### public is not a dumping ground

"General knowledge" is not sufficient reason to keep a note. A personal knowledge
base gains nothing from facts you could look up again in ten seconds. What earns
a place in `public` is that **you made something**: a decision recorded with the
options you rejected, a procedure you actually verified, a synthesis nobody else
has written. If the note would be equally good copied from a search result, do
not keep it.

### The line that matters most: reasoning versus status

The same subject splits across two repos depending on whether it is *how you
think* or *what is true of you*.

| Reasoning → `personal` | Actual status → `private` |
|---|---|
| how to weigh a single-country overweight | the balances in each sleeve |
| how to model a withdrawal rate | the projected portfolio total |
| how to read a DEXA result | your body-fat percentage |
| which card benefits are worth the fee | your credit limits and balances |
| how to think about a contract term | the contract you signed |

**Financial problems, not financial status. Health practices, not medical
status.** The reasoning is reusable and shareable; the numbers identify you.

### Whose information is it?

`personal` versus `business` is **not** a sensitivity question — it is an
ownership one. A colleague's name is no more secret than your own; it simply is
not yours to record.

| Material | Repo |
|---|---|
| Your CV and career history | `personal` — your history, even though it names employers |
| Your homelab Kubernetes notes | `personal`, promotable to `public` sanitised |
| Your employer's cluster configuration | `business` |
| Generic QA or Kubernetes practice you wrote up | `public` |
| A colleague's or referee's contact details | **nowhere.** You are a custodian, not an owner |

Note the ambiguity in the word *reference*: technical reference material on work
*topics* is usually `public` or `personal`; only your employer's own
configuration is `business`.

### Family follows the same rule as you

Apply the four questions to a family member exactly as you would to yourself.
General context is `personal`; actual status is `private`.

| | |
|---|---|
| `personal` | first name, life stage, which university, that they play a sport |
| `private` | full legal name with exact date of birth, medical status, and anything revealing where they are at a given time |

**Time-bounded exception.** Eric is 17 until **2026-10-27**. Until then treat his
full name, date of birth and current school as `private` even in combination with
nothing else — a minor's whereabouts carries a risk an adult's does not. After
that date this paragraph is obsolete and the general rule above applies with no
exception; delete it.

### The ladder, for genuine ties

Ask in order. **Stop at the first yes.** Most restrictive wins.

1. Credential, legal/medical/identity document, actual financial status, or intimate? → **private**
2. Names or concerns an employer, client, colleague, or *their* systems? → **business**
3. Specific to you or your household, but shareable with a friend? → **personal**
4. Something you produced that anyone could read forever, with nothing identifying? → **public**
5. Still unsure → **personal**.

**Never default to public.** Publication is permanent. Promotion from `personal`
is a deliberate review step where the fact is *restated* in sanitised form, not
moved. Demotion does not exist.

### Then choose the folder

| Question | Folder |
|---|---|
| A dated log entry? | `daily/YYYY/MM/` |
| A machine or service you run? | `infra/hosts/`, `infra/services/` |
| Something that broke? | `infra/incidents/` |
| A procedure someone will follow? | `infra/runbooks/` |
| A claim about an investment? | `invest/thesis/` |
| A holding expressing a thesis? | `invest/positions/` |
| A dated decision and its reasoning? | `invest/journal/` |
| A standing rule you will not renegotiate mid-panic? | `invest/policy/` |
| A person, organisation, or meeting? | `people/`, `orgs/`, `meetings/` |
| Household or hobby? | `home/` |
| Mathematics? | `math/` |
| **Genuinely do not know yet?** | `inbox/` — then triage weekly |

`inbox/` is a real answer, not a failure. Filing wrongly costs more than filing
late. Leaving it there past 30 days is the only unacceptable outcome.

## 3. How much detail — four tiers

Depth follows **durability and reuse**, never the length of the source. A
two-hour conversation may deserve four lines; a one-line decision may deserve a
page.

| Tier | Keep | Applies to |
|---|---|---|
| **Decision** | Everything needed to re-evaluate later: the context that forced it, options considered and rejected *with reasons*, the decision, its consequences, and what would reverse it | `decisions/`, `invest/thesis/`, `invest/journal/`, `infra/incidents/` |
| **Reference** | The conclusion, the numbers, and where they came from. Drop the derivation | `reference/`, `glossary/`, `infra/hosts/`, benchmarks |
| **Volatile** | The figure, the date it was observed, and where to reverify. Nothing else | prices, fees, policies, availability, admissions rules |
| **Discard** | Nothing. Do not create a note | one-off lookups, filler, near-duplicates of an existing note |

The test for Decision tier: **would a stranger — or you in two years — understand
why, and be able to disagree?** If the reasoning is missing, the note is a
record of an outcome, not a decision.

The test for Discard: **would you ever re-read it?** If not, it is noise. An
inbox nobody reads is worse than no inbox.

### Volatile content

Mark it `time_sensitivity: volatile` in frontmatter, and state the observation
date inline next to the figure:

```markdown
GLM-5.3-Flash: $0.15/M input, $0.50/M output (observed 2026-09-05, z.ai pricing page)
```

A volatile figure with no date is worse than no figure — it will be trusted long
after it stopped being true.

### Captured chat conversations, specifically

A conversation is **not** an artefact worth keeping. What was concluded is.
`watcher.py` therefore files a distilled note and **discards the transcript**.
A manual import should produce the same shape.

Every captured note carries:

| Section | Content |
|---|---|
| Frontmatter | `source:` naming the export, plus the source URL and turn count in the body |
| **Summary** | Exactly 3 bullets. What was *concluded* — never "the user asked about X" |
| **Details** | 3–10 bullets: figures verbatim, options considered *and why they were rejected*, constraints, unresolved questions |
| Provenance | which provider distilled it, and a note that the transcript was not retained |

**The Details section replaces the transcript, so anything omitted there is
gone.** That is the whole discipline: decide what matters while you still have
the original, not later.

What gets dropped: greetings, restatements, clarifying exchanges, dead ends that
led nowhere, and the model's own hedging. A two-hour conversation may deserve
four bullets. A three-line exchange that settled a decision may deserve a page.

Two cases keep the full transcript, both flagged `needs-review`:

- content held back from the summariser because it matched a secret or
  private-address pattern — it was never read, so there is nothing to distil
- every provider failed — better a raw note than a lost one

Both are temporary states. Distil by hand, then delete the transcript.

### Worked example

A 6-turn conversation about market-data APIs, ~180 lines of transcript, became a
33-line note:

```markdown
## Summary
- Adopted a free stack: Stooq for prices, SEC EDGAR XBRL for fundamentals,
  FRED for macro — no API keys, no rate limits, ~95% of the stated need.
- Alpha Vantage rejected: 25 requests/day is too tight for a daily refresh
  of a few dozen tickers. Rejected on rate limits, not data quality.
- EODHD at $19.99/mo is the paid fallback if global coverage is needed.

## Details
- Requirement narrowed to daily closes and dividends only — that is what
  made the free stack viable.
- Prices compared: Marketstack ~$9.99, EODHD ~$19.99, FMP ~$22, Finnhub $49–80.
- EODHD caveat: fundamentals sit behind a higher tier, not the base plan.
- Trigger for revisiting: needing non-US coverage.
```

Note what survived: every figure, the rejected option *with its reason*, and the
condition that would reverse the decision. Note what did not: the questions, the
narrowing, and the model's caveats. Someone reading this in a year can act on it
or disagree with it, which is the test in §3.

## 4. Note anatomy

### Frontmatter — required, lint-enforced

```yaml
id: 01M1R7H0WBG1D3MZJVSQKT6X7M   # ULID, immutable, never edit
title: "..."                      # specific noun phrase, max ~60 chars
repo: personal                    # must match the directory
tags: [host, benchmark]           # from the repo's tags.txt, 1-5
created: 2026-09-05
updated: 2026-09-05               # bump on every edit
```

Optional, and used where they earn their place: `source:` (what import or export
it came from), `sensitivity:`, `importance:`, `time_sensitivity:`.

### Titles

A title is the filename slug and the primary retrieval handle. Name the
**specific thing or decision**, not the topic.

- Good: `Switching from flake8 to Ruff on a 40k-line codebase`
- Bad: `Linting tools comparison`

### Size

Past **~200 lines** a note is usually two notes. Split by *question answered*,
not by topic size. A note that answers three unrelated questions is three notes
that will each be found more easily alone.

Exception: append-only logs (`daily/`, `invest/journal/`) grow without limit by
design and are never split.

### Creating notes

```
scripts/newnote.sh <path/slug> "<title>" [template]
```

**This is the only correct way.** It generates the ULID. Writing a note file
directly means inventing an `id`, and lint will reject it. An agent that cannot
run the script should output the content and let a human create the note.

## 5. Tags

The principle: **tag only what full-text search cannot find.**

A note mentioning Chase is already findable by searching `Chase`. A note that
*is a decision* is not — nothing in its text says so. So `decision` is a useful
tag and `chase` is not.

Consequences:
- Tags are **facets**, not keywords. Domain, note type, and status.
- Specific entities — people, companies, tickers, product names, places — belong
  in the title and body, never in tags.
- Each repo has a controlled vocabulary in `tags.txt`, enforced by lint. Adding a
  tag is a deliberate edit to that file, not something done in passing.
- 1–5 tags. A note needing more than five has not been split.
- English only, like every other artifact in this vault.

## 6. Links

`[[slug]]`, and **only to notes inside the same repo**. Lint enforces this.

Cross-repo links are forbidden by design. To use something from a more private
repo in a more public one, restate the sanitised fact. The friction is the point:
it forces a conscious decision at the moment of disclosure.

Inline code is exempt, so documentation can write `[[slug]]` as an example.

## 7. Append, supersede, retain

- **Append-only:** `daily/`, `invest/journal/`. Never retroactively edit.
- **Frozen after sign-off:** `infra/incidents/`. Correct the record in a new note.
- **Supersede, do not delete:** mark stale content `> superseded by [[slug]]` and
  leave it. The history of a wrong belief is often the useful part.
- **`inbox/` is the only unstructured folder.** Triage weekly. An item older than
  30 days is either filed or deleted — never left to rot.
- **Volatile notes** whose observation date is over a year old are reverified or
  marked superseded.

## 8. Secrets

Reference a secret's location, never its value: "Bitwarden → kb-private
git-crypt key". No exceptions, in any repo. Git history is permanent — a value
committed once is committed forever, and rewriting history is unreliable.

## 9. Before finishing

```
python3 scripts/lint.py
```

The pre-commit hook runs it and refuses the commit on failure. `--no-verify`
exists for genuine emergencies and is not one of them.
