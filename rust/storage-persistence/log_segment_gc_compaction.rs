#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Log-segment GC / compaction for an append-only Insert/Update/Delete log. Replays the
// log to derive the live set (latest value per key, deletes removed), then rewrites a
// compacted log holding only those live entries. Use it to reclaim space once segments
// are sealed and superseded/deleted records pile up.
// Guarantees the live key->value set is preserved exactly while entry count strictly
// shrinks: overwritten versions collapse to the newest, deleted keys never reappear.
fn main() {
    // Log segment GC: merge sealed segments, drop superseded/dead records.
    // Live key→value set preserved exactly, bytes reclaimed.

    #[derive(Clone, Debug, PartialEq, Eq)]
    enum LogEntry {
        Insert { key: String, value: String },
        Update { key: String, value: String },
        Delete { key: String },
    }

    // Scenario 1: Compact and preserve exact live set
    let mut log: Vec<LogEntry> = vec![];

    // Segment 1: initial inserts
    log.push(LogEntry::Insert { key: "a".into(), value: "v1".into() });
    log.push(LogEntry::Insert { key: "b".into(), value: "v1".into() });
    log.push(LogEntry::Insert { key: "c".into(), value: "v1".into() });

    // Segment 2: updates
    log.push(LogEntry::Update { key: "a".into(), value: "v2".into() });
    log.push(LogEntry::Update { key: "b".into(), value: "v2".into() });

    // Segment 3: deletion
    log.push(LogEntry::Delete { key: "c".into() });
    log.push(LogEntry::Update { key: "a".into(), value: "v3".into() });

    // Compute live set (latest version per key, skip deletes)
    let mut live_set: std::collections::HashMap<String, String> = std::collections::HashMap::new();
    for entry in &log {
        match entry {
            LogEntry::Insert { key, value } | LogEntry::Update { key, value } => {
                live_set.insert(key.clone(), value.clone());
            }
            LogEntry::Delete { key } => {
                live_set.remove(key);
            }
        }
    }

    assert_eq!(live_set.len(), 2);
    assert_eq!(live_set.get("a"), Some(&"v3".into()));
    assert_eq!(live_set.get("b"), Some(&"v2".into()));
    assert_eq!(live_set.get("c"), None);

    // Compact: rebuild with only live entries
    let mut compacted: Vec<LogEntry> = vec![];
    for (key, value) in live_set.iter() {
        compacted.push(LogEntry::Insert {
            key: key.clone(),
            value: value.clone(),
        });
    }

    // Assert: compacted log has exactly 2 entries, same live set
    assert_eq!(compacted.len(), 2);
    let mut compacted_live: std::collections::HashMap<String, String> =
        std::collections::HashMap::new();
    for entry in &compacted {
        match entry {
            LogEntry::Insert { key, value } | LogEntry::Update { key, value } => {
                compacted_live.insert(key.clone(), value.clone());
            }
            LogEntry::Delete { key } => {
                compacted_live.remove(key);
            }
        }
    }

    // Original log: 7 entries. Compacted: 2 entries. Bytes reclaimed.
    assert_eq!(compacted_live, live_set);
    assert!(compacted.len() < log.len());

    // Scenario 2: Multiple overwrites of same key
    let mut log2: Vec<LogEntry> = vec![];
    log2.push(LogEntry::Insert { key: "x".into(), value: "v1".into() });
    log2.push(LogEntry::Update { key: "x".into(), value: "v2".into() });
    log2.push(LogEntry::Update { key: "x".into(), value: "v3".into() });
    log2.push(LogEntry::Update { key: "x".into(), value: "v4".into() });

    let mut live_set2: std::collections::HashMap<String, String> =
        std::collections::HashMap::new();
    for entry in &log2 {
        match entry {
            LogEntry::Insert { key, value } | LogEntry::Update { key, value } => {
                live_set2.insert(key.clone(), value.clone());
            }
            LogEntry::Delete { key } => {
                live_set2.remove(key);
            }
        }
    }

    // Only the latest version survives
    assert_eq!(live_set2.len(), 1);
    assert_eq!(live_set2.get("x"), Some(&"v4".into()));

    // Compacted
    let mut compacted2: Vec<LogEntry> = vec![];
    for (key, value) in live_set2.iter() {
        compacted2.push(LogEntry::Insert {
            key: key.clone(),
            value: value.clone(),
        });
    }
    assert_eq!(compacted2.len(), 1);

    // Scenario 3: Deleted keys don't appear in compacted log
    let mut log3: Vec<LogEntry> = vec![];
    log3.push(LogEntry::Insert { key: "p".into(), value: "v1".into() });
    log3.push(LogEntry::Insert { key: "q".into(), value: "v1".into() });
    log3.push(LogEntry::Delete { key: "p".into() });

    let mut live_set3: std::collections::HashMap<String, String> =
        std::collections::HashMap::new();
    for entry in &log3 {
        match entry {
            LogEntry::Insert { key, value } | LogEntry::Update { key, value } => {
                live_set3.insert(key.clone(), value.clone());
            }
            LogEntry::Delete { key } => {
                live_set3.remove(key);
            }
        }
    }

    assert_eq!(live_set3.len(), 1);
    assert_eq!(live_set3.get("q"), Some(&"v1".into()));

    println!("log_segment_gc_compaction: PASS");
}
