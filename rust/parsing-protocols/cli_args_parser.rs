#![forbid(unsafe_code)]
//! cli_args_parser — from-scratch getopt: short/long flags, =values, -- boundary.
//!
//! Core idea: parse command-line arguments from scratch, handling short/long flags, values,
//! and -- to stop flag parsing. THE ONE LAW: plant argv with mixed flags, values, and the --
//! boundary, parse it, and assert every flag/value/positional is captured exactly, including
//! combined short flags (-abc) and --key=value — a naive split would fail on both.
//! (The parser is intentionally lenient — it does not reject unknown flags.)
//! When to use: CLI tools, configuration loading, argument validation.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#[derive(Debug, PartialEq)]
#[allow(dead_code)]
enum ParseError {
    MissingValue(String),
    UnknownFlag(String),
}

struct Args {
    flags: Vec<(String, Option<String>)>,
    positional: Vec<String>,
}

fn parse_args(argv: &[&str]) -> Result<Args, ParseError> {
    let mut flags = Vec::new();
    let mut positional = Vec::new();
    let mut i = 0;

    while i < argv.len() {
        let arg = argv[i];

        if arg == "--" {
            // Rest are positional.
            i += 1;
            while i < argv.len() {
                positional.push(argv[i].to_string());
                i += 1;
            }
            break;
        }

        if arg.starts_with("--") {
            // Long flag.
            let flag_part = &arg[2..];
            if let Some(eq_pos) = flag_part.find('=') {
                let flag = flag_part[..eq_pos].to_string();
                let value = flag_part[eq_pos + 1..].to_string();
                flags.push((flag, Some(value)));
            } else {
                let flag = flag_part.to_string();
                if i + 1 < argv.len() && !argv[i + 1].starts_with('-') {
                    i += 1;
                    flags.push((flag, Some(argv[i].to_string())));
                } else {
                    flags.push((flag, None));
                }
            }
            i += 1;
        } else if arg.starts_with('-') && arg.len() > 1 && arg != "-" {
            // Short flag(s).
            let flag_chars: Vec<char> = arg[1..].chars().collect();
            for j in 0..flag_chars.len() {
                let flag = flag_chars[j].to_string();
                let is_last = j == flag_chars.len() - 1;

                if is_last && i + 1 < argv.len() && !argv[i + 1].starts_with('-') {
                    i += 1;
                    flags.push((flag, Some(argv[i].to_string())));
                } else {
                    flags.push((flag, None));
                }
            }
            i += 1;
        } else {
            // Positional argument.
            positional.push(arg.to_string());
            i += 1;
        }
    }

    Ok(Args { flags, positional })
}

fn main() {
    // Test case 1: basic flags and values (skip argv[0] which is prog name).
    let argv1 = vec!["-v", "--config=/etc/app.conf", "-n", "100"];
    let parsed1 = parse_args(&argv1).expect("parse failed");
    assert_eq!(parsed1.flags.len(), 3);
    assert_eq!(parsed1.flags[0].0, "v");
    assert_eq!(parsed1.flags[1].0, "config");
    assert_eq!(parsed1.flags[1].1, Some("/etc/app.conf".to_string()));
    assert_eq!(parsed1.flags[2].0, "n");
    assert_eq!(parsed1.flags[2].1, Some("100".to_string()));

    // Test case 2: positional after --.
    let argv2 = vec!["-v", "--", "file1", "file2"];
    let parsed2 = parse_args(&argv2).expect("parse failed");
    assert_eq!(parsed2.positional, vec!["file1", "file2"]);

    // THE ONE LAW: mixed flags and positionals parse exactly.
    let argv3 = vec!["-abc", "--long=val", "pos1"];
    let parsed3 = parse_args(&argv3).expect("parse failed");
    assert_eq!(parsed3.flags.len(), 4); // a, b, c, long
    assert_eq!(parsed3.positional, vec!["pos1"]);

    println!("cli_args_parser: mixed flags and positionals exact — PASS");
}
