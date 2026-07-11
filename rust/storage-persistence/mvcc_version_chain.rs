#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn main() {
    // MVCC version chain: per-key versions by commit ts.
    // Snapshot at ts T sees newest version <= T; newer hidden.

    #[derive(Clone, Debug, PartialEq, Eq)]
    struct VersionEntry {
        commit_ts: u64,
        value: String,
    }

    // Key → version chain (in commit ts order)
    let mut mvcc_store: std::collections::HashMap<String, Vec<VersionEntry>> =
        std::collections::HashMap::new();

    // Scenario 1: Write and snapshot at different timestamps
    // Insert key "a" at ts=1
    mvcc_store.insert(
        "a".into(),
        vec![VersionEntry {
            commit_ts: 1,
            value: "v1".into(),
        }],
    );

    // Update at ts=3
    mvcc_store.get_mut("a").unwrap().push(VersionEntry {
        commit_ts: 3,
        value: "v2".into(),
    });

    // Update at ts=5
    mvcc_store.get_mut("a").unwrap().push(VersionEntry {
        commit_ts: 5,
        value: "v3".into(),
    });

    // Snapshot at ts=2: should see v1
    let snapshot_ts = 2u64;
    let version_at_2 = mvcc_store
        .get("a")
        .and_then(|chain| {
            chain
                .iter()
                .filter(|v| v.commit_ts <= snapshot_ts)
                .max_by_key(|v| v.commit_ts)
                .cloned()
        });

    assert_eq!(version_at_2, Some(VersionEntry {
        commit_ts: 1,
        value: "v1".into(),
    }));

    // Snapshot at ts=4: should see v2
    let version_at_4 = mvcc_store
        .get("a")
        .and_then(|chain| {
            chain
                .iter()
                .filter(|v| v.commit_ts <= 4)
                .max_by_key(|v| v.commit_ts)
                .cloned()
        });

    assert_eq!(version_at_4, Some(VersionEntry {
        commit_ts: 3,
        value: "v2".into(),
    }));

    // Snapshot at ts=6: should see v3
    let version_at_6 = mvcc_store
        .get("a")
        .and_then(|chain| {
            chain
                .iter()
                .filter(|v| v.commit_ts <= 6)
                .max_by_key(|v| v.commit_ts)
                .cloned()
        });

    assert_eq!(version_at_6, Some(VersionEntry {
        commit_ts: 5,
        value: "v3".into(),
    }));

    // Scenario 2: Multiple keys with overlapping versions
    mvcc_store.insert(
        "b".into(),
        vec![
            VersionEntry {
                commit_ts: 2,
                value: "b_v1".into(),
            },
            VersionEntry {
                commit_ts: 4,
                value: "b_v2".into(),
            },
        ],
    );

    // Snapshot at ts=3: a→v2 (from ts=3), b→b_v1 (from ts=2)
    let snap_3_a = mvcc_store
        .get("a")
        .and_then(|chain| {
            chain
                .iter()
                .filter(|v| v.commit_ts <= 3)
                .max_by_key(|v| v.commit_ts)
        });
    let snap_3_b = mvcc_store
        .get("b")
        .and_then(|chain| {
            chain
                .iter()
                .filter(|v| v.commit_ts <= 3)
                .max_by_key(|v| v.commit_ts)
        });

    assert_eq!(snap_3_a.map(|v| &v.value), Some(&"v2".into()));
    assert_eq!(snap_3_b.map(|v| &v.value), Some(&"b_v1".into()));

    // Snapshot at ts=5: a→v3 (from ts=5), b→b_v2 (from ts=4)
    let snap_5_a = mvcc_store
        .get("a")
        .and_then(|chain| {
            chain
                .iter()
                .filter(|v| v.commit_ts <= 5)
                .max_by_key(|v| v.commit_ts)
        });
    let snap_5_b = mvcc_store
        .get("b")
        .and_then(|chain| {
            chain
                .iter()
                .filter(|v| v.commit_ts <= 5)
                .max_by_key(|v| v.commit_ts)
        });

    assert_eq!(snap_5_a.map(|v| &v.value), Some(&"v3".into()));
    assert_eq!(snap_5_b.map(|v| &v.value), Some(&"b_v2".into()));

    println!("mvcc_version_chain: PASS");
}
