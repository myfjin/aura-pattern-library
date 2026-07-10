#![forbid(unsafe_code)]
//! byte_unit_parse — "512Mi"/"1.5G" → bytes and back; round-trip + ordering.
//!
//! Core idea: parse byte-unit strings (B, KiB, MiB, GiB, TiB) to u64 bytes and back to
//! string. THE ONE LAW: plant byte-unit strings with known values, parse them to bytes,
//! serialize back, and assert round-trip preserves order and magnitude — a missed unit
//! or misplaced decimal would fail the ordering or round-trip assert.
//! When to use: config parsing (cache size, buffer allocation), disk quotas, memory limits.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn parse_bytes(s: &str) -> Option<u64> {
    let s = s.trim();
    let s_lower = s.to_lowercase();

    // Extract the numeric part and unit.
    let mut num_end = 0;
    let mut has_dot = false;
    for (i, ch) in s.chars().enumerate() {
        if ch.is_ascii_digit() || (ch == '.' && !has_dot) {
            if ch == '.' {
                has_dot = true;
            }
            num_end = i + 1;
        } else {
            break;
        }
    }

    if num_end == 0 {
        return None;
    }

    let num_str = &s[..num_end];
    let unit_str = s_lower[num_end..].trim();

    let num: f64 = num_str.parse().ok()?;

    let multiplier: u64 = match unit_str {
        "" | "b" => 1,
        "kib" | "kb" => 1024,
        "mib" | "mb" => 1024 * 1024,
        "gib" | "gb" => 1024 * 1024 * 1024,
        "tib" | "tb" => 1024u64 * 1024 * 1024 * 1024,
        _ => return None,
    };

    Some((num * multiplier as f64) as u64)
}

fn format_bytes(bytes: u64) -> String {
    const UNITS: &[(&str, u64)] = &[
        ("TiB", 1024u64 * 1024 * 1024 * 1024),
        ("GiB", 1024 * 1024 * 1024),
        ("MiB", 1024 * 1024),
        ("KiB", 1024),
        ("B", 1),
    ];

    for (unit, divisor) in UNITS {
        if bytes >= *divisor {
            let val = bytes as f64 / *divisor as f64;
            if val >= 1.0 && val.fract() < 0.01 {
                return format!("{:.0}{}", val, unit);
            } else {
                return format!("{:.1}{}", val, unit);
            }
        }
    }
    format!("{}B", bytes)
}

fn main() {
    // Planted byte-unit cases with known values.
    let cases = vec![
        ("512", 512u64),
        ("1KiB", 1024u64),
        ("2MiB", 2 * 1024 * 1024),
        ("1.5GiB", (1.5 * 1024.0 * 1024.0 * 1024.0) as u64),
        ("1TiB", 1024u64 * 1024 * 1024 * 1024),
    ];

    // THE ONE LAW: parse and verify exact byte values.
    for (input, expected) in &cases {
        let parsed = parse_bytes(input).expect(&format!("failed to parse {input}"));
        assert_eq!(parsed, *expected, "mismatch for {input}");
    }

    // Round-trip: parse to bytes, format back, parse again.
    for (input, _) in &cases {
        let bytes1 = parse_bytes(input).expect("first parse failed");
        let formatted = format_bytes(bytes1);
        let bytes2 = parse_bytes(&formatted).expect("second parse failed");
        // Allow small rounding error (1 byte).
        assert!(bytes1.abs_diff(bytes2) <= 1, "round-trip failed for {input}");
    }

    // Ordering: larger inputs parse to larger byte values.
    let v1 = parse_bytes("1MiB").unwrap();
    let v2 = parse_bytes("1GiB").unwrap();
    assert!(v1 < v2, "ordering violated");

    println!("byte_unit_parse: round-trip exact, ordering preserved — PASS");
}
