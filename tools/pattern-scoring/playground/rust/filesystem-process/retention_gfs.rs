#![forbid(unsafe_code)]
//! retention_gfs — grandfather-father-son retention over a synthetic date set; keeps exactly.
//!
//! Core idea: keep the most recent snapshot in each period bucket (daily within 7 days, weekly
//! within 4 weeks, monthly within 12 months); everything else is pruned. THE ONE LAW: apply GFS
//! retention, then assert the kept set equals — EXACTLY — an independently computed expected set
//! (newest-per-bucket-within-window), not merely a loose count. A drop or duplicate would diverge.
//! When to use: backup rotation, snapshot retention, tiered archival.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::{HashMap, HashSet};

/// The three (bucket-divisor, window-in-buckets) rules: daily/7, weekly/4, monthly/12.
const RULES: [(u32, u32); 3] = [(1, 7), (7, 4), (30, 12)];

fn gfs_retain(dates: &[u32]) -> Vec<u32> {
    let last = *dates.last().unwrap();
    let mut result = Vec::new();
    let mut seen: [HashSet<u32>; 3] = [HashSet::new(), HashSet::new(), HashSet::new()];

    // Newest first: the first snapshot seen in a bucket is that bucket's most recent.
    for &d in dates.iter().rev() {
        let mut keep = false;
        for (r, &(divisor, window)) in RULES.iter().enumerate() {
            let bucket = d / divisor;
            let last_bucket = last / divisor;
            if bucket + window >= last_bucket && !seen[r].contains(&bucket) {
                seen[r].insert(bucket);
                keep = true;
            }
        }
        if keep {
            result.push(d);
        }
    }
    result.sort();
    result
}

/// Independent expected set: for each rule, the MAX date in every in-window bucket; union them.
fn expected_gfs(dates: &[u32]) -> Vec<u32> {
    let last = *dates.iter().max().unwrap();
    let mut keep: HashSet<u32> = HashSet::new();
    for &(divisor, window) in &RULES {
        let last_bucket = last / divisor;
        let mut newest: HashMap<u32, u32> = HashMap::new();
        for &d in dates {
            let bucket = d / divisor;
            if bucket + window >= last_bucket {
                let e = newest.entry(bucket).or_insert(0);
                if d >= *e {
                    *e = d;
                }
            }
        }
        for (_, &d) in &newest {
            keep.insert(d);
        }
    }
    let mut v: Vec<u32> = keep.into_iter().collect();
    v.sort();
    v
}

fn main() {
    // Planted case 1: a full year of daily snapshots (0..=364).
    let daily: Vec<u32> = (0..365).collect();
    let retained = gfs_retain(&daily);
    let expected = expected_gfs(&daily);

    // THE ONE LAW: exact set equality with the independent computation.
    assert_eq!(retained, expected, "GFS kept set must match the independent expected set exactly");

    // Concrete anchors that must hold for 0..=364 (last=364):
    // daily window keeps every day with date >= 364-7 = 357 → days 357..=364 (8 snapshots).
    for d in 357..=364u32 {
        assert!(retained.contains(&d), "recent day {d} must be retained by the daily rule");
    }
    // It is a real reduction, strictly ordered, all valid.
    assert!(retained.len() < 40 && retained.len() > 15, "365→{} is the expected reduction", retained.len());
    for w in retained.windows(2) {
        assert!(w[1] > w[0], "retained dates must be strictly increasing (no dups)");
    }
    assert!(retained.iter().all(|&d| d < 365), "every retained date is a real snapshot");

    // Planted case 2: sparse weekly-only snapshots — still exact against the independent set.
    let weekly: Vec<u32> = (0..52).map(|w| w * 7).collect();
    assert_eq!(gfs_retain(&weekly), expected_gfs(&weekly), "sparse set must also match exactly");

    println!(
        "retention_gfs: kept set == independent expected set exactly ({} of 365) — PASS",
        retained.len()
    );
}
