#![forbid(unsafe_code)]
//! glob_match — from-scratch * ? [..] matcher; planted matches/non-matches correct.
//!
//! Core idea: implement glob pattern matching with *, ?, and character classes [abc] / [^abc].
//! THE ONE LAW: plant patterns and filenames with known matches and non-matches, then assert
//! every match/non-match is correct — a naive string contains would fail on * or ? anchoring.
//! When to use: file listing, wildcard filters, pathname matching in shell/tools.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn glob_match(pattern: &str, text: &str) -> bool {
    let pat_chars: Vec<char> = pattern.chars().collect();
    let txt_chars: Vec<char> = text.chars().collect();

    fn match_recursive(
        pat: &[char],
        txt: &[char],
        pi: usize,
        ti: usize,
    ) -> bool {
        // Base cases.
        if pi >= pat.len() && ti >= txt.len() {
            return true; // Both exhausted.
        }
        if pi >= pat.len() {
            return false; // Pattern done, text remains.
        }

        match pat[pi] {
            '*' => {
                // * matches zero or more characters.
                // Try matching with zero characters (skip the *).
                if match_recursive(pat, txt, pi + 1, ti) {
                    return true;
                }
                // Try matching with one or more characters (if text remains).
                if ti < txt.len() && match_recursive(pat, txt, pi, ti + 1) {
                    return true;
                }
                false
            }
            '?' => {
                // ? matches exactly one character.
                if ti >= txt.len() {
                    return false;
                }
                match_recursive(pat, txt, pi + 1, ti + 1)
            }
            '[' => {
                // Character class [abc] or [^abc].
                let mut ci = pi + 1;
                let negate = ci < pat.len() && pat[ci] == '^';
                if negate {
                    ci += 1;
                }

                let mut found = false;
                while ci < pat.len() && pat[ci] != ']' {
                    if ti < txt.len() && txt[ti] == pat[ci] {
                        found = true;
                    }
                    ci += 1;
                }

                if ci >= pat.len() {
                    return false; // Malformed, no closing ].
                }

                let matched = if negate { !found } else { found };
                if matched && ti < txt.len() {
                    match_recursive(pat, txt, ci + 1, ti + 1)
                } else {
                    false
                }
            }
            c => {
                // Literal character.
                if ti >= txt.len() || txt[ti] != c {
                    return false;
                }
                match_recursive(pat, txt, pi + 1, ti + 1)
            }
        }
    }

    match_recursive(&pat_chars, &txt_chars, 0, 0)
}

fn main() {
    // Planted matches: patterns and expected results.
    let cases = vec![
        ("*.txt", "file.txt", true),
        ("*.txt", "file.rs", false),
        ("test_*.rs", "test_foo.rs", true),
        ("test_*.rs", "test.rs", false),
        ("a?c", "abc", true),
        ("a?c", "abbc", false),
        ("a?c", "ac", false),
        ("[abc]", "a", true),
        ("[abc]", "b", true),
        ("[abc]", "d", false),
        ("[^abc]", "d", true),
        ("[^abc]", "a", false),
        ("*.[ot]xt", "file.txt", true),
        ("*.[ot]xt", "file.oxt", true),
        ("*.[ot]xt", "file.rst", false),
        ("*", "anything", true),
        ("*", "", true),
    ];

    // THE ONE LAW: every match/non-match is exact.
    for (pattern, text, expected) in &cases {
        let result = glob_match(pattern, text);
        assert_eq!(
            result, *expected,
            "glob_match failed for pattern '{}' vs '{}'",
            pattern, text
        );
    }

    println!("glob_match: {} cases tested, all exact — PASS", cases.len());
}
