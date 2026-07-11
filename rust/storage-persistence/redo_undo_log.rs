#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn main() {
    // ARIES-lite: after crash, REDO committed txns (forward), UNDO in-flight (backward).
    // The exact final state must match: committed changes applied, in-flight rolled back.

    #[derive(Clone, Debug, PartialEq, Eq)]
    enum LogRecord {
        Begin { txn_id: u64, lsn: u64 },
        Update { txn_id: u64, key: String, old_val: String, new_val: String, lsn: u64 },
        Commit { txn_id: u64, lsn: u64 },
    }

    // State: key → value
    let mut db_state: std::collections::HashMap<String, String> = std::collections::HashMap::new();
    db_state.insert("a".into(), "v1".into());
    db_state.insert("b".into(), "v2".into());

    let mut log: Vec<LogRecord> = vec![];
    let mut committed_txns: std::collections::HashSet<u64> = std::collections::HashSet::new();
    let mut next_lsn = 1u64;

    let begin_txn = |log: &mut Vec<_>, txn_id: u64, lsn: &mut u64| {
        log.push(LogRecord::Begin { txn_id, lsn: *lsn });
        *lsn += 1;
    };

    let update_in_txn = |log: &mut Vec<_>, txn_id: u64, key: String, old_val: String, new_val: String, lsn: &mut u64| {
        log.push(LogRecord::Update { txn_id, key, old_val, new_val, lsn: *lsn });
        *lsn += 1;
    };

    let commit_txn = |log: &mut Vec<_>, txn_id: u64, committed: &mut std::collections::HashSet<u64>, lsn: &mut u64| {
        log.push(LogRecord::Commit { txn_id, lsn: *lsn });
        committed.insert(txn_id);
        *lsn += 1;
    };

    // Scenario 1: Two transactions, one committed, one not.
    begin_txn(&mut log, 1, &mut next_lsn);
    update_in_txn(&mut log, 1, "a".into(), "v1".into(), "updated_a".into(), &mut next_lsn);
    commit_txn(&mut log, 1, &mut committed_txns, &mut next_lsn); // Txn 1 committed at LSN 3

    begin_txn(&mut log, 2, &mut next_lsn);
    update_in_txn(&mut log, 2, "b".into(), "v2".into(), "updated_b".into(), &mut next_lsn);
    // Txn 2 NOT committed — crash here

    // Simulate crash under a STEAL/no-force buffer pool — the state on disk at crash time is
    // NOT the clean original. Model both hazards so BOTH recovery phases are load-bearing:
    //   - txn1 committed, but its page was NOT yet flushed  → a = v1  (REDO must reapply → updated_a)
    //   - txn2 uncommitted, but its dirty page WAS flushed   → b = updated_b (UNDO must roll back → v2)
    // Drop REDO and `a` stays v1; drop UNDO and `b` stays updated_b — either omission now fails.
    db_state.clear();
    db_state.insert("a".into(), "v1".into());
    db_state.insert("b".into(), "updated_b".into());

    // REDO phase: apply all updates from committed txns
    for record in &log {
        match record {
            LogRecord::Update { txn_id, key, new_val, .. } if committed_txns.contains(txn_id) => {
                db_state.insert(key.clone(), new_val.clone());
            }
            _ => {}
        }
    }

    // UNDO phase: roll back all updates from uncommitted txns
    for record in log.iter().rev() {
        match record {
            LogRecord::Update { txn_id, key, old_val, .. } if !committed_txns.contains(txn_id) => {
                db_state.insert(key.clone(), old_val.clone());
            }
            _ => {}
        }
    }

    // Assert exact state: txn 1 committed (a→updated_a), txn 2 rolled back (b→v2)
    assert_eq!(db_state.get("a"), Some(&"updated_a".into()));
    assert_eq!(db_state.get("b"), Some(&"v2".into()));

    // Scenario 2: All transactions committed — crash after all commits
    db_state.clear();
    db_state.insert("x".into(), "x1".into());
    db_state.insert("y".into(), "y1".into());

    let mut log2: Vec<LogRecord> = vec![];
    let mut committed2: std::collections::HashSet<u64> = std::collections::HashSet::new();
    let mut lsn2 = 1u64;

    begin_txn(&mut log2, 10, &mut lsn2);
    update_in_txn(&mut log2, 10, "x".into(), "x1".into(), "x_new".into(), &mut lsn2);
    commit_txn(&mut log2, 10, &mut committed2, &mut lsn2);

    begin_txn(&mut log2, 11, &mut lsn2);
    update_in_txn(&mut log2, 11, "y".into(), "y1".into(), "y_new".into(), &mut lsn2);
    commit_txn(&mut log2, 11, &mut committed2, &mut lsn2);
    // Crash here: all are committed

    // Recovery
    db_state.clear();
    db_state.insert("x".into(), "x1".into());
    db_state.insert("y".into(), "y1".into());

    for record in &log2 {
        match record {
            LogRecord::Update { txn_id, key, new_val, .. } if committed2.contains(txn_id) => {
                db_state.insert(key.clone(), new_val.clone());
            }
            _ => {}
        }
    }

    for record in log2.iter().rev() {
        match record {
            LogRecord::Update { txn_id, key, old_val, .. } if !committed2.contains(txn_id) => {
                db_state.insert(key.clone(), old_val.clone());
            }
            _ => {}
        }
    }

    assert_eq!(db_state.get("x"), Some(&"x_new".into()));
    assert_eq!(db_state.get("y"), Some(&"y_new".into()));

    println!("redo_undo_log: PASS");
}
