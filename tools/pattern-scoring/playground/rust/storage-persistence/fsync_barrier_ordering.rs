#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// fsync barrier / durable-LSN ordering. Log records carry increasing LSNs; a barrier
// advances a durable_lsn watermark, marking every record up to it as persisted.
// Use it to reason about what a crash may lose: recovery keeps only records with
// lsn <= durable_lsn and discards everything after the last barrier.
// Guarantees prefix consistency — records before a barrier are durable before any
// after it, so a crash yields a clean prefix (nothing after the barrier survives).
fn main() {
    // fsync barrier: writes before barrier are durable before any after it.
    // Crash between → only prefix-consistent state.

    #[derive(Clone, Debug, PartialEq, Eq)]
    struct WriteOp {
        key: String,
        value: String,
        lsn: u64,
    }

    let mut wal: Vec<WriteOp> = vec![];
    let mut next_lsn = 1u64;

    // Scenario 1: Writes before barrier, then barrier, then writes after
    wal.push(WriteOp {
        key: "a".into(),
        value: "v1".into(),
        lsn: next_lsn,
    });
    next_lsn += 1;

    wal.push(WriteOp {
        key: "b".into(),
        value: "v2".into(),
        lsn: next_lsn,
    });
    next_lsn += 1;

    // BARRIER: fsync up to LSN 2
    let durable_lsn: u64 = 2;

    wal.push(WriteOp {
        key: "c".into(),
        value: "v3".into(),
        lsn: next_lsn,
    });
    next_lsn += 1;

    wal.push(WriteOp {
        key: "d".into(),
        value: "v4".into(),
        lsn: next_lsn,
    });

    // CRASH after barrier but before end of WAL
    // On recovery: only records with lsn <= durable_lsn are recoverable
    let recovered: Vec<_> = wal.iter().filter(|w| w.lsn <= durable_lsn).collect();

    assert_eq!(recovered.len(), 2);
    assert_eq!(recovered[0].key, "a");
    assert_eq!(recovered[1].key, "b");

    // Records after barrier are lost
    let lost: Vec<_> = wal.iter().filter(|w| w.lsn > durable_lsn).collect();
    assert_eq!(lost.len(), 2);

    // Scenario 2: Multiple barriers
    let mut wal2: Vec<WriteOp> = vec![];
    let mut lsn2 = 1u64;

    wal2.push(WriteOp { key: "x".into(), value: "x1".into(), lsn: lsn2 });
    lsn2 += 1;
    wal2.push(WriteOp { key: "y".into(), value: "y1".into(), lsn: lsn2 });
    lsn2 += 1;

    // Barrier 1 at LSN 2
    let _durable_lsn2_first: u64 = 2;

    wal2.push(WriteOp { key: "z".into(), value: "z1".into(), lsn: lsn2 });
    lsn2 += 1;

    // Barrier 2 at LSN 3
    let durable_lsn2: u64 = 3;

    wal2.push(WriteOp { key: "w".into(), value: "w1".into(), lsn: lsn2 });

    // CRASH before Barrier 2 can fully complete
    // durable_lsn2 still = 3
    // Scenario: pretend we crashed between recording LSN 3 and LSN 4

    let recovered2: Vec<_> = wal2.iter().filter(|w| w.lsn <= durable_lsn2).collect();
    assert_eq!(recovered2.len(), 3);
    assert_eq!(recovered2[0].key, "x");
    assert_eq!(recovered2[1].key, "y");
    assert_eq!(recovered2[2].key, "z");

    // Scenario 3: Crash before first barrier
    let mut wal3: Vec<WriteOp> = vec![];
    let durable_lsn3: u64 = 0; // No barrier yet
    let mut lsn3 = 1u64;

    wal3.push(WriteOp { key: "m".into(), value: "m1".into(), lsn: lsn3 });
    lsn3 += 1;
    wal3.push(WriteOp { key: "n".into(), value: "n1".into(), lsn: lsn3 });

    // CRASH before any barrier
    // durable_lsn3 = 0, so nothing is recoverable
    let recovered3: Vec<_> = wal3.iter().filter(|w| w.lsn <= durable_lsn3).collect();
    assert_eq!(recovered3.len(), 0);

    println!("fsync_barrier_ordering: PASS");
}
