#![forbid(unsafe_code)]
// composes: append-to-N-replicas + lag + quorum-read + majority-VALUE-consensus
//
// A quorum read returns the (index, value) that a MAJORITY of replicas agree on — the value is
// load-bearing, not just the index. An entry present on only a minority (or a divergent value on
// a minority) is not returned.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashMap;

#[derive(Clone, Debug, PartialEq)]
struct Entry {
    index: usize,
    value: String,
}

// A quorum read scans the replicas' logs and returns the highest index whose (index, value) pair
// is held by >= quorum replicas. Scanning the logs (not just the tail) is what lets it fall back
// to the last committed entry when the newest entry lacks a quorum.
fn quorum_read(replicas: &[&[Entry]], quorum: usize) -> Option<Entry> {
    let mut counts: HashMap<(usize, String), usize> = HashMap::new();
    for rep in replicas {
        for e in rep.iter() {
            *counts.entry((e.index, e.value.clone())).or_insert(0) += 1;
        }
    }
    counts
        .into_iter()
        .filter(|(_, c)| *c >= quorum)
        .map(|((index, value), _)| Entry { index, value })
        .max_by_key(|e| e.index)
}

fn main() {
    let quorum = 2; // majority of 3

    // Stage 1: three replicas; replica3 lags (missing the latest entry).
    let mut r1: Vec<Entry> = Vec::new();
    let mut r2: Vec<Entry> = Vec::new();
    let mut r3: Vec<Entry> = Vec::new();
    for (i, v) in [(1, "val1"), (2, "val2")] {
        for r in [&mut r1, &mut r2, &mut r3] {
            r.push(Entry { index: i, value: v.to_string() });
        }
    }
    // Entry 3 reaches only a majority (r1, r2); r3 lags.
    r1.push(Entry { index: 3, value: "val3".to_string() });
    r2.push(Entry { index: 3, value: "val3".to_string() });

    // Stage 2+3: quorum read returns the VALUE agreed by a majority.
    let read = quorum_read(&[&r1, &r2, &r3], quorum);
    assert_eq!(
        read,
        Some(Entry { index: 3, value: "val3".to_string() }),
        "quorum read returns index 3 AND its majority-agreed value"
    );

    // A minority-only write is not returned; the read falls back to the committed index 3.
    let r3_solo = vec![Entry { index: 99, value: "ghost".to_string() }];
    let read2 = quorum_read(&[&r1, &r2, &r3_solo], quorum);
    assert_eq!(read2.as_ref().map(|e| e.index), Some(3), "minority index 99 is not chosen; quorum stays at 3");
    assert_ne!(read2.unwrap().value, "ghost", "the minority value is never returned");

    // A SPLIT value at the newest index (no majority agrees on A vs B) has no quorum, so the read
    // falls back to the last index a majority DID agree on (index 3).
    let mut r1b = r1.clone();
    let mut r2b = r2.clone();
    r1b.push(Entry { index: 4, value: "A".to_string() });
    r2b.push(Entry { index: 4, value: "B".to_string() });
    let read3 = quorum_read(&[&r1b, &r2b, &r3], quorum);
    assert_eq!(read3.map(|e| e.index), Some(3), "split value at index 4 has no quorum → falls back to committed index 3");

    println!("replicated_log_quorum: PASS");
}
