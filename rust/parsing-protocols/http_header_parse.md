# http header parse

**Language:** Rust · **Sphere:** rust · **Category:** parsing-protocols

**Signature:** `(block: &str) → ?`

## What it does

http_header_parse — header block parse + case-insensitive lookup; folding handled.

Core idea: parse HTTP header lines, store them, and allow case-insensitive lookup.
Handle folding (continuation lines starting with space/tab). THE ONE LAW: plant a header
block with multi-line folded headers and duplicate header names, parse it, then assert
lookups return exact values and folding is handled — a naive split would lose folded lines.
When to use: HTTP client/server, header parsing in proxies.

## Guarantee

When it runs, http header parse guarantees assert_eq!(headers.get("Content-Type"), Some("text/html"), "Content-Type lookup failed"); assert_eq!(headers.get("content-type"), Some("text/html"), "lowercase lookup failed"); assert_eq!(headers.get("CONTENT-TYPE"), Some("text/html"), "uppercase lookup failed") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(headers.get("Content-Type"), Some("text/html"), "Content-Type lookup failed")`
- `assert_eq!(headers.get("content-type"), Some("text/html"), "lowercase lookup failed")`
- `assert_eq!(headers.get("CONTENT-TYPE"), Some("text/html"), "uppercase lookup failed")`
- `assert_eq!(headers.get("Content-Length"), Some("1234"), "Content-Length lookup failed")`
- `assert_eq!(headers.get("Authorization"), Some("Bearer token123"), "Authorization lookup failed")`
- `assert_eq!(headers.get("X-Custom-Header"), None)`
- `assert!(accept.contains("text/html"), "folded header lost")`
- `assert!(accept.contains("application/json"), "folded continuation lost")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
