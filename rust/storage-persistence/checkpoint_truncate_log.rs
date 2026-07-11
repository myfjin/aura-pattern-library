#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn main() {
    // Checkpoint: at LSN L, all WAL records with lsn <= L are discardable.
    // Recovery from L reconstructs exact state.

    #[derive(Clone, Debug, PartialEq, Eq)]
    struct LogRecord {
        lsn: u64,
        key: String,
        value: String,
    }

    #[derive(Clone, Debug, PartialEq, Eq)]
    struct Checkpoint {
        lsn: u64,
        state_snapshot: std::collections::HashMap<String, String>,
    }

    // Scenario 1: Build log, checkpoint, truncate, recover
    let mut log: Vec<LogRecord> = vec![];
    let mut db_state: std::collections::HashMap<String, String> = std::collections::HashMap::new();

    // Insert records
    db_state.insert("a".into(), "v1".into());
    log.push(LogRecord { lsn: 1, key: "a".into(), value: "v1".into() });

    db_state.insert("b".into(), "v2".into());
    log.push(LogRecord { lsn: 2, key: "b".into(), value: "v2".into() });

    db_state.insert("c".into(), "v3".into());
    log.push(LogRecord { lsn: 3, key: "c".into(), value: "v3".into() });

    // Checkpoint at LSN 3
    let ckpt = Checkpoint {
        lsn: 3,
        state_snapshot: db_state.clone(),
    };

    // Add more records after checkpoint
    db_state.insert("d".into(), "v4".into());
    log.push(LogRecord { lsn: 4, key: "d".into(), value: "v4".into() });

    db_state.insert("e".into(), "v5".into());
    log.push(LogRecord { lsn: 5, key: "e".into(), value: "v5".into() });

    // Truncate log: discard all records with lsn <= checkpoint.lsn
    let truncated_log: Vec<_> = log
        .iter()
        .filter(|r| r.lsn > ckpt.lsn)
        .cloned()
        .collect();

    assert_eq!(truncated_log.len(), 2);
    assert_eq!(truncated_log[0].lsn, 4);
    assert_eq!(truncated_log[1].lsn, 5);

    // Scenario 2: Recovery from checkpoint
    // Start with checkpoint state
    let mut recovered_state = ckpt.state_snapshot.clone();

    // Replay post-checkpoint logs
    for record in &truncated_log {
        recovered_state.insert(record.key.clone(), record.value.clone());
    }

    // Assert exact state
    assert_eq!(recovered_state.get("a"), Some(&"v1".into()));
    assert_eq!(recovered_state.get("b"), Some(&"v2".into()));
    assert_eq!(recovered_state.get("c"), Some(&"v3".into()));
    assert_eq!(recovered_state.get("d"), Some(&"v4".into()));
    assert_eq!(recovered_state.get("e"), Some(&"v5".into()));
    assert_eq!(recovered_state.len(), 5);

    // Scenario 3: Crash before checkpoint completion
    // We have a valid checkpoint at LSN 3, log continues to LSN 5
    let mut log2: Vec<LogRecord> = vec![];
    let mut db_state2: std::collections::HashMap<String, String> = std::collections::HashMap::new();

    db_state2.insert("x".into(), "x1".into());
    log2.push(LogRecord { lsn: 1, key: "x".into(), value: "x1".into() });

    db_state2.insert("y".into(), "y1".into());
    log2.push(LogRecord { lsn: 2, key: "y".into(), value: "y1".into() });

    let ckpt2 = Checkpoint {
        lsn: 2,
        state_snapshot: db_state2.clone(),
    };

    // New writes after checkpoint
    db_state2.insert("z".into(), "z1".into());
    log2.push(LogRecord { lsn: 3, key: "z".into(), value: "z1".into() });

    // CRASH: checkpoint is durable, but newer logs might not be
    // Recovery uses checkpoint as base
    let mut recovered2 = ckpt2.state_snapshot.clone();

    // Only replay logs that survived (in this case, we trust the checkpoint fully)
    for record in log2.iter().filter(|r| r.lsn > ckpt2.lsn) {
        recovered2.insert(record.key.clone(), record.value.clone());
    }

    // Assert: at minimum we have checkpoint state
    assert_eq!(recovered2.get("x"), Some(&"x1".into()));
    assert_eq!(recovered2.get("y"), Some(&"y1".into()));

    println!("checkpoint_truncate_log: PASS");
}
