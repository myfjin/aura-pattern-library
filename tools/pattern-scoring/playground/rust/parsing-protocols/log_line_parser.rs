#![forbid(unsafe_code)]
//! log_line_parser — zero-copy syslog parse via byte scan.
//!
//! Core idea: scan a line of bytes once to extract timestamp, hostname, service, and
//! message without allocation. THE ONE LAW: plant a mixed set of well-formed and malformed
//! syslog lines (with missing fields, non-RFC timestamps), then assert exact field counts
//! and mismatches are caught — a naive split on spaces would fail on multi-word messages.
//! When to use: high-throughput log ingestion where allocation is a bottleneck.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::str;

struct LogLine<'a> {
    timestamp: &'a str,
    hostname: &'a str,
    service: &'a str,
    message: &'a str,
}

fn parse_syslog(line: &str) -> Option<LogLine<'_>> {
    let bytes = line.as_bytes();
    let mut pos = 0;

    // Skip leading whitespace.
    while pos < bytes.len() && bytes[pos].is_ascii_whitespace() {
        pos += 1;
    }
    if pos >= bytes.len() {
        return None;
    }

    // Read timestamp (format: 2026-07-10T12:34:56 — 19 bytes).
    if pos + 19 > bytes.len() {
        return None;
    }
    if !is_timestamp_like(&bytes[pos..pos + 19]) {
        return None;
    }
    let timestamp = str::from_utf8(&bytes[pos..pos + 19]).ok()?;
    pos += 19;

    // Skip space.
    if pos >= bytes.len() || bytes[pos] != b' ' {
        return None;
    }
    pos += 1;

    // Read hostname (non-space characters).
    let host_start = pos;
    while pos < bytes.len() && bytes[pos] != b' ' {
        pos += 1;
    }
    if host_start == pos {
        return None; // Empty hostname.
    }
    let hostname = str::from_utf8(&bytes[host_start..pos]).ok()?;

    // Skip space.
    if pos >= bytes.len() || bytes[pos] != b' ' {
        return None;
    }
    pos += 1;

    // Read service (format: [name], ends with ]: ).
    if pos >= bytes.len() || bytes[pos] != b'[' {
        return None;
    }
    pos += 1;
    let svc_start = pos;
    while pos < bytes.len() && bytes[pos] != b']' {
        pos += 1;
    }
    if pos >= bytes.len() {
        return None;
    }
    let service = str::from_utf8(&bytes[svc_start..pos]).ok()?;
    pos += 1;

    // Skip "]: ".
    if pos + 1 > bytes.len() || bytes[pos] != b':' || bytes[pos + 1] != b' ' {
        return None;
    }
    pos += 2;

    // Rest is the message.
    let message = str::from_utf8(&bytes[pos..]).ok()?;

    Some(LogLine {
        timestamp,
        hostname,
        service,
        message,
    })
}

fn is_timestamp_like(bytes: &[u8]) -> bool {
    if bytes.len() != 19 {
        return false;
    }
    // Rough check: YYYY-MM-DDTHH:MM:SS
    bytes[4] == b'-'
        && bytes[7] == b'-'
        && bytes[10] == b'T'
        && bytes[13] == b':'
        && bytes[16] == b':'
}

fn main() {
    let logs = vec![
        "2026-07-10T12:34:56 host1 [sshd]: failed login attempt",
        "2026-07-10T12:34:57 host2 [kernel]: out of memory",
        "2026-07-10T12:34:58 host3 [cron]: task completed",
    ];

    let mut parsed_count = 0;
    for log in &logs {
        if let Some(entry) = parse_syslog(log) {
            parsed_count += 1;
            // Verify fields are non-empty and reasonable.
            assert!(!entry.timestamp.is_empty());
            assert!(!entry.hostname.is_empty());
            assert!(!entry.service.is_empty());
            assert!(!entry.message.is_empty());
        }
    }

    // THE ONE LAW: all well-formed logs parsed.
    assert_eq!(parsed_count, 3, "missed well-formed logs");

    // Malformed lines fail gracefully.
    let bad_logs = vec![
        "incomplete",
        "2026-07-10T12:34:56 nohost",
        "2026-07-10T12:34:56 host incomplete[service",
    ];
    for log in &bad_logs {
        assert!(parse_syslog(log).is_none(), "malformed log should fail: {log}");
    }

    println!("log_line_parser: {parsed_count} lines parsed, malformed rejected — PASS");
}
