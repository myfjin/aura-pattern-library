#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct DelimiterBalancer;

impl DelimiterBalancer {
    fn is_balanced(input: &str) -> Result<bool, String> {
        let mut stack: Vec<char> = Vec::new();
        let mut in_string = false;
        let mut escape_next = false;
        let mut chars = input.chars();

        while let Some(ch) = chars.next() {
            if escape_next {
                escape_next = false;
                continue;
            }

            if ch == '\\' && in_string {
                escape_next = true;
                continue;
            }

            if ch == '"' {
                in_string = !in_string;
                continue;
            }

            if in_string {
                continue;
            }

            match ch {
                '(' | '[' | '{' => stack.push(ch),
                ')' => {
                    if stack.is_empty() || stack.pop() != Some('(') {
                        return Err("mismatched )".to_string());
                    }
                }
                ']' => {
                    if stack.is_empty() || stack.pop() != Some('[') {
                        return Err("mismatched ]".to_string());
                    }
                }
                '}' => {
                    if stack.is_empty() || stack.pop() != Some('{') {
                        return Err("mismatched }".to_string());
                    }
                }
                _ => {}
            }
        }

        if in_string {
            return Err("unclosed string".to_string());
        }

        if stack.is_empty() {
            Ok(true)
        } else {
            Err("unclosed delimiter".to_string())
        }
    }
}

fn main() {
    // Ground truth: balanced simple
    assert!(DelimiterBalancer::is_balanced("()").unwrap());
    assert!(DelimiterBalancer::is_balanced("[]").unwrap());
    assert!(DelimiterBalancer::is_balanced("{}").unwrap());

    // Ground truth: nested balanced
    assert!(DelimiterBalancer::is_balanced("({[]})").unwrap());

    // Ground truth: brackets inside string are ignored (naive counter would fail)
    assert!(DelimiterBalancer::is_balanced("(\")\")").unwrap());
    assert!(DelimiterBalancer::is_balanced("\"([{}])\"").unwrap());

    // Ground truth: escaped quote in string
    assert!(DelimiterBalancer::is_balanced("(\"\\\"quote\\\"\")").unwrap());

    // Adversarial: mismatched closing bracket
    assert!(DelimiterBalancer::is_balanced("(]").is_err());

    // Adversarial: unclosed opening bracket
    assert!(DelimiterBalancer::is_balanced("([]").is_err());

    // Adversarial: extra closing bracket
    assert!(DelimiterBalancer::is_balanced("())]").is_err());

    // Adversarial: unclosed string
    assert!(DelimiterBalancer::is_balanced("(\"unclosed").is_err());

    // Adversarial: string with escaped backslash followed by quote
    assert!(DelimiterBalancer::is_balanced("(\"test\\\\\")").unwrap());

    // Adversarial: closing bracket inside string doesn't close
    assert!(DelimiterBalancer::is_balanced("\"(unmatched closing) inside\"").unwrap());

    println!("balanced_delimiter_check: PASS");
}
