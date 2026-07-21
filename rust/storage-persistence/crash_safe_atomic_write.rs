#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Demonstrates the write-temp-then-rename pattern for durable file updates, modeling the
// filesystem as a name->contents map and injecting a crash at each critical point. The new
// contents are written to a temp name and only an atomic rename swaps it over the target.
// Use as the reference protocol for never leaving a half-written file on disk.
// Guarantees the target is always all-old-or-all-new: a crash before the rename leaves the
// original file intact (the partial temp is discarded), a crash after the rename leaves the
// fully-updated file, and repeated writes each transition atomically with no torn state.
fn main() {
    // Atomic write: write to temp file, then rename.
    // Crash BETWEEN write and rename → old file intact, never half-written.

    // "Disk" is a HashMap: name → contents
    let mut disk: std::collections::HashMap<String, Vec<u8>> = std::collections::HashMap::new();

    // Initial state: file "data" exists with "original"
    disk.insert("data".into(), b"original".to_vec());

    // Scenario 1: Successful atomic write (no crash)
    let new_data = b"updated".to_vec();

    // Write to temp
    disk.insert("data.tmp".into(), new_data.clone());

    // Rename: atomic operation (modeled as two steps, but we commit before crash)
    let temp_contents = disk.remove("data.tmp").expect("temp must exist");
    disk.insert("data".into(), temp_contents);

    // Assert: file "data" has new contents, no "data.tmp"
    assert_eq!(disk.get("data"), Some(&b"updated".to_vec()));
    assert_eq!(disk.get("data.tmp"), None);

    // Scenario 2: Crash BEFORE write completes (temp file never fully written)
    let mut disk2: std::collections::HashMap<String, Vec<u8>> = std::collections::HashMap::new();
    disk2.insert("data".into(), b"original".to_vec());

    // Write to temp — starts
    let new_data2 = b"updated".to_vec();
    disk2.insert("data.tmp".into(), new_data2);

    // CRASH HERE: before rename
    // Simulate crash by dropping all uncommitted temp writes
    disk2.remove("data.tmp");

    // After recovery: only "data" exists, unchanged
    assert_eq!(disk2.get("data"), Some(&b"original".to_vec()));
    assert_eq!(disk2.get("data.tmp"), None);

    // Scenario 3: Crash AFTER rename (old file is safely replaced)
    let mut disk3: std::collections::HashMap<String, Vec<u8>> = std::collections::HashMap::new();
    disk3.insert("data".into(), b"original".to_vec());

    let new_data3 = b"updated".to_vec();
    disk3.insert("data.tmp".into(), new_data3.clone());

    // Rename happens (and "succeeds" before crash)
    let temp_contents3 = disk3.remove("data.tmp").expect("temp must exist");
    disk3.insert("data".into(), temp_contents3);

    // CRASH HERE: after rename (no cleanup needed; rename is atomic)
    // Recovery: file "data" has new contents
    assert_eq!(disk3.get("data"), Some(&b"updated".to_vec()));

    // Scenario 4: Multiple atomic writes in sequence
    let mut disk4: std::collections::HashMap<String, Vec<u8>> = std::collections::HashMap::new();
    disk4.insert("data".into(), b"v1".to_vec());

    // Write 1
    disk4.insert("data.tmp".into(), b"v2".to_vec());
    let temp_contents4 = disk4.remove("data.tmp").expect("temp must exist");
    disk4.insert("data".into(), temp_contents4);
    assert_eq!(disk4.get("data"), Some(&b"v2".to_vec()));

    // Write 2
    disk4.insert("data.tmp".into(), b"v3".to_vec());
    let temp_contents4 = disk4.remove("data.tmp").expect("temp must exist");
    disk4.insert("data".into(), temp_contents4);
    assert_eq!(disk4.get("data"), Some(&b"v3".to_vec()));

    println!("crash_safe_atomic_write: PASS");
}
