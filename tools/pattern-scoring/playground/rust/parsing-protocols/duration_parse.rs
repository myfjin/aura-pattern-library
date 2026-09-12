#![forbid(unsafe_code)]
//! duration_parse — "1h30m"/"250ms" → total; round-trip + arithmetic.
//!
//! Core idea: parse duration strings (1h, 30m, 250ms, etc.) to total milliseconds,
//! serialize back, and verify arithmetic. THE ONE LAW: plant duration strings with
//! known totals, parse them, serialize back, then assert round-trip and arithmetic are
//! exact — a missed unit or decimal error would fail the total or arithmetic asserts.
//! When to use: timeout config, sleep durations, rate-limiting intervals.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn parse_duration_ms(s: &str) -> Option<u64> {
    let s = s.trim();
    let mut total_ms: u64 = 0;
    let mut current_num = String::new();
    let mut i = 0;
    let chars: Vec<char> = s.chars().collect();

    while i < chars.len() {
        let ch = chars[i];
        if ch.is_ascii_digit() || ch == '.' {
            current_num.push(ch);
            i += 1;
        } else if ch.is_ascii_alphabetic() {
            if current_num.is_empty() {
                return None;
            }
            let num: f64 = current_num.parse().ok()?;

            // Try to parse multi-character units (ms)
            let unit = if i + 1 < chars.len() && ch == 'm' && chars[i + 1] == 's' {
                i += 1; // Skip the 's' in 'ms'
                "ms".to_string()
            } else {
                ch.to_lowercase().to_string()
            };

            let ms = match unit.as_str() {
                "d" => (num * 24.0 * 60.0 * 60.0 * 1000.0) as u64,
                "h" => (num * 60.0 * 60.0 * 1000.0) as u64,
                "m" => (num * 60.0 * 1000.0) as u64,
                "s" => (num * 1000.0) as u64,
                "ms" => num as u64,
                _ => return None,
            };
            total_ms += ms;
            current_num.clear();
            i += 1;
        } else if !ch.is_whitespace() {
            return None;
        } else {
            i += 1;
        }
    }

    if !current_num.is_empty() {
        return None; // Trailing number without unit.
    }

    Some(total_ms)
}

fn format_duration_ms(ms: u64) -> String {
    let mut remaining = ms;
    let mut parts = Vec::new();

    let days = remaining / (24 * 60 * 60 * 1000);
    remaining %= 24 * 60 * 60 * 1000;
    if days > 0 {
        parts.push(format!("{}d", days));
    }

    let hours = remaining / (60 * 60 * 1000);
    remaining %= 60 * 60 * 1000;
    if hours > 0 {
        parts.push(format!("{}h", hours));
    }

    let minutes = remaining / (60 * 1000);
    remaining %= 60 * 1000;
    if minutes > 0 {
        parts.push(format!("{}m", minutes));
    }

    let seconds = remaining / 1000;
    remaining %= 1000;
    if seconds > 0 {
        parts.push(format!("{}s", seconds));
    }

    if remaining > 0 {
        parts.push(format!("{}ms", remaining));
    }

    if parts.is_empty() {
        return "0ms".to_string();
    }
    parts.join("")
}

fn main() {
    // Planted duration cases with known millisecond totals.
    let cases = vec![
        ("1s", 1000),
        ("1m", 60 * 1000),
        ("1h", 60 * 60 * 1000),
        ("1h30m", 90 * 60 * 1000),
        ("250ms", 250),
        ("2h15m30s", (2 * 60 * 60 + 15 * 60 + 30) * 1000),
    ];

    // THE ONE LAW: parse and verify exact millisecond totals.
    for (input, expected_ms) in &cases {
        let parsed = parse_duration_ms(input).expect(&format!("failed to parse {input}"));
        assert_eq!(parsed, *expected_ms, "mismatch for {input}");
    }

    // Round-trip: parse to ms, format back, parse again.
    for (input, _) in &cases {
        let ms1 = parse_duration_ms(input).expect("first parse failed");
        let formatted = format_duration_ms(ms1);
        let ms2 = parse_duration_ms(&formatted).expect("second parse failed");
        assert_eq!(ms1, ms2, "round-trip failed for {input}");
    }

    // Arithmetic: 1h + 30m + 30s = 1h30m30s.
    let h = parse_duration_ms("1h").unwrap();
    let m = parse_duration_ms("30m").unwrap();
    let s = parse_duration_ms("30s").unwrap();
    let sum = h + m + s;
    let expected = parse_duration_ms("1h30m30s").unwrap();
    assert_eq!(sum, expected, "arithmetic failed");

    println!("duration_parse: round-trip exact, arithmetic verified — PASS");
}
