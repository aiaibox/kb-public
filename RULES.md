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
| Cards, banking, spending, points? | `finance/` |
| A claim about an investment? | `finance/invest/thesis/` |
| A holding expressing a thesis? | `finance/invest/positions/` |
| A dated decision and its reasoning? | `finance/invest/journal/` |
| A standing rule you will not renegotiate mid-panic? | `finance/invest/policy/` |
| A trip, a redemption, a place visited? | `travel/` |
| An order, a return, a retailer dispute? | `shopping/` |
| Training or health *practice*? | `health/` — actual medical status is `private/` |
| A person, organisation, or meeting? | `people/`, `orgs/`, `meetings/` |
| Household, garden, pets? | `home/` |
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
| **Decision** | Everything needed to re-evaluate later: the context that forced it, options considered and rejected *with reasons*, the decision, its consequences, and what would reverse it | `decisions/`, `finance/invest/thesis/`, `finance/invest/journal/`, `infra/incidents/` |
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

A conversation is **not** an artefact worth keeping. What was concluded is. The
transcript is discarded; only the distillation survives. The goal for every
captured note is that the solution is:

- **repeatable** — someone can re-execute it, because the exact commands and
  values are present and there is a check that proves it worked
- **traceable** — someone can verify where it came from, because every source is
  linked and every measured number carries its date and method

Use the `capture` template, or let `watcher.py` produce it automatically.

| Section | Content |
|---|---|
| **Scope** | One line: what this covers **and what it does not** |
| **Conclusion** | The answer, actionable. Commands, config and values *verbatim*, never described |
| **Verify** | The concrete check that proves it worked. **This is what makes the note repeatable** |
| **Decided** | What was committed to — only when it differs from the conclusion |
| **Facts** | Durable specifics, figures verbatim. Measured numbers carry date and method inline |
| **Rejected** | Every option considered, with the reason it lost. Prevents re-proposing |
| **Failures** | What broke and its *actual* cause. Prevents re-debugging |
| **Open** | What is unresolved. Often the most valuable line in the note |
| **References** | Every URL, service or document named, with what it was used for |

### What to leave out

- Repeated questions and repeated answers
- Greetings, sign-offs, pleasantries, and the model's own hedging
- Restating the question back
- Narration of reaching the conclusion — keep the destination, not the walk
- Generic background that could simply be looked up
- **Anything about the *conversation* rather than the *subject*.** Write "three
  options exist: A, B, C", never "we discussed three options". The conversation
  is scaffolding and comes down when the note is built.
- Intermediate wrong answers — **unless someone would independently make the
  same mistake.** Those belong in Failures. A typo does not; a misleading error
  code does.

### Two things Verify buys you

**It falsifies stale advice.** The first real test of this schema produced a note
recommending a "free, keyless, just curl it" data source. Running the generated
check showed the service now returns an anti-bot challenge — the recommendation
had silently stopped working. Without a Verify section that claim would have
entered the vault as fact.

**It surfaces missing prerequisites.** The same note added a required HTTP header
that the source conversation never mentioned. Testing confirmed the call returns
403 without it. A conclusion that omits a prerequisite is not repeatable, and only
a check reveals the omission.

### Edge cases

**No conclusion reached.** An exploratory conversation still earns a note, but it
is mostly **Open**, tagged `needs-review`, and short. It must not dress wandering
up as a finding.

**A conclusion spanning several conversations.** Update the *existing* note rather
than adding a second. Bump `updated:`. If the new position reverses the old, mark
the superseded text `> superseded by …` and keep it — per §7, the history of a
wrong belief is often the useful part.

**Held back or no summary.** If content matched a secret pattern it was never sent
anywhere, so there is nothing to distil: the full transcript is kept and tagged
`needs-review`. Same if every provider failed. Both are temporary states — distil
by hand, then delete the transcript.

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

### Size — one note, one question

**Split a note when its sections are independent subjects. Do not split it when
they are steps in one sequence, however many there are.**

Line count is not the measure. A runbook with fifteen numbered steps is one
question — *how do I do this?* — and splitting it mid-procedure makes it worse,
because the reader would follow steps across two files. A design document with
nine unrelated sections is nine questions wearing one filename, and it should
split however short it is.

The test: **could you give one section a specific title and would anyone search
for it on its own?** If yes, it is a note. If it only makes sense in sequence
with its neighbours, it is a section.

**Technical ceiling: roughly 600 lines.** Past that a note exceeds the embedding
model's 8192-token window and gets silently truncated by semantic search, so the
tail becomes unfindable. This is a real limit with a real cause — not a style
preference — and it is generous: the largest note in this vault is 389 lines
(~4,800 tokens, 59% of the window).

> That ceiling disappears if `semantic.py` embeds **per heading** rather than per
> note, which is the better design anyway. Treat 600 as a property of the current
> indexing approach, not of the vault.

Append-only logs (`daily/`, `finance/invest/journal/`) grow without limit by design.
They need no exemption from the rule above: a continuous dated record *is* one
question.

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

- **Append-only:** `daily/`, `finance/invest/journal/`. Never retroactively edit.
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
