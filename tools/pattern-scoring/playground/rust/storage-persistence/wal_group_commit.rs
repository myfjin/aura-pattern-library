#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::VecDeque;

// WAL group commit. Multiple transactions append records to the log, then one fsync
// advances a synced_lsn watermark to the highest batched LSN, persisting the whole
// group at once. Use it to amortize fsync cost across many concurrent transactions.
// Guarantees an all-or-nothing batch boundary: recovery replays only records with
// lsn <= synced_lsn, so a crash before the fsync recovers none of the group and a
// crash after it recovers all N — no transaction in a batch is durable by halves.
fn main() {
    // WAL group commit: batch N transactions into one fsync.
    // Crash before fsync → none recovered.
    // Crash after fsync → all N recovered.

    #[derive(Clone, Debug, PartialEq)]
    struct TxnRecord {
        id: u64,
        data: String,
        lsn: u64,
    }

    let mut wal: VecDeque<TxnRecord> = VecDeque::new();
    let mut synced_lsn: u64 = 0;
    let mut next_lsn: u64 = 1;

    // Function to append a transaction to WAL
    let append_txn = |wal: &mut VecDeque<TxnRecord>, id: u64, data: String, lsn: &mut u64| {
        wal.push_back(TxnRecord {
            id,
            data,
            lsn: *lsn,
        });
        *lsn += 1;
    };

    // Function to flush all unflushed records
    let group_commit = |wal: &VecDeque<TxnRecord>, synced_lsn: &mut u64| {
        if let Some(max_rec) = wal.iter().max_by_key(|r| r.lsn) {
            *synced_lsn = max_rec.lsn;
        }
    };

    // Scenario 1: Add transactions and commit
    append_txn(&mut wal, 1, "txn1".into(), &mut next_lsn);
    append_txn(&mut wal, 2, "txn2".into(), &mut next_lsn);
    append_txn(&mut wal, 3, "txn3".into(), &mut next_lsn);

    // Before crash: synced_lsn is still 0, so txns 1–3 are unflushed
    assert_eq!(synced_lsn, 0, "Before fsync, synced_lsn must be 0");
    assert_eq!(wal.len(), 3, "WAL must have 3 records");

    // Commit: group_commit flushes all
    group_commit(&wal, &mut synced_lsn);
    assert_eq!(synced_lsn, 3, "After fsync, synced_lsn must be 3");

    // Scenario 2: Simulate crash BEFORE fsync
    let mut wal2: VecDeque<TxnRecord> = VecDeque::new();
    let synced_lsn2: u64 = 0;
    let mut next_lsn2: u64 = 1;

    append_txn(&mut wal2, 10, "txn10".into(), &mut next_lsn2);
    append_txn(&mut wal2, 11, "txn11".into(), &mut next_lsn2);
    // Crash happens here: synced_lsn2 is still 0
    // On recovery, we only replay committed (synced) records
    let recovered = wal2
        .iter()
        .filter(|r| r.lsn <= synced_lsn2)
        .collect::<Vec<_>>();
    assert_eq!(recovered.len(), 0, "Recovery before fsync must recover no txns");

    // Scenario 3: Simulate crash AFTER fsync
    let mut wal3: VecDeque<TxnRecord> = VecDeque::new();
    let mut synced_lsn3: u64 = 0;
    let mut next_lsn3: u64 = 1;

    append_txn(&mut wal3, 20, "txn20".into(), &mut next_lsn3);
    append_txn(&mut wal3, 21, "txn21".into(), &mut next_lsn3);
    append_txn(&mut wal3, 22, "txn22".into(), &mut next_lsn3);

    // fsync happens
    group_commit(&wal3, &mut synced_lsn3);
    assert_eq!(synced_lsn3, 3);

    // Crash happens here: synced_lsn3 is 3
    // On recovery, replay all records with lsn <= synced_lsn3
    let recovered3 = wal3
        .iter()
        .filter(|r| r.lsn <= synced_lsn3)
        .collect::<Vec<_>>();
    assert_eq!(recovered3.len(), 3, "Recovery after fsync must recover all 3 txns");
    assert_eq!(recovered3[0].id, 20);
    assert_eq!(recovered3[1].id, 21);
    assert_eq!(recovered3[2].id, 22);

    println!("wal_group_commit: PASS");
}
