# Contributing to aura-pattern-library

The crew is small — one human and five machines — and this project is what it is because of that. We would rather grow it slowly with people who care about substance than fast with people who don't.

If you found this and it interests you, you are welcome. This file is what we ask before you send code, and what we ask about ourselves before we merge it.

---

## How we take contributions

We take **pull requests** on GitHub. We do not use a CLA. Sign-off on every commit is the entire contributor agreement:

    git commit -s -m "your message"

The `-s` adds a `Signed-off-by:` line and asserts the **Developer Certificate of Origin (DCO)** — that you wrote the change or have the right to submit it under Apache-2.0. That is all we require.

If you have an idea larger than one PR, **open an issue first** and talk it through with us. Small fixes and typos can skip that step; anything that changes how a pattern is signed, verified, or classified should be discussed before you write it.

**When you open an issue, please describe what you saw and how to recreate it.** A clear reproduction is the difference between something we can act on and something that has to sit until someone can guess. If you cannot reproduce it yet — say so, and share what you have.

---

## The rules that were paid for

Each rule below was learned from a specific afternoon where we got it wrong first. We do not ask you to follow them because they are elegant. We ask because we already broke each one and would rather not do it again.

### Measurement

- **Nothing at n=1 is a measurement.** Report the **median of ≥3 runs plus the call count**, or **fail-once as a rate over N≥10**.
- **A number you cannot trace to exactly one run is not a measurement.** Attribute every figure.
- **Read the newest state, never the oldest record.** Freshness before neatness. For pattern counts, re-count from disk via `build_patterns_index.py`; never quote from memory or the old CATALOG header.
- **Make a checker fail once before you trust it.** A green that has never been red is a green you have not tested. `library_verify.py` without a known-RED counterexample proves nothing.

### Honesty

- **Say "unknown" when you do not know.** Absence of a visible cause is not evidence — "unknown" beats invented history every time.
- **Retract in public.** If a number you published turns out to be wrong, correct it in the same visible place. Silent edits are worse than the original error.
- **No self-scored superiority.** The person who wrote the code does not grade it. Independence between author, caller and grader is the whole point of the design. A pattern's self-test is the oracle of record — the author of the pattern does not get to overrule it.

### Files, hashes, signatures

- **Edit → re-sign → verify. Every time.** Every edit changes the sha, the sha is signed. An edit to a file inside a signed subtree without a matching re-sign leaves the tree RED. `library_verify.py` must print GREEN before any commit touches a signed subtree. Root-level files (README, CATALOG, PATTERNS_INDEX, `*.py` helpers, `tools/`) are not signed and can be edited freely.
- **Never edit, move, or re-stamp the watermark block.** It is set once at ingest and never again. Re-stamping is how you corrupt a mark that was fine.
- **The description slot is language-specific** and finicky — a description in the wrong slot is invisible to the ruler and the pattern reads as "no description." See [`.claude/skills/library-operations/SKILL.md`](https://github.com/myfjin) for the per-language rule.

### Fixes, reverts, proofs

- **Prove-by-revert only inside `mktemp -d`, never on the live tree.** Reverting on the signed tree leaves it RED; the next verifier run reports the revert, not the fix.
- **Quiesce before you verify.** A verification that races with a live ingester is a verification of the race, not the fix.

### Failure modes

- **Fail open with a loud `WARN`.** Silent fail-closed is invisible; silent fail-open is a lie. Loud fail-open is the honest shape. A missing toolchain (no `rustc`, no `go`) is a LOUD per-language SKIP that turns the gate RED — never silently green.

---

## Testing & verification

Run the library's own gate before opening a PR. If your change touches:

- **a pattern file** (anything inside `python/`, `cpp/`, `rust/`, `go/`, `javascript/`, `r/`) — re-sign the touched subtree, then `python3 library_verify.py` to GREEN. Batch by sphere and verify after each sphere, not once at the end — a RED tells you far more when it names one subtree.
- **the catalog or index** — regenerate via `python3 build_patterns_index.py`; descriptions come from the files themselves, so the generator cannot drift.
- **a verification tool itself** (`library_verify.py`, `library_audit.py`) — include a known-RED counterexample in the test so the tool is proven to actually detect what it claims to.

Adding patterns goes through the **ingest flow** (`ingest.py`, `ingest_cpp_native.py`, `ingest_go.py`), not raw commits. Ingest stamps the watermark, signs the subtree, and updates CATALOG in one atomic operation.

---

## What we will not take

- **Backwards-compatibility shims** for hypothetical futures. If you can change the code, change the code.
- **Error handling for scenarios that cannot happen.** Trust internal contracts and framework guarantees; validate at boundaries only.
- **Comments that describe what the code does.** Well-named identifiers do that. Comments are for the *why* that is not obvious from the *what*.
- **Documentation that references issue numbers, callers, or the current sprint.** That belongs in the PR description. Code outlives PRs.
- **New abstractions ahead of use.** Three similar lines are better than a premature abstraction; wait for the fourth.
- **Patterns without a self-test.** A pattern that cannot grade itself does not belong here.
- **Fixtures that bake in a seed, platform, or environment detail.** Determinism must be stated and enforced, not stumbled into.

None of the above is aesthetic preference — each is a rule we broke first and paid for.

---

## Register

We work as brothers and friends, not as vendors and customers. Feedback is direct; corrections are welcome from any seat. If a machine reviewer catches something a human missed, that is the design working, not a failure of hierarchy.

If your first PR is small — a typo, a missing comma, a description fix — that is a good first PR. Some of ours are the same.

---

## Contact

For anything that does not fit an issue: **ihladkyi2@gmail.com**.

🖖
