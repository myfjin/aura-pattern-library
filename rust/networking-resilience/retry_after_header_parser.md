# retry after header parser

**Language:** Rust · **Sphere:** rust · **Category:** networking-resilience

**Signature:** `(y: i64, m: i64, d: i64) → i64`

## What it does

Retry-After (RFC 7231 §7.1.3): either delta-seconds (an integer) OR an HTTP-date
(IMF-fixdate, e.g. "Mon, 01 Jan 2024 00:00:00 GMT"). Both resolve to "seconds to wait"
relative to a caller-supplied `now_epoch` (Unix seconds), computed deterministically:
- delta-seconds: the integer, verbatim.
- HTTP-date: parse to absolute epoch seconds, return date - now (saturating at 0 if past).
The HTTP-date branch is a REAL parser (month name → number, civil date → days-since-epoch
via Howard Hinnant's algorithm), not a hardcoded default.

## Guarantee

When it runs, retry after header parser guarantees assert_eq!(parse_retry_after("120", now).unwrap(), 120); assert_eq!(parse_retry_after("0", now).unwrap(), 0); assert_eq!(parse_retry_after("3600", now).unwrap(), 3600) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(parse_retry_after("120", now).unwrap(), 120)`
- `assert_eq!(parse_retry_after("0", now).unwrap(), 0)`
- `assert_eq!(parse_retry_after("3600", now).unwrap(), 3600)`
- `assert_eq!(parse_retry_after(" 120 ", now).unwrap(), 120, "whitespace trimmed")`
- `assert_eq!(parse_retry_after("Mon, 01 Jan 2024 00:00:00 GMT", now).unwrap(), 0, "date == now → wait 0")`
- `assert_eq!(parse_retry_after("Mon, 01 Jan 2024 01:00:00 GMT", now).unwrap(), 3600, "one hour ahead → 3600s")`
- `assert_eq!(parse_retry_after("Sun, 31 Dec 2023 23:00:00 GMT", now).unwrap(), 0, "past date → 0")`
- `assert_eq!(parse_http_date_epoch("Thu, 01 Jan 1970 00:00:00 GMT").unwrap(), 0, "epoch 0")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
