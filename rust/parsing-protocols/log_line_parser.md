# log line parser

**Language:** Rust · **Sphere:** rust · **Category:** parsing-protocols

**Signature:** `(line: &str) → Option<LogLine<'_>>`

## What it does

log_line_parser — zero-copy syslog parse via byte scan.

Core idea: scan a line of bytes once to extract timestamp, hostname, service, and
message without allocation. THE ONE LAW: plant a mixed set of well-formed and malformed
syslog lines (with missing fields, non-RFC timestamps), then assert exact field counts
and mismatches are caught — a naive split on spaces would fail on multi-word messages.
When to use: high-throughput log ingestion where allocation is a bottleneck.

## Guarantee

When it runs, log line parser guarantees assert_eq!(parsed_count, 3, "missed well-formed logs") (proven by rustc-run).

**Checkable constraints:**

- `assert!(!entry.timestamp.is_empty())`
- `assert!(!entry.hostname.is_empty())`
- `assert!(!entry.service.is_empty())`
- `assert!(!entry.message.is_empty())`
- `assert_eq!(parsed_count, 3, "missed well-formed logs")`
- `assert!(parse_syslog(log).is_none(), "malformed log should fail: {log}")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
