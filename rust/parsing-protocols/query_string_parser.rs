#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct QueryParser;

impl QueryParser {
    fn parse(query: &str) -> Result<Vec<(String, String)>, String> {
        let mut pairs = Vec::new();

        if query.is_empty() {
            return Ok(pairs);
        }

        for pair in query.split('&') {
            if let Some(eq_pos) = pair.find('=') {
                let key = &pair[..eq_pos];
                let value = &pair[eq_pos + 1..];

                let decoded_key = Self::decode_percent(key)?;
                let decoded_value = Self::decode_percent(value)?;

                pairs.push((decoded_key, decoded_value));
            } else {
                return Err(format!("pair without '=': {}", pair));
            }
        }

        Ok(pairs)
    }

    fn decode_percent(encoded: &str) -> Result<String, String> {
        let mut result = String::new();
        let mut chars = encoded.chars();

        while let Some(ch) = chars.next() {
            if ch == '%' {
                // Expect two hex digits
                let mut hex = String::new();
                for _ in 0..2 {
                    if let Some(hc) = chars.next() {
                        hex.push(hc);
                    } else {
                        return Err("incomplete %XX escape".to_string());
                    }
                }
                let byte = u8::from_str_radix(&hex, 16)
                    .map_err(|_| format!("invalid hex in %%XX escape: {}", hex))?;
                result.push(byte as char);
            } else if ch == '+' {
                result.push(' ');
            } else {
                result.push(ch);
            }
        }

        Ok(result)
    }
}

fn main() {
    // Ground truth: simple query
    let q1 = "name=alice&age=30";
    let pairs1 = QueryParser::parse(q1).unwrap();
    assert_eq!(pairs1[0], ("name".to_string(), "alice".to_string()));
    assert_eq!(pairs1[1], ("age".to_string(), "30".to_string()));

    // Ground truth: percent-encoded value
    let q2 = "name=John%20Doe&city=New%20York";
    let pairs2 = QueryParser::parse(q2).unwrap();
    assert_eq!(pairs2[0], ("name".to_string(), "John Doe".to_string()));
    assert_eq!(pairs2[1], ("city".to_string(), "New York".to_string()));

    // Ground truth: plus as space
    let q3 = "search=hello+world";
    let pairs3 = QueryParser::parse(q3).unwrap();
    assert_eq!(pairs3[0], ("search".to_string(), "hello world".to_string()));

    // Ground truth: empty query
    let q4 = "";
    let pairs4 = QueryParser::parse(q4).unwrap();
    assert_eq!(pairs4.len(), 0);

    // Ground truth: special characters in percent-encoding
    let q5 = "data=%2F%3D%26";
    let pairs5 = QueryParser::parse(q5).unwrap();
    assert_eq!(pairs5[0], ("data".to_string(), "/=&".to_string()));

    // Adversarial: stray %X (only one hex digit) must error
    let q6 = "key=bad%X";
    assert!(QueryParser::parse(q6).is_err());

    // Adversarial: stray % at end must error
    let q7 = "key=value%";
    assert!(QueryParser::parse(q7).is_err());

    // Adversarial: pair without '=' must error
    let q8 = "key&other=value";
    assert!(QueryParser::parse(q8).is_err());

    // Adversarial: non-hex digits in %XX must error
    let q9 = "key=%ZZ";
    assert!(QueryParser::parse(q9).is_err());

    println!("query_string_parser: PASS");
}
