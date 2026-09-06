---
id: 01M1SQQC339FMTVPF9MZTNXAQN
title: "Separating a knowledge base by sensitivity"
repo: public
tags: [privacy, git]
created: 2026-09-05
updated: 2026-09-05
---

# Separating a knowledge base by sensitivity

**Status:** accepted
**Date:** 2026-09-05

## Context

A personal knowledge base accumulates material with very different disclosure
requirements: notes worth publishing, notes that are merely private, commercial
material, and material that must never leave the machine. A single repository
forces the strictest requirement onto everything, or — worse — invites a mistake
where the strictest material ends up under the loosest rules.

Git makes that mistake permanent. History is not meaningfully erasable once
pushed, so the boundary has to be structural rather than a matter of care.

## Decision

Four independent git repositories, separated by what may be disclosed rather
than by subject matter. Three sit under one editor workspace; the fourth
deliberately does not.

| Repository | Holds | Remote |
|---|---|---|
| `public` | Notes written for publication: glossary, generic how-tos, reading notes, sanitised infrastructure writeups, decision records like this one | Public |
| `personal` | Everyday private knowledge: domain notes, daily log, reference material distilled from AI chat history | Private |
| `business` | Commercial and client material | Private |
| *(separate)* | Legal, medical, estate, and **private topics** | Private, encrypted at rest |

The fourth repository sits outside the editor workspace entirely. It is not
indexed, not searched, and not passed to any AI agent. Its folder permissions are
owner-only, and no automation touches it: the sync script iterates an explicit
list of the other three, so it cannot be included by accident.

Its contents are encrypted at rest before reaching any remote, so the host stores
ciphertext only. Because that scheme encrypts file contents but not file names,
the names are deliberately non-descriptive — a readable filename would leak the
subject of a note whose text is protected. Passwords and keys are not kept here
at all; they belong in a password manager, because git history is permanent.

## Consequences

**Links never cross a repository boundary.** A wikilink resolves only within its
own repo. To use something from a more private repo in a more public one, the
fact is restated in sanitised form rather than linked. This is deliberate
friction — it forces a conscious decision at the moment of disclosure.

**Material moves one way.** Promoting a note from private to public is a review
step. The reverse does not exist, because publication cannot be undone. Anything
uncertain therefore starts private.

**A linter enforces what it can.** Required frontmatter, unique identifiers,
resolvable links, and — in the public repo only — a check for private network
addresses and internal hostnames. A pre-commit hook refuses commits that fail.
This catches mechanical mistakes; it does not replace judgement about content.

**The cost is duplication.** Shared tooling — the linter, the note creator, the
templates — exists as an identical copy in each repository, deriving its
configuration from its own directory name. Four copies to update is the price of
four repositories that cannot contaminate each other.

## What would make us revisit this

If cross-repository linking became a frequent need rather than an occasional
one, the separation would be fighting the content rather than protecting it.
Frequent restating is a signal that the boundary sits in the wrong place.
