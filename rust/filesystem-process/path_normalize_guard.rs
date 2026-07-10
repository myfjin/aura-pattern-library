#![forbid(unsafe_code)]
//! path_normalize_guard — normalize + traversal-escape guard; ../ escapes blocked.
//!
//! Core idea: normalize paths and prevent directory traversal attacks (e.g., ../../etc).
//! THE ONE LAW: plant a path with ../.. sequences, normalize it, assert it stays within
//! the base directory and traversal escapes are blocked.
//! When to use: web servers, file handlers, security boundaries.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn normalize_path(path: &str, base: &str) -> Result<String, String> {
    let mut parts = Vec::new();
    let mut depth = 0;

    for segment in path.split('/') {
        match segment {
            "" | "." => {
                // Empty or current directory; skip.
            }
            ".." => {
                // Parent directory.
                if depth > 0 {
                    parts.pop();
                    depth -= 1;
                } else {
                    return Err("traversal escape detected".to_string());
                }
            }
            _ => {
                // Regular segment.
                parts.push(segment);
                depth += 1;
            }
        }
    }

    let normalized = if parts.is_empty() {
        base.to_string()
    } else {
        format!("{}/{}", base, parts.join("/"))
    };
    Ok(normalized)
}

fn is_under_base(path: &str, base: &str) -> bool {
    path.starts_with(base)
}

fn main() {
    let base = "/home/user/data";

    // Planted case 1: normal path.
    let path1 = "subdir/file.txt";
    let norm1 = normalize_path(path1, base).expect("should normalize");
    assert_eq!(norm1, "/home/user/data/subdir/file.txt");
    assert!(is_under_base(&norm1, base), "should be under base");

    // Planted case 2: path with . and ..
    let path2 = "subdir/./file.txt";
    let norm2 = normalize_path(path2, base).expect("should normalize");
    assert_eq!(norm2, "/home/user/data/subdir/file.txt");

    // Planted case 3: path with valid .. (within bounds).
    let path3 = "subdir/deeper/../file.txt";
    let norm3 = normalize_path(path3, base).expect("should normalize");
    assert_eq!(norm3, "/home/user/data/subdir/file.txt");
    assert!(is_under_base(&norm3, base), "should still be under base");

    // THE ONE LAW: escape attempts are blocked.
    let escape1 = "../../etc/passwd";
    let result1 = normalize_path(escape1, base);
    assert!(result1.is_err(), "escape attempt should be rejected");

    let escape2 = "subdir/../../../../../../etc/passwd";
    let result2 = normalize_path(escape2, base);
    assert!(result2.is_err(), "deep escape attempt should be rejected");

    // Planted case 4: just enough .. to get back to base is OK (but then we're not under base anymore).
    let path4 = "subdir/..";
    let norm4 = normalize_path(path4, base).expect("should normalize");
    assert_eq!(norm4, "/home/user/data");

    // At the base boundary, further .. should fail.
    let escape3 = "subdir/../../..";
    let result3 = normalize_path(escape3, base);
    assert!(result3.is_err(), "going beyond base should fail");

    // Planted case 5: multiple segments and normalizations.
    let path5 = "a/b/c/d/../.././e/f/..";
    let norm5 = normalize_path(path5, base).expect("should normalize");
    // Trace: a/b/c/d, pop d -> a/b/c, pop c -> a/b, skip ".", add e -> a/b/e, add f -> a/b/e/f, pop f -> a/b/e.
    assert_eq!(norm5, "/home/user/data/a/b/e");
    assert!(is_under_base(&norm5, base), "should be under base");

    println!("path_normalize_guard: valid paths normalized, ../ escapes blocked — PASS");
}
