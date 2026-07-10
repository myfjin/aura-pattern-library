#![forbid(unsafe_code)]
//! file_dedup_hash — group synthetic file table by content hash; planted dupes grouped.
//!
//! Core idea: hash file contents, group files by hash, identify duplicates.
//! THE ONE LAW: plant a table of files with known duplicates, compute hashes, group
//! by hash, and assert duplicates are correctly grouped and unique files are singletons.
//! A broken hash or missing grouping would fail.
//! When to use: deduplication, backup, storage optimization, file integrity.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashMap;

fn simple_hash(data: &[u8]) -> u64 {
    let mut hash = 5381u64;
    for &byte in data {
        hash = hash.wrapping_mul(33).wrapping_add(byte as u64);
    }
    hash
}

struct FileEntry {
    name: String,
    content: Vec<u8>,
}

fn group_by_content_hash(files: &[FileEntry]) -> HashMap<u64, Vec<String>> {
    let mut groups: HashMap<u64, Vec<String>> = HashMap::new();
    for file in files {
        let hash = simple_hash(&file.content);
        groups.entry(hash).or_insert_with(Vec::new).push(file.name.clone());
    }
    groups
}

fn main() {
    // Planted case: 5 files, 3 unique contents (2 duplicates).
    let files = vec![
        FileEntry { name: "a.txt".to_string(), content: b"hello".to_vec() },
        FileEntry { name: "b.txt".to_string(), content: b"hello".to_vec() }, // dup of a
        FileEntry { name: "c.txt".to_string(), content: b"world".to_vec() },
        FileEntry { name: "d.txt".to_string(), content: b"hello".to_vec() }, // dup of a
        FileEntry { name: "e.txt".to_string(), content: b"goodbye".to_vec() },
    ];

    let groups = group_by_content_hash(&files);

    // THE ONE LAW: we should have 3 unique content hashes.
    assert_eq!(groups.len(), 3, "should have 3 unique content hashes");

    // Find the hash for "hello" (should have 3 files: a, b, d).
    let hello_hash = simple_hash(b"hello");
    assert!(groups.contains_key(&hello_hash), "hello hash should exist");
    let hello_group = &groups[&hello_hash];
    assert_eq!(hello_group.len(), 3, "hello should have 3 duplicates");
    assert!(hello_group.contains(&"a.txt".to_string()));
    assert!(hello_group.contains(&"b.txt".to_string()));
    assert!(hello_group.contains(&"d.txt".to_string()));

    // "world" and "goodbye" should each be singleton.
    let world_hash = simple_hash(b"world");
    let goodbye_hash = simple_hash(b"goodbye");
    assert_eq!(groups[&world_hash].len(), 1, "world should be singleton");
    assert_eq!(groups[&goodbye_hash].len(), 1, "goodbye should be singleton");

    // Planted case 2: verify empty file handling.
    let files2 = vec![
        FileEntry { name: "empty1.txt".to_string(), content: vec![] },
        FileEntry { name: "empty2.txt".to_string(), content: vec![] },
        FileEntry { name: "nonempty.txt".to_string(), content: b"text".to_vec() },
    ];

    let groups2 = group_by_content_hash(&files2);
    assert_eq!(groups2.len(), 2, "should have 2 unique hashes (1 for empty, 1 for nonempty)");

    let empty_hash = simple_hash(&[]);
    assert_eq!(groups2[&empty_hash].len(), 2, "both empty files should be grouped together");

    println!("file_dedup_hash: duplicates correctly grouped, singletons isolated, empty handled — PASS");
}
