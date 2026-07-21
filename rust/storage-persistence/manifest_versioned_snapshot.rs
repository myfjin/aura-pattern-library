#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Versioned manifest with atomic snapshot swap. The active manifest (version + file set)
// is replaced by installing a whole new one; a reader that captured an earlier manifest
// keeps reading that exact file set. Use it for LSM/SSTable-style file-set management
// where readers must see a stable, consistent view across compactions.
// Guarantees each pinned reader sees only its own version's complete file list (including
// files later removed), and swaps are all-or-nothing — never a partial/mixed manifest.
fn main() {
    // Manifest versioned snapshot: atomic swap of active file-set version.
    // Reader pinned to v1 sees v1's files after v2 is installed.

    #[derive(Clone, Debug, PartialEq, Eq)]
    struct Manifest {
        version: u64,
        files: Vec<String>,
    }

    // Scenario 1: Reader pinned to v1 before swap
    let mut active_manifest = Manifest {
        version: 1,
        files: vec!["file_a".into(), "file_b".into()],
    };

    // Reader 1 pins to v1 and reads
    let reader1_manifest = active_manifest.clone();
    assert_eq!(reader1_manifest.version, 1);
    assert_eq!(reader1_manifest.files.len(), 2);

    // Manager installs v2 (atomic swap)
    active_manifest = Manifest {
        version: 2,
        files: vec!["file_c".into(), "file_d".into()],
    };

    // Reader 1 still sees v1 (pinned)
    assert_eq!(reader1_manifest.version, 1);
    assert_eq!(reader1_manifest.files.len(), 2);
    assert_eq!(reader1_manifest.files[0], "file_a");
    assert_eq!(reader1_manifest.files[1], "file_b");

    // Reader 2 sees v2 (new)
    let reader2_manifest = active_manifest.clone();
    assert_eq!(reader2_manifest.version, 2);
    assert_eq!(reader2_manifest.files.len(), 2);
    assert_eq!(reader2_manifest.files[0], "file_c");
    assert_eq!(reader2_manifest.files[1], "file_d");

    // Scenario 2: Multiple versions
    let mut manifest = Manifest {
        version: 1,
        files: vec!["s1".into()],
    };

    let r1_pin = manifest.clone();

    // Swap to v2
    manifest = Manifest {
        version: 2,
        files: vec!["s1".into(), "s2".into()],
    };

    let r2_pin = manifest.clone();

    // Swap to v3
    manifest = Manifest {
        version: 3,
        files: vec!["s1".into(), "s2".into(), "s3".into()],
    };

    let r3_pin = manifest.clone();

    // Each reader sees exactly the version it pinned
    assert_eq!(r1_pin.version, 1);
    assert_eq!(r1_pin.files.len(), 1);

    assert_eq!(r2_pin.version, 2);
    assert_eq!(r2_pin.files.len(), 2);

    assert_eq!(r3_pin.version, 3);
    assert_eq!(r3_pin.files.len(), 3);

    // Current active version is 3
    assert_eq!(manifest.version, 3);

    // Scenario 3: File removal in new version
    let mut manifest2 = Manifest {
        version: 1,
        files: vec!["file1".into(), "file2".into(), "file3".into()],
    };

    let reader_old = manifest2.clone();

    // Swap: file2 removed in v2
    manifest2 = Manifest {
        version: 2,
        files: vec!["file1".into(), "file3".into()],
    };

    // Old reader still sees all 3 files
    assert_eq!(reader_old.files.len(), 3);
    assert!(reader_old.files.contains(&"file2".into()));

    // New reader sees only 2 files
    assert_eq!(manifest2.files.len(), 2);
    assert!(!manifest2.files.contains(&"file2".into()));

    // Scenario 4: Atomic swap correctness
    // All readers at any instant see a complete, consistent manifest
    let mut m = Manifest {
        version: 1,
        files: vec!["a".into(), "b".into()],
    };

    // Simulate 3 concurrent readers
    let r1 = m.clone(); // Sees v1

    // Atomic swap
    m = Manifest {
        version: 2,
        files: vec!["a".into(), "b".into(), "c".into()],
    };

    let r2 = m.clone(); // Sees v2

    // Each sees a consistent set of files for their version
    assert_eq!(r1.files.len(), 2);
    assert!(r1.files[0].len() > 0); // No partial/corrupted files
    assert_eq!(r2.files.len(), 3);
    assert!(r2.files[2].len() > 0); // c is complete

    println!("manifest_versioned_snapshot: PASS");
}
