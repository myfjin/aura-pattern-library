#![forbid(unsafe_code)]
//! dir_size_aggregate — recursive size sum over a synthetic tree; equals brute force.
//!
//! Core idea: walk a directory tree and sum file sizes. THE ONE LAW: create a synthetic
//! tree with known structure and sizes, compute total size via recursion, then assert
//! it matches a brute-force sum of all files. A missed file or double-count would fail.
//! When to use: disk usage analysis, quota checking, storage reporting.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct DirNode {
    size: u64, // Size if it's a file; 0 if directory.
    children: Vec<DirNode>,
}

impl DirNode {
    fn total_size(&self) -> u64 {
        let mut sum = self.size;
        for child in &self.children {
            sum += child.total_size();
        }
        sum
    }

    fn file_count(&self) -> usize {
        let mut count = if self.size > 0 { 1 } else { 0 };
        for child in &self.children {
            count += child.file_count();
        }
        count
    }

    fn flatten_files(&self) -> Vec<u64> {
        let mut files = Vec::new();
        if self.size > 0 {
            files.push(self.size);
        }
        for child in &self.children {
            files.extend(child.flatten_files());
        }
        files
    }
}

fn main() {
    // Planted case 1: simple tree structure.
    //   root/
    //     file1.txt (100 bytes)
    //     file2.txt (200 bytes)
    //     subdir/
    //       file3.txt (50 bytes)
    //       nested/
    //         file4.txt (75 bytes)
    let root = DirNode {
        size: 0,
        children: vec![
            DirNode { size: 100, children: vec![] },
            DirNode { size: 200, children: vec![] },
            DirNode {
                size: 0,
                children: vec![
                    DirNode { size: 50, children: vec![] },
                    DirNode {
                        size: 0,
                        children: vec![
                            DirNode { size: 75, children: vec![] },
                        ],
                    },
                ],
            },
        ],
    };

    // THE ONE LAW: recursive total must match brute-force sum.
    let recursive_total = root.total_size();
    let files = root.flatten_files();
    let brute_force_total: u64 = files.iter().sum();

    assert_eq!(recursive_total, brute_force_total, "recursive total must match brute force");
    assert_eq!(recursive_total, 100 + 200 + 50 + 75, "total should be 425 bytes");

    // Verify file count.
    assert_eq!(root.file_count(), 4, "should count all 4 files");

    // Planted case 2: empty directories.
    let sparse = DirNode {
        size: 0,
        children: vec![
            DirNode { size: 0, children: vec![] },
            DirNode { size: 999, children: vec![] },
            DirNode {
                size: 0,
                children: vec![
                    DirNode { size: 0, children: vec![] },
                ],
            },
        ],
    };

    let sparse_recursive = sparse.total_size();
    let sparse_files = sparse.flatten_files();
    let sparse_brute = sparse_files.iter().sum::<u64>();

    assert_eq!(sparse_recursive, sparse_brute, "empty dirs should not affect total");
    assert_eq!(sparse_recursive, 999, "only one file with 999 bytes");

    // Planted case 3: single file (no directories).
    let single = DirNode {
        size: 12345,
        children: vec![],
    };

    assert_eq!(single.total_size(), 12345);
    assert_eq!(single.file_count(), 1);

    // Planted case 4: many files in one directory.
    let mut many_files = vec![];
    for i in 0..100 {
        many_files.push(DirNode {
            size: (i + 1) as u64,
            children: vec![],
        });
    }
    let many = DirNode {
        size: 0,
        children: many_files,
    };

    let many_recursive = many.total_size();
    let many_expected: u64 = (1..=100).sum();
    assert_eq!(many_recursive, many_expected, "sum of 1..100 should be 5050");

    println!("dir_size_aggregate: recursive total matches brute force, empty dirs handled — PASS");
}
