#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashMap;

// Scans a single line of whitespace-separated key=value pairs into a HashMap, where a
// value may be bare (ends at the next space/tab) or double-quoted to contain spaces,
// with backslash escaping any character inside the quotes.
// Use for logfmt-style lines where a naive split(' ') would wrongly break quoted values.
// Guarantees quote-aware tokenization: "hello world" stays one value and \" survives as a
// literal quote; an empty key or a key with no '=' returns Err rather than being dropped.
struct KvScanner;

impl KvScanner {
    fn scan_line(line: &str) -> Result<HashMap<String, String>, String> {
        let mut map = HashMap::new();
        let mut chars = line.chars().peekable();

        while chars.peek().is_some() {
            // Skip leading whitespace
            while chars.peek() == Some(&' ') || chars.peek() == Some(&'\t') {
                chars.next();
            }

            if chars.peek().is_none() {
                break;
            }

            // Parse key
            let mut key = String::new();
            while let Some(&ch) = chars.peek() {
                if ch == '=' {
                    break;
                }
                key.push(ch);
                chars.next();
            }

            key = key.trim().to_string();
            if key.is_empty() {
                return Err("empty key".to_string());
            }

            if chars.next() != Some('=') {
                return Err(format!("expected '=' after key '{}'", key));
            }

            // Parse value
            let value = if chars.peek() == Some(&'"') {
                chars.next(); // consume opening quote
                let mut val = String::new();
                let mut escaped = false;
                while let Some(ch) = chars.next() {
                    if escaped {
                        val.push(ch);
                        escaped = false;
                    } else if ch == '\\' {
                        escaped = true;
                    } else if ch == '"' {
                        break;
                    } else {
                        val.push(ch);
                    }
                }
                val
            } else {
                // Unquoted value: consume until space
                let mut val = String::new();
                while let Some(&ch) = chars.peek() {
                    if ch == ' ' || ch == '\t' {
                        break;
                    }
                    val.push(ch);
                    chars.next();
                }
                val
            };

            map.insert(key, value);
        }

        Ok(map)
    }
}

fn main() {
    // Ground truth: simple key=value
    let line1 = "host=localhost port=8080";
    let map1 = KvScanner::scan_line(line1).unwrap();
    assert_eq!(map1["host"], "localhost");
    assert_eq!(map1["port"], "8080");

    // Ground truth: quoted value with spaces (naive split(' ') FAILS here)
    let line2 = "msg=\"hello world\" level=info";
    let map2 = KvScanner::scan_line(line2).unwrap();
    assert_eq!(map2["msg"], "hello world");
    assert_eq!(map2["level"], "info");

    // Ground truth: multiple quoted values
    let line3 = "cmd=\"ls -la\" user=\"john doe\" status=ok";
    let map3 = KvScanner::scan_line(line3).unwrap();
    assert_eq!(map3["cmd"], "ls -la");
    assert_eq!(map3["user"], "john doe");
    assert_eq!(map3["status"], "ok");

    // Ground truth: escaped quote in quoted value
    let line4 = "msg=\"say \\\"hello\\\"\" type=quote";
    let map4 = KvScanner::scan_line(line4).unwrap();
    assert_eq!(map4["msg"], "say \"hello\"");
    assert_eq!(map4["type"], "quote");

    // Ground truth: mixed quoted and unquoted
    let line5 = "file=/path/to/file size=1024 note=\"a note with spaces\"";
    let map5 = KvScanner::scan_line(line5).unwrap();
    assert_eq!(map5["file"], "/path/to/file");
    assert_eq!(map5["size"], "1024");
    assert_eq!(map5["note"], "a note with spaces");

    // Adversarial: empty key must error
    let line6 = "=value";
    assert!(KvScanner::scan_line(line6).is_err());

    // Adversarial: missing '=' must error
    let line7 = "key value";
    assert!(KvScanner::scan_line(line7).is_err());

    // Adversarial: quoted value with spaces but naive approach splits it
    // (our parser gets it right, naive split on space would get it wrong)
    let line8 = "a=\"x y\" b=z";
    let map8 = KvScanner::scan_line(line8).unwrap();
    assert_eq!(map8["a"], "x y");
    assert_eq!(map8["b"], "z");
    // If we naively split on space, we'd get a=x which is wrong

    println!("key_value_line_scanner: PASS");
}
