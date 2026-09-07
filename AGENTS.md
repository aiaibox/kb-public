# kb-public

**Read `../base/RULES.md` and `../base/WORKING-RULES.md` first.**

- `../base/RULES.md` — what a note must contain, which repo it belongs in, the four
  detail tiers, frontmatter, tags and links. Shared across all four repos.
- `../base/WORKING-RULES.md` — how to behave while working: command output, change
  summaries, exact CLI, naming the machine, time estimates.

This file holds only what is specific to `public`.

## What makes this repo different

It is **world-readable, permanently**. Git history is not meaningfully erasable,
so treat every commit as irreversible publication. This is the only repo where a
mistake cannot be corrected by editing.

Consequence: nothing arrives here by default. Material is *promoted* from
`personal` by restating the sanitised fact, never by moving a file.

## Never commit
- Names of private individuals, employer names, client names
- Internal hostnames, IP addresses, network topology
- Credentials of any kind, including examples that look real
- Anything copied from another repo without sanitising first

`scripts/lint-local.py` — this repo's own rule, run as part of base lint — blocks
private IPs and `.internal`/`.local`/`.lan` hostnames **in this repo only**. That is a backstop for the cases a regex can catch, not a
substitute for reading what you are about to publish.

## Layout — 5 top-level, no inbox

- `decisions/` — ADRs on generic technical choices: chosen, rejected, why
- `howto/` — reproducible procedures with no personal or employer specifics
- `notes/` — `glossary/` one term per note · `reading/` notes on others' work
- `research/` — research status and progress
- `writing/` — essays, long-form, talks

**There is deliberately no `inbox/`.** `sync.sh` pushes this repo automatically,
so anything landing here reaches a world-readable remote before review.
Nothing is *routed* to `public` — material arrives because it was written for
here, or promoted by restatement from `personal` (see `RULES.md` §2).

## Writing for an audience

Notes here are read by strangers with no context. A note that assumes knowledge of
this vault, this household or this hardware belongs in `personal`. Where a public
note draws on private material, state the general principle rather than the
specific instance.

## Paths
Your working directory IS the repo root. Never prefix paths with `kb/`, `public/`
or the project name.

## Before finishing
`python3 ../base/scripts/lint.py` — one copy, in `kb-base`; the repo is where you run it
