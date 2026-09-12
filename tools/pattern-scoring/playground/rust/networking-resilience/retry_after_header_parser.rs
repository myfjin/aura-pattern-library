#![forbid(unsafe_code)]

// Retry-After (RFC 7231 §7.1.3): either delta-seconds (an integer) OR an HTTP-date
// (IMF-fixdate, e.g. "Mon, 01 Jan 2024 00:00:00 GMT"). Both resolve to "seconds to wait"
// relative to a caller-supplied `now_epoch` (Unix seconds), computed deterministically:
//   - delta-seconds: the integer, verbatim.
//   - HTTP-date: parse to absolute epoch seconds, return date - now (saturating at 0 if past).
// The HTTP-date branch is a REAL parser (month name → number, civil date → days-since-epoch
// via Howard Hinnant's algorithm), not a hardcoded default.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn days_from_civil(y: i64, m: i64, d: i64) -> i64 {
    // Days from 1970-01-01 (may be negative). Valid for the proleptic Gregorian calendar.
    let y = if m <= 2 { y - 1 } else { y };
    let era = if y >= 0 { y } else { y - 399 } / 400;
    let yoe = y - era * 400; // [0, 399]
    let mp = (m + 9) % 12; // Mar=0 .. Feb=11
    let doy = (153 * mp + 2) / 5 + d - 1; // [0, 365]
    let doe = yoe * 365 + yoe / 4 - yoe / 100 + doy; // [0, 146096]
    era * 146097 + doe - 719468
}

fn month_num(name: &str) -> Option<i64> {
    match name {
        "Jan" => Some(1), "Feb" => Some(2), "Mar" => Some(3), "Apr" => Some(4),
        "May" => Some(5), "Jun" => Some(6), "Jul" => Some(7), "Aug" => Some(8),
        "Sep" => Some(9), "Oct" => Some(10), "Nov" => Some(11), "Dec" => Some(12),
        _ => None,
    }
}

fn parse_http_date_epoch(value: &str) -> Result<i64, &'static str> {
    // IMF-fixdate: "Wdy, DD Mon YYYY HH:MM:SS GMT"
    let v = value.trim();
    if !v.ends_with(" GMT") {
        return Err("HTTP-date must end with GMT");
    }
    let comma = v.find(", ").ok_or("HTTP-date missing day-of-week comma")?;
    let rest = &v[comma + 2..v.len() - 4]; // strip "Wdy, " and trailing " GMT"
    let parts: Vec<&str> = rest.split(' ').collect();
    if parts.len() != 4 {
        return Err("HTTP-date wrong field count");
    }
    let day: i64 = parts[0].parse().map_err(|_| "bad day")?;
    let month = month_num(parts[1]).ok_or("bad month")?;
    let year: i64 = parts[2].parse().map_err(|_| "bad year")?;
    let hms: Vec<&str> = parts[3].split(':').collect();
    if hms.len() != 3 {
        return Err("bad time");
    }
    let hh: i64 = hms[0].parse().map_err(|_| "bad hour")?;
    let mm: i64 = hms[1].parse().map_err(|_| "bad minute")?;
    let ss: i64 = hms[2].parse().map_err(|_| "bad second")?;
    if !(1..=31).contains(&day) || hh > 23 || mm > 59 || ss > 60 {
        return Err("HTTP-date field out of range");
    }
    let days = days_from_civil(year, month, day);
    Ok(days * 86400 + hh * 3600 + mm * 60 + ss)
}

fn parse_retry_after(value: &str, now_epoch: i64) -> Result<u64, &'static str> {
    // delta-seconds first (an all-digit integer).
    let trimmed = value.trim();
    if !trimmed.is_empty() && trimmed.bytes().all(|b| b.is_ascii_digit()) {
        return trimmed.parse::<u64>().map_err(|_| "delta-seconds overflow");
    }
    // Otherwise it must be an HTTP-date.
    let epoch = parse_http_date_epoch(trimmed)?;
    Ok((epoch - now_epoch).max(0) as u64)
}

fn main() {
    // Reference "now" = 2024-01-01 00:00:00 GMT = 1704067200 (hand-checkable Unix time).
    let now = 1_704_067_200i64;

    // Test 1: delta-seconds ignore `now` and return verbatim.
    assert_eq!(parse_retry_after("120", now).unwrap(), 120);
    assert_eq!(parse_retry_after("0", now).unwrap(), 0);
    assert_eq!(parse_retry_after("3600", now).unwrap(), 3600);
    assert_eq!(parse_retry_after("  120  ", now).unwrap(), 120, "whitespace trimmed");

    // Test 2: the epoch of the reference date itself resolves to 0 seconds to wait.
    assert_eq!(
        parse_retry_after("Mon, 01 Jan 2024 00:00:00 GMT", now).unwrap(),
        0,
        "date == now → wait 0"
    );

    // Test 3: a date one hour ahead → exactly 3600 seconds (REAL date math, not a default).
    assert_eq!(
        parse_retry_after("Mon, 01 Jan 2024 01:00:00 GMT", now).unwrap(),
        3600,
        "one hour ahead → 3600s"
    );

    // Test 4: a date in the past → saturates to 0.
    assert_eq!(
        parse_retry_after("Sun, 31 Dec 2023 23:00:00 GMT", now).unwrap(),
        0,
        "past date → 0"
    );

    // Test 5: absolute-epoch known vector — the Unix epoch itself.
    assert_eq!(parse_http_date_epoch("Thu, 01 Jan 1970 00:00:00 GMT").unwrap(), 0, "epoch 0");
    assert_eq!(
        parse_http_date_epoch("Mon, 01 Jan 2024 00:00:00 GMT").unwrap(),
        1_704_067_200,
        "2024-01-01 epoch"
    );

    // Test 6: reject garbage and malformed dates.
    assert!(parse_retry_after("not-a-number", now).is_err(), "reject garbage");
    assert!(parse_retry_after("123abc", now).is_err(), "reject mixed");
    assert!(parse_retry_after("", now).is_err(), "reject empty");
    assert!(parse_retry_after("12.34", now).is_err(), "reject float");
    assert!(parse_retry_after("-120", now).is_err(), "reject negative");
    assert!(parse_retry_after("Mon, 01 Foo 2024 00:00:00 GMT", now).is_err(), "reject bad month");
    assert!(parse_retry_after("Mon, 01 Jan 2024 00:00:00 UTC", now).is_err(), "reject non-GMT");

    println!("retry_after_header_parser: PASS");
}
