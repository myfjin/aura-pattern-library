#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct EscapeCodec;

impl EscapeCodec {
    fn encode(data: &[u8]) -> String {
        let mut result = String::new();
        for &byte in data {
            match byte {
                b'\\' => result.push_str("\\\\"),
                b'\n' => result.push_str("\\n"),
                b'\r' => result.push_str("\\r"),
                b'\t' => result.push_str("\\t"),
                b'\0' => result.push_str("\\0"),
                32..=126 => result.push(byte as char), // printable ASCII
                _ => {
                    // Non-printable: hex escape \xHH
                    result.push_str(&format!("\\x{:02x}", byte));
                }
            }
        }
        result
    }

    fn decode(encoded: &str) -> Result<Vec<u8>, String> {
        let mut result = Vec::new();
        let mut chars = encoded.chars();

        while let Some(ch) = chars.next() {
            if ch == '\\' {
                if let Some(next) = chars.next() {
                    match next {
                        '\\' => result.push(b'\\'),
                        'n' => result.push(b'\n'),
                        'r' => result.push(b'\r'),
                        't' => result.push(b'\t'),
                        '0' => result.push(b'\0'),
                        'x' => {
                            // \xHH
                            let mut hex = String::new();
                            for _ in 0..2 {
                                if let Some(hc) = chars.next() {
                                    hex.push(hc);
                                } else {
                                    return Err("incomplete \\x escape".to_string());
                                }
                            }
                            let byte = u8::from_str_radix(&hex, 16)
                                .map_err(|_| format!("invalid hex in \\x escape: {}", hex))?;
                            result.push(byte);
                        }
                        _ => {
                            return Err(format!("invalid escape sequence: \\{}", next));
                        }
                    }
                } else {
                    return Err("backslash at end of string".to_string());
                }
            } else {
                result.push(ch as u8);
            }
        }

        Ok(result)
    }
}

fn main() {
    // Ground truth: simple ASCII roundtrip
    let original1 = b"hello";
    let encoded1 = EscapeCodec::encode(original1);
    let decoded1 = EscapeCodec::decode(&encoded1).unwrap();
    assert_eq!(decoded1, original1);

    // Ground truth: with special characters
    let original2 = "line1\nline2\t".as_bytes();
    let encoded2 = EscapeCodec::encode(original2);
    assert_eq!(encoded2, "line1\\nline2\\t");
    let decoded2 = EscapeCodec::decode(&encoded2).unwrap();
    assert_eq!(decoded2, original2);

    // Ground truth: null byte
    let original3 = b"before\x00after";
    let encoded3 = EscapeCodec::encode(original3);
    assert_eq!(encoded3, "before\\0after");
    let decoded3 = EscapeCodec::decode(&encoded3).unwrap();
    assert_eq!(decoded3, original3);

    // Adversarial: embedded control bytes must survive roundtrip
    let original4 = vec![0x01, 0x02, 0x03, b'x', 0xFF, 0xFE];
    let encoded4 = EscapeCodec::encode(&original4);
    let decoded4 = EscapeCodec::decode(&encoded4).unwrap();
    assert_eq!(decoded4, original4, "control bytes didn't roundtrip");

    // Adversarial: backslash in data must not cause escaping confusion
    let original5 = "path\\to\\file".as_bytes();
    let encoded5 = EscapeCodec::encode(original5);
    let decoded5 = EscapeCodec::decode(&encoded5).unwrap();
    assert_eq!(decoded5, original5);

    // Adversarial: decode error on incomplete hex escape
    assert!(EscapeCodec::decode("bad\\x0").is_err());

    // Adversarial: decode error on backslash at end
    assert!(EscapeCodec::decode("ending\\").is_err());

    // Adversarial: all possible byte values
    let original6: Vec<u8> = (0..=255).collect();
    let encoded6 = EscapeCodec::encode(&original6);
    let decoded6 = EscapeCodec::decode(&encoded6).unwrap();
    assert_eq!(decoded6, original6, "roundtrip failed for all bytes");

    println!("backslash_escape_codec: PASS");
}
