#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// RFC-4180-style parser for a single CSV line with quoted-field support.
// Tracks an in-quotes flag: a field may open with '"', commas inside quotes are literal, and a
// doubled "" inside a quoted field decodes to one literal quote; commas outside quotes split fields.
// Use to split CSV rows correctly where a naive split(',') would break on embedded commas/quotes.
// Guarantees: preserves commas and newlines inside quoted fields and unescapes "" -> "; errors on a
// stray quote in the middle of an unquoted field and on an unclosed quote.
struct CsvParser;

impl CsvParser {
    fn parse_line(line: &str) -> Result<Vec<String>, String> {
        let mut fields = Vec::new();
        let mut current = String::new();
        let mut in_quotes = false;
        let mut chars = line.chars().peekable();

        while let Some(ch) = chars.next() {
            match ch {
                '"' => {
                    if in_quotes {
                        if chars.peek() == Some(&'"') {
                            // Escaped quote: "" -> "
                            current.push('"');
                            chars.next();
                        } else {
                            in_quotes = false;
                        }
                    } else if current.is_empty() {
                        in_quotes = true;
                    } else {
                        return Err("quote in middle of unquoted field".to_string());
                    }
                }
                ',' => {
                    if in_quotes {
                        current.push(',');
                    } else {
                        fields.push(current.clone());
                        current.clear();
                    }
                }
                _ => current.push(ch),
            }
        }

        if in_quotes {
            return Err("unclosed quote".to_string());
        }

        fields.push(current);
        Ok(fields)
    }
}

fn main() {
    // Ground truth: simple CSV line
    let line1 = "alice,bob,charlie";
    let fields1 = CsvParser::parse_line(line1).unwrap();
    assert_eq!(fields1, vec!["alice", "bob", "charlie"]);

    // Ground truth: quoted field with internal comma (naive split(',') FAILS here)
    let line2 = "alice,\"bob,charlie\",david";
    let fields2 = CsvParser::parse_line(line2).unwrap();
    assert_eq!(fields2, vec!["alice", "bob,charlie", "david"]);
    // If we naively split on ',', we'd get ["alice", "\"bob", "charlie\"", "david"] — wrong

    // Ground truth: quoted field with escaped quote
    let line3 = "alice,\"she said \"\"hello\"\"\",charlie";
    let fields3 = CsvParser::parse_line(line3).unwrap();
    assert_eq!(fields3, vec!["alice", "she said \"hello\"", "charlie"]);

    // Ground truth: empty fields
    let line4 = "alice,,charlie";
    let fields4 = CsvParser::parse_line(line4).unwrap();
    assert_eq!(fields4, vec!["alice", "", "charlie"]);

    // Adversarial: quote in middle of unquoted field must error
    let line5 = "alice,bo\"b,charlie";
    assert!(CsvParser::parse_line(line5).is_err());

    // Adversarial: unclosed quote must error
    let line6 = "alice,\"unclosed";
    assert!(CsvParser::parse_line(line6).is_err());

    // Adversarial: complex embedded newline scenario (we handle it as part of multi-char data)
    let line7 = "alice,\"multi\nline\",bob";
    let fields7 = CsvParser::parse_line(line7).unwrap();
    assert_eq!(fields7, vec!["alice", "multi\nline", "bob"]);

    println!("csv_quote_escape: PASS");
}
