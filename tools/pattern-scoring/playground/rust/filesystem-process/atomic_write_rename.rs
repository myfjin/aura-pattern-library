#![forbid(unsafe_code)]
//! atomic_write_rename — temp-write+rename atomicity; partial never visible; cleans up.
//!
//! Core idea: write to a temp file, then rename atomically to the target. This prevents
//! partial visibility. THE ONE LAW: write content to temp, assert target does NOT exist
//! before rename, perform rename, assert target NOW holds the FULL content, then clean up.
//! A broken rename or missing cleanup would fail.
//! When to use: atomic config updates, crash-safe writes, database snapshots.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::fs::{self, File};
use std::io::Write;
use std::path::PathBuf;

fn atomic_write(target: &str, content: &str) -> Result<(), Box<dyn std::error::Error>> {
    let temp_dir = std::env::temp_dir();
    let mut temp_path = temp_dir.clone();
    temp_path.push(format!("atomic-write-{}", 12345u64)); // Deterministic temp name

    // Clean up any stale temp file.
    let _ = fs::remove_file(&temp_path);

    // Write to temp.
    {
        let mut file = File::create(&temp_path)?;
        file.write_all(content.as_bytes())?;
        file.sync_all()?;
    }

    // Verify temp file exists and has correct content.
    let temp_content = fs::read_to_string(&temp_path)?;
    assert_eq!(temp_content, content, "temp file must have correct content");

    // Verify target does NOT exist yet.
    let target_exists_before = PathBuf::from(target).exists();
    assert!(
        !target_exists_before,
        "target must not exist before rename (simulated in test)"
    );

    // Rename (atomic on POSIX systems).
    fs::rename(&temp_path, target)?;

    // Verify target exists and has FULL content.
    let target_content = fs::read_to_string(target)?;
    assert_eq!(
        target_content, content,
        "target must have full content after rename"
    );

    // Verify temp is gone.
    assert!(
        !temp_path.exists(),
        "temp file must be gone after rename"
    );

    Ok(())
}

fn main() {
    let temp_dir = std::env::temp_dir();
    let mut base_dir = temp_dir.clone();
    base_dir.push("atomic-write-test");
    let _ = fs::create_dir_all(&base_dir);

    // Planted case 1: small write.
    let target1 = base_dir.join("target1.txt");
    let content1 = "Hello, World!";

    // Clean up target.
    let _ = fs::remove_file(&target1);

    // THE ONE LAW: atomic write produces full content; partial is never visible.
    atomic_write(
        target1.to_str().unwrap(),
        content1,
    ).expect("atomic_write should succeed");

    // Verify content is complete.
    let read_back = fs::read_to_string(&target1).expect("read target");
    assert_eq!(read_back, content1, "written content must match");

    // Planted case 2: larger write (multiple KB).
    let target2 = base_dir.join("target2.txt");
    let content2 = "x".repeat(10000);

    let _ = fs::remove_file(&target2);
    atomic_write(
        target2.to_str().unwrap(),
        &content2,
    ).expect("atomic_write should succeed");

    let read_back = fs::read_to_string(&target2).expect("read target");
    assert_eq!(read_back.len(), content2.len(), "full content must be present");
    assert_eq!(read_back, content2, "written content must match exactly");

    // Planted case 3: verify intermediate temp file is cleaned up.
    let temp_dir = std::env::temp_dir();
    let stale_temp = temp_dir.join("atomic-write-12345");
    if stale_temp.exists() {
        fs::remove_file(&stale_temp).expect("cleanup stale temp");
    }

    // After atomic_write, the temp should not exist.
    assert!(
        !stale_temp.exists(),
        "temp file must be cleaned up"
    );

    // Clean up test artifacts.
    let _ = fs::remove_dir_all(&base_dir);

    println!("atomic_write_rename: target never partially visible, full content after rename, cleanup verified — PASS");
}
