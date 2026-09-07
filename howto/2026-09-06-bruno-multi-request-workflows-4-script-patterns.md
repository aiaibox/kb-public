---
id: 01M1V4611SW4R6TDMYTBK8RSFB
title: "Bruno multi-request workflows: 4 script patterns"
repo: public
tags: [qa, reference, runbook, import]
created: 2026-09-06
updated: 2026-09-07
source: claude-export-2026-09-06
---

# Bruno multi-request workflows: 4 script patterns

**Source:** Claude — https://claude.ai/chat/4ac041f2-cdf3-4876-be7d-06a239cf7681
**Exported:** 2026-09-06T05:33:24.783Z
**Turns:** 2

**Scope:** Covers chaining, looping and conditional ordering of multiple requests in Bruno via scripts and CLI; does not cover assertion syntax, environment setup, or any specific API suite.

## Conclusion

Pick the pattern by workflow shape. (1) Fixed sequence: put the requests in one folder — execution order is the seq field in each request's meta block (the drag order in the UI). In each request's post-response script store values with bru.setVar("authToken", res.body.token) and bru.setVar("userId", res.body.user.id); later requests read them via {{authToken}} / {{userId}} or bru.getVar("userId") in a pre-request script. Run the whole chain with the folder's Run button. bru.setVar() creates runtime variables that vanish after the run; bru.setEnvVar() persists into the environment. (2) Script-driven calls: const login = await bru.runRequest("auth/login"); — path is relative to the collection root, response exposes .status and .body, e.g. if (login.status === 200) { bru.setVar("authToken", login.body.token); }. Loop example: for (const id of ["ns-a","ns-b","ns-c"]) { bru.setVar("nsId", id); const r = await bru.runRequest("k8s/get-namespace"); }. For arbitrary external HTTP or custom headers/timeouts use bru.sendRequest({method, url, headers, data}, cb). (3) Conditional flow: in a post-response script call bru.runner.setNextRequest("Cleanup") — it takes the request NAME, not its path — or bru.runner.stopExecution() to abort the run; these only take effect during Runner/CLI runs, not single-request sends. (4) CI: install @usebruno/cli and run bru run <folder> --env <env>; it emits JUnit and HTML reports for the e2e pipeline.

## Verify

```
npm install -g @usebruno/cli && bru run <folder> --env <env> — expect a per-request pass/fail summary plus JUnit/HTML report output
Add a post-response script bru.setVar("authToken", res.body.token) to a login request, reference {{authToken}} in the next request's header, and confirm that request returns 200 during a folder run
Add await bru.runRequest("auth/login") in a pre-request script and confirm the dependent request resolves the stored variable
In a Runner run, make a post-response script call bru.runner.setNextRequest() on failure and confirm execution jumps to the named request; confirm it has no effect when sending the request individually
```

## Facts

- Request execution order inside a folder run is the seq field in the request's meta block, which is the drag order shown in the UI
- bru.setVar() stores runtime variables that do not survive past the run; bru.setEnvVar() writes into the environment
- bru.runRequest() takes a path relative to the collection root and returns an object exposing .status and .body
- bru.runRequest() must NOT be used in collection-level scripts: the collection script runs for every request, causing infinite recursion
- bru.runner.setNextRequest() takes the request name, not its path, and only takes effect during Runner/CLI runs; bru.runner.stopExecution() aborts the whole run
- bru run <folder> --env <env> outputs JUnit and HTML reports

## Open

- User's actual call chain was not provided, so no concrete script was written for their case
- Which pattern fits depends on whether the user needs fixed order + assertions (option 1 + CLI), loops/dynamic requests (option 2), or failure branching (option 3) — not yet confirmed

## References

- https://docs.usebruno.com/ — Bruno documentation — scripting APIs bru.runRequest, bru.sendRequest, bru.runner.setNextRequest (cited in the answer's search results as 'Bruno Docs')
- https://github.com/usebruno/bruno — Bruno repository, canonical home of the tool
- https://www.npmjs.com/package/@usebruno/cli — CLI package used for bru run <folder> --env <env> in CI

---

*Distilled from a 2-turn Claude conversation by glm-5.3-flash. The transcript was not retained; the source URL above is the only route back to it.*
