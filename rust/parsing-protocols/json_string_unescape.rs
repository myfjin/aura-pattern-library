#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct JsonString;

impl JsonString {
    fn unescape(input: &str) -> Result<String, String> {
        let mut output = String::new();
        let mut chars = input.chars();

        while let Some(ch) = chars.next() {
            if ch == '\\' {
                if let Some(next) = chars.next() {
                    match next {
                        'n' => output.push('\n'),
                        't' => output.push('\t'),
                        'r' => output.push('\r'),
                        '\\' => output.push('\\'),
                        '"' => output.push('"'),
                        'b' => output.push('\u{0008}'),
                        'f' => output.push('\u{000C}'),
                        '/' => output.push('/'),
                        'u' => {
                            // \uXXXX - collect 4 hex digits
                            let mut hex = String::new();
                            for _ in 0..4 {
                                if let Some(hc) = chars.next() {
                                    hex.push(hc);
                                } else {
                                    return Err("incomplete \\u escape".to_string());
                                }
                            }
                            let code = u32::from_str_radix(&hex, 16)
                                .map_err(|_| format!("invalid hex in \\u escape: {}", hex))?;
                            let c = char::from_u32(code)
                                .ok_or_else(|| format!("invalid unicode codepoint: {}", code))?;
                            output.push(c);
                        }
                        _ => {
                            return Err(format!("invalid escape sequence: \\{}", next));
                        }
                    }
                } else {
                    return Err("backslash at end of string".to_string());
                }
            } else {
                output.push(ch);
            }
        }

        Ok(output)
    }
}

fn main() {
    // Ground truth: simple text
    let s1 = "hello world";
    assert_eq!(JsonString::unescape(s1).unwrap(), "hello world");

    // Ground truth: \n escape
    let s2 = "line1\\nline2";
    assert_eq!(JsonString::unescape(s2).unwrap(), "line1\nline2");

    // Ground truth: \t escape
    let s3 = "col1\\tcol2";
    assert_eq!(JsonString::unescape(s3).unwrap(), "col1\tcol2");

    // Ground truth: \" escape
    let s4 = "say \\\"hello\\\"";
    assert_eq!(JsonString::unescape(s4).unwrap(), "say \"hello\"");

    // Ground truth: \\ escape
    let s5 = "path\\\\to\\\\file";
    assert_eq!(JsonString::unescape(s5).unwrap(), "path\\to\\file");

    // Ground truth: \uXXXX unicode
    let s6 = "emoji\\u0041";
    assert_eq!(JsonString::unescape(s6).unwrap(), "emojiA");

    // Adversarial: invalid escape sequence must error
    let s7 = "bad\\xescape";
    assert!(JsonString::unescape(s7).is_err());

    // Adversarial: incomplete \u escape (< 4 digits)
    let s8 = "short\\u00";
    assert!(JsonString::unescape(s8).is_err());

    // Adversarial: backslash at end
    let s9 = "ending\\";
    assert!(JsonString::unescape(s9).is_err());

    // Adversarial: non-hex digits in \u escape
    let s10 = "bad\\uXYZA";
    assert!(JsonString::unescape(s10).is_err());

    // Adversarial: valid but surrogate pair (simplified check: invalid codepoint)
    let s11 = "invalid\\uD800"; // UTF-16 surrogate, not a valid standalone codepoint
    assert!(JsonString::unescape(s11).is_err());

    println!("json_string_unescape: PASS");
}
