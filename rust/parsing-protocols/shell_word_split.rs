#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct ShellSplitter;

impl ShellSplitter {
    fn split(input: &str) -> Result<Vec<String>, String> {
        let mut words = Vec::new();
        let mut current = String::new();
        let mut chars = input.chars().peekable();
        let mut in_single = false;
        let mut in_double = false;

        while let Some(ch) = chars.next() {
            match ch {
                '\'' if !in_double => {
                    if in_single {
                        in_single = false;
                    } else {
                        in_single = true;
                    }
                }
                '"' if !in_single => {
                    if in_double {
                        in_double = false;
                    } else {
                        in_double = true;
                    }
                }
                '\\' if !in_single => {
                    // Backslash escape: next char is literal
                    if let Some(next) = chars.next() {
                        current.push(next);
                    } else {
                        return Err("backslash at end of input".to_string());
                    }
                }
                ' ' | '\t' if !in_single && !in_double => {
                    if !current.is_empty() {
                        words.push(current.clone());
                        current.clear();
                    }
                }
                _ => current.push(ch),
            }
        }

        if in_single {
            return Err("unclosed single quote".to_string());
        }
        if in_double {
            return Err("unclosed double quote".to_string());
        }

        if !current.is_empty() {
            words.push(current);
        }

        Ok(words)
    }
}

fn main() {
    // Ground truth: simple split
    let cmd1 = "ls -la /tmp";
    let args1 = ShellSplitter::split(cmd1).unwrap();
    assert_eq!(args1, vec!["ls", "-la", "/tmp"]);

    // Ground truth: single-quoted string with spaces
    let cmd2 = "echo 'hello world'";
    let args2 = ShellSplitter::split(cmd2).unwrap();
    assert_eq!(args2, vec!["echo", "hello world"]);

    // Ground truth: double-quoted with space
    let cmd3 = "echo \"hello world\"";
    let args3 = ShellSplitter::split(cmd3).unwrap();
    assert_eq!(args3, vec!["echo", "hello world"]);

    // Ground truth: backslash escape (space becomes literal)
    let cmd4 = "echo hello\\ world";
    let args4 = ShellSplitter::split(cmd4).unwrap();
    assert_eq!(args4, vec!["echo", "hello world"]);

    // Adversarial: naive split on whitespace would fail with quoted strings
    let cmd5 = "foo \"arg with spaces\" bar";
    let args5 = ShellSplitter::split(cmd5).unwrap();
    assert_eq!(args5, vec!["foo", "arg with spaces", "bar"]);

    // Adversarial: unclosed single quote must error
    let cmd6 = "echo 'unclosed";
    assert!(ShellSplitter::split(cmd6).is_err());

    // Adversarial: unclosed double quote must error
    let cmd7 = "echo \"unclosed";
    assert!(ShellSplitter::split(cmd7).is_err());

    // Adversarial: single quote inside double quote is literal
    let cmd8 = "echo \"it's ok\"";
    let args8 = ShellSplitter::split(cmd8).unwrap();
    assert_eq!(args8, vec!["echo", "it's ok"]);

    // Adversarial: backslash at end of input is error
    let cmd9 = "foo bar\\";
    assert!(ShellSplitter::split(cmd9).is_err());

    println!("shell_word_split: PASS");
}
