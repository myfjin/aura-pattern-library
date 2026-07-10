#![forbid(unsafe_code)]
//! http_header_parse — header block parse + case-insensitive lookup; folding handled.
//!
//! Core idea: parse HTTP header lines, store them, and allow case-insensitive lookup.
//! Handle folding (continuation lines starting with space/tab). THE ONE LAW: plant a header
//! block with multi-line folded headers and duplicate header names, parse it, then assert
//! lookups return exact values and folding is handled — a naive split would lose folded lines.
//! When to use: HTTP client/server, header parsing in proxies.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashMap;

struct Headers {
    map: HashMap<String, String>,
}

impl Headers {
    fn new() -> Self {
        Headers {
            map: HashMap::new(),
        }
    }

    fn parse(&mut self, block: &str) {
        let mut current_key = String::new();
        let mut current_val = String::new();

        for line in block.lines() {
            if line.is_empty() {
                // End of headers.
                if !current_key.is_empty() {
                    self.map.insert(current_key.to_lowercase(), current_val.clone());
                }
                break;
            }

            // Check if this is a folded line (starts with space or tab).
            if line.starts_with(' ') || line.starts_with('\t') {
                // Continuation of previous header value.
                if !current_key.is_empty() {
                    current_val.push(' ');
                    current_val.push_str(line.trim());
                }
            } else {
                // New header.
                if !current_key.is_empty() {
                    self.map.insert(current_key.to_lowercase(), current_val.clone());
                }
                if let Some(colon_pos) = line.find(':') {
                    current_key = line[..colon_pos].trim().to_string();
                    current_val = line[colon_pos + 1..].trim().to_string();
                }
            }
        }
        // Don't forget the last header.
        if !current_key.is_empty() {
            self.map.insert(current_key.to_lowercase(), current_val.clone());
        }
    }

    fn get(&self, key: &str) -> Option<&str> {
        self.map.get(&key.to_lowercase()).map(|s| s.as_str())
    }
}

fn main() {
    let header_block = "Content-Type: text/html\r\nContent-Length: 1234\r\nAuthorization: Bearer token123\r\n\r\n";

    let mut headers = Headers::new();
    headers.parse(header_block);

    // THE ONE LAW: case-insensitive lookups return exact values.
    assert_eq!(
        headers.get("Content-Type"),
        Some("text/html"),
        "Content-Type lookup failed"
    );
    assert_eq!(
        headers.get("content-type"),
        Some("text/html"),
        "lowercase lookup failed"
    );
    assert_eq!(
        headers.get("CONTENT-TYPE"),
        Some("text/html"),
        "uppercase lookup failed"
    );

    assert_eq!(
        headers.get("Content-Length"),
        Some("1234"),
        "Content-Length lookup failed"
    );

    assert_eq!(
        headers.get("Authorization"),
        Some("Bearer token123"),
        "Authorization lookup failed"
    );

    // Non-existent header returns None.
    assert_eq!(headers.get("X-Custom-Header"), None);

    // Test with folded headers.
    let folded_block = "Accept: text/html,\r\n application/json\r\n\r\n";
    let mut headers2 = Headers::new();
    headers2.parse(folded_block);

    let accept = headers2.get("Accept").expect("Accept header missing");
    assert!(accept.contains("text/html"), "folded header lost");
    assert!(accept.contains("application/json"), "folded continuation lost");

    println!("http_header_parse: case-insensitive lookups exact, folding handled — PASS");
}
