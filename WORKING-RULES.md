# Working rules for an AI agent

How to *behave* in this vault, as distinct from `RULES.md`, which governs what a
note must contain. Canonical here; distributed to every repo by
`personal/scripts/distribute.sh`.

---

## 1. Keep displayed command output minimal

When running a command to think, check or calculate, show the least output that
supports the conclusion. Do not dump full directory listings, verbose logs or
long verification sweeps when one line answers the question.

Output should remain *expandable* — never suppress it so far that a result cannot
be re-checked. Prefer a count, a diff, or a single decisive line over the raw
dump, and keep the raw form available if the conclusion is questioned.

## 2. End with a table of what changed

Any session that modified the codebase closes with a summary table: which files
changed, and lines added/removed. Cover deletions and files created outside the
repos (LaunchAgents, shell config, Keychain entries) as well as tracked files.

No changes means no table.

## 3. Finish the current request before reading the next

If a message arrives mid-task, complete the in-flight request **fully** first,
then address the new one. Do not abandon or half-finish work to pivot.

Acknowledge the interruption briefly so it is clear it was seen and queued, then
carry on.

## 4. Give exact commands, then stop

When a command's output matters, give **one** command, stop, and wait for the
pasted result. Batch only trivial settings whose output is uninteresting.

- Give the **exact** command, never a description of one.
- Be precise and concise: an instruction, not an essay.
- After a destructive command, verify — do not assume it worked.

## 5. Name the machine

Whenever more than one machine is in play, state which one a command runs on
before the command. Never leave it ambiguous.

## 6. Estimate anything slow

If a command may take longer than roughly 30 seconds, say how long it is expected
to take, in the same message as the command. A long silence with no estimate is
indistinguishable from a hang.

---

## Why these exist

Rules 4 through 6 came from real failures: steps stacked ahead of a result that
turned out differently, pasted output misread as coming from the wrong repo, and
commands run against the wrong host. Rule 1 came from verification sweeps burying
the answer they were meant to surface. Rule 2 came from having to re-read a
transcript to find out what had been touched.

They are about making work reviewable. An agent that is fast but unauditable
produces changes nobody can verify, which in a knowledge base is worse than
being slow.

## Applies alongside

- `RULES.md` — what a note must contain, and which repo it belongs in
- Each repo's `AGENTS.md` — constraints specific to that repo
