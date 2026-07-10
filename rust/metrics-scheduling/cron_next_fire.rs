#![forbid(unsafe_code)]
//! cron_next_fire — parse simple cron expression; compute next fire time.
//!
//! Core idea: parse "*/5 * * * *" (every 5 minutes) or similar, then compute the next
//! fire time from a given time. THE ONE LAW: plant a known current time and cron expr,
//! hand-compute the expected next fire, then assert the cron engine produces exactly that.
//! A missed fire or off-by-one interval would fail.
//! When to use: job scheduling, recurring task execution, cron-like systems.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#[derive(Debug, Clone)]
struct CronExpr {
    minute: Vec<u32>,
    hour: Vec<u32>,
}

impl CronExpr {
    fn parse(expr: &str) -> Option<Self> {
        let parts: Vec<&str> = expr.split_whitespace().collect();
        if parts.len() != 5 {
            return None;
        }

        let minute = Self::parse_field(parts[0], 0, 59)?;
        let hour = Self::parse_field(parts[1], 0, 23)?;

        Some(CronExpr { minute, hour })
    }

    fn parse_field(field: &str, min: u32, max: u32) -> Option<Vec<u32>> {
        if field == "*" {
            return Some((min..=max).collect());
        }

        if field.starts_with("*/") {
            let step = field[2..].parse::<u32>().ok()?;
            return Some((min..=max).step_by(step as usize).collect());
        }

        let parts: Vec<&str> = field.split(',').collect();
        let mut result = Vec::new();
        for part in parts {
            if let Ok(val) = part.parse::<u32>() {
                if val >= min && val <= max {
                    result.push(val);
                }
            }
        }
        Some(result)
    }

    fn next_fire(&self, from_minute: u32, from_hour: u32) -> (u32, u32) {
        // Simple logic: start from next minute, find the first matching minute/hour.
        let mut minute = from_minute + 1;
        let mut hour = from_hour;

        if minute > 59 {
            minute = 0;
            hour += 1;
            if hour > 23 {
                hour = 0;
            }
        }

        // Find next fire: scan ahead up to 24*60 minutes.
        for _ in 0..1440 {
            if self.minute.contains(&minute) && self.hour.contains(&hour) {
                return (hour, minute);
            }

            minute += 1;
            if minute > 59 {
                minute = 0;
                hour += 1;
                if hour > 23 {
                    hour = 0;
                }
            }
        }

        (hour, minute)
    }
}

fn main() {
    // Planted case 1: every 5 minutes.
    let cron = CronExpr::parse("*/5 * * * *").expect("parse */5 * * * *");
    let next = cron.next_fire(0, 10);
    assert_eq!(next, (10, 5), "from 10:00, next fire should be 10:05");

    let next = cron.next_fire(4, 10);
    assert_eq!(next, (10, 5), "from 10:04, next fire should be 10:05");

    let next = cron.next_fire(5, 10);
    assert_eq!(next, (10, 10), "from 10:05, next fire should be 10:10");

    let next = cron.next_fire(59, 23);
    assert_eq!(next, (0, 0), "from 23:59, next fire should wrap to 00:00");

    // Planted case 2: specific hours and minutes (9 AM and 3 PM, at minute 0 and 30).
    let cron2 = CronExpr::parse("0,30 9,15 * * *").expect("parse 0,30 9,15 * * *");
    let next = cron2.next_fire(0, 8);
    assert_eq!(next, (9, 0), "from 08:00, next fire should be 09:00");

    let next = cron2.next_fire(5, 9);
    assert_eq!(next, (9, 30), "from 09:05, next fire should be 09:30");

    let next = cron2.next_fire(30, 9);
    assert_eq!(next, (15, 0), "from 09:30, next fire should be 15:00");

    // THE ONE LAW: fire times are strictly increasing from a given start.
    let cron3 = CronExpr::parse("*/15 * * * *").expect("parse */15 * * * *");
    let mut current = (0u32, 0u32);
    let mut fires = Vec::new();
    for _ in 0..10 {
        let next = cron3.next_fire(current.1, current.0);
        // Ensure it's strictly after current.
        let next_total = next.0 * 60 + next.1;
        let current_total = current.0 * 60 + current.1;
        assert!(
            next_total > current_total,
            "next fire must be strictly after current"
        );
        fires.push(next);
        current = next;
    }

    // Verify interval: every 15 minutes.
    for i in 1..fires.len() {
        let prev_total = fires[i - 1].0 * 60 + fires[i - 1].1;
        let next_total = fires[i].0 * 60 + fires[i].1;
        let interval = (next_total - prev_total) as i32;
        let expected = if i < fires.len() - 1 { 15 } else { 15 }; // wraps around midnight
        assert!(
            interval == expected || interval == expected + 24 * 60,
            "interval should be 15 minutes or wrap around midnight"
        );
    }

    println!("cron_next_fire: expr parsing + next-fire logic verified, strictly increasing — PASS");
}
