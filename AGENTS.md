# kb-public

**Read `RULES.md` and `WORKING-RULES.md` first.**

- `RULES.md` — what a note must contain, which repo it belongs in, the four
  detail tiers, frontmatter, tags and links. Shared across all four repos.
- `WORKING-RULES.md` — how to behave while working: command output, change
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

Lint mechanically blocks private IPs and `.internal`/`.local`/`.lan` hostnames
**in this repo only**. That is a backstop for the cases a regex can catch, not a
substitute for reading what you are about to publish.

## Layout
- `glossary/` — term definitions, one concept per note
- `howto/` — generic procedures with no local specifics
- `sources/` — reading notes on public material
- `infra/` — homelab writeups, sanitised
- `decisions/` — ADRs safe to publish
- `RULES.md` — **canonical** shared rules. Edit here, then run
  `personal/scripts/distribute.sh`

## Writing for an audience

Notes here are read by strangers with no context. A note that assumes knowledge of
this vault, this household or this hardware belongs in `personal`. Where a public
note draws on private material, state the general principle rather than the
specific instance.

## Paths
Your working directory IS the repo root. Never prefix paths with `kb/`, `public/`
or the project name.

## Before finishing
`python3 scripts/lint.py`
