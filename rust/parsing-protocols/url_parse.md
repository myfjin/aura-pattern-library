# url parse

**Language:** Rust · **Sphere:** rust · **Category:** parsing-protocols

**Signature:** `(url: &str) → Option<URL<'_>>`

## What it does

url_parse — scheme/host/port/path/query split; planted URLs decomposed.

Core idea: parse a URL into components without regex or external parsing. THE ONE LAW:
plant a set of well-formed and edge-case URLs, parse them, and assert each component
matches the expected value — a naive split on / or : would fail on ports or queries.
When to use: proxy rules, request routing, URL canonicalization.

## Guarantee

When it runs, url parse guarantees assert_eq!(parsed.scheme, *exp_scheme, "scheme mismatch in {url_str}"); assert_eq!(parsed.host, *exp_host, "host mismatch in {url_str}"); assert_eq!(parsed.port, *exp_port, "port mismatch in {url_str}") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(parsed.scheme, *exp_scheme, "scheme mismatch in {url_str}")`
- `assert_eq!(parsed.host, *exp_host, "host mismatch in {url_str}")`
- `assert_eq!(parsed.port, *exp_port, "port mismatch in {url_str}")`
- `assert_eq!(parsed.path, *exp_path, "path mismatch in {url_str}")`
- `assert_eq!(parsed.query, *exp_query, "query mismatch in {url_str}")`
- `assert!(parse_url("not-a-url").is_none())`
- `assert!(parse_url("https://no-path-no-scheme.com:invalid-port/").is_none())`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
