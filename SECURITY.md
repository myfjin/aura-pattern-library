# Security policy

The crew maintaining aura-pattern-library is small — one human and five machines — and we take security reports seriously. This file says how to reach us privately, what we treat as in scope, and what you can expect back.

---

## Reporting a vulnerability

**Email:** [ihladkyi2@gmail.com](mailto:ihladkyi2@gmail.com)

**Please do not open a public GitHub issue for a suspected security problem.** GitHub issues are visible to everyone from the moment they are filed; a real vulnerability filed there is a disclosure, not a report. Email us first.

Include as much of the following as you have:

- what you saw, and what you expected instead
- how to reproduce it — the minimum sequence of steps or the smallest input
- which version or commit hash you were looking at
- your assessment of the impact, if you have one
- whether you would like to be credited (and how), or would prefer anonymity

If you cannot reproduce it yet but believe something is wrong, say so and share what you have. We would rather look at a real hunch than wait for a perfect writeup.

---

## What we will do

We are a small crew without a paid on-call rotation, so timing is best-effort — but honest:

- **Acknowledgement** within **7 days** of your email. If you have not heard from us in that window, please assume the email did not arrive and try again.
- **A first assessment** within **30 days** — whether we confirm the issue, cannot reproduce it, or need more information.
- **Coordinated disclosure**. If the report is confirmed, we agree with you on a disclosure timeline. Our default is up to **90 days** from confirmation, extended if a fix is genuinely in flight.
- **Credit** on the release notes and in the commit message, in the form you asked for. If you asked for anonymity, we honor that.

We will not sue researchers acting in good faith. We do not run a bounty program.

---

## Scope

**In scope:** anything that undermines the library's one claim — *"this is what it claims"*.

- **Signature forgery or bypass** — anything that gets a file past `library_verify.py` while mis-stated or tampered with. The signature system is the entry criterion.
- **Watermark removal, forgery, or confusion** — the visible mark + invisible channels are the attribution surface. An exploit that removes a mark undetectably, or stamps a non-crew mark that `library_verify.py` would accept, is in scope.
- **Catalog or index misreporting** — code paths that would cause `build_patterns_index.py`, `CATALOG.md` generation, or `library_audit.py` to report a count or classification that does not match disk truth.
- **Compromise of `aura-signing.pub`** — if you can construct a plausible exchange that would get our public key replaced, that is in scope.
- **A pattern that executes beyond its documented scope** — a self-test that reaches the network, writes outside its temp dir, or escapes the sandbox the gate expects. The library ships `main()`/`stopifnot`/self-test code to be *run*; the contract is that it stays within its stated scope.
- Vulnerabilities in `library_verify.py`, `library_audit.py`, `build_patterns_index.py`, `harvest_gate.py`, `ingest*.py` — the tooling that produces the signed claim.

**Out of scope:**

- Third-party dependencies. Report those to their upstream projects; we will pick up the fix on their release.
- Vulnerabilities that require an already-compromised environment (root on the host, control of the process, physical access to the signing key).
- Denial-of-service via absurd resource limits (e.g. a 10 GB fake pattern tree). Deployment limits are a deployment concern.
- Missing "security headers" in code paths that never serve HTTP.
- Automated scanner findings without a demonstrated exploit path — please attach the reproduction, not just the scanner name.
- Vulnerabilities in the folder-nature or aura-brain repositories — report those to their respective `SECURITY.md` channels (same email, different scope).

---

## Secrets and private data — how we handle them

This repository is a **curated public export** of a larger private working tree. That private tree contains harvest workspaces, pending candidates, the Ed25519 signing private key, and crew infrastructure that is intentionally not published. The following classes of file are never included in a release; if you ever see one land in a public commit, tell us — that is itself a security bug:

- any Ed25519 **private** signing material (the `.pub` is intended; a `.priv` or raw secret is not)
- harvest workspace sessions, diaries, or gate scratch (`~/ai-lab/patterns_*/`)
- pending-tree salvage with explanatory notes (`~/aura-pattern-library-pending/`)
- any credentials, tokens, environment files, or pairing/authorization files — in any form, from any tool
- internal hostnames, LAN IPs, or Tailnet addresses used by the crew's infrastructure

The library's `aura-signing.pub` is the only key material that ships. If you need to verify a copy of the tree yourself, use that public key with `folder-nature verify . --root --pubkey aura-signing.pub` or `python3 library_verify.py`.

---

## PGP

We do not currently publish a PGP key. Plain email to `ihladkyi2@gmail.com` is the reporting channel. If your report is sensitive enough that transport encryption matters, mention it in the first mail and we will coordinate a secure channel before you send details.

---

## Thank you

Reporters who take the time to write us privately are doing us a favor, and we know it. The crew is small; the ledger is honest; the door is open. 🖖
