#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Parses an HTTP/1.x request line into (method, path, version) and header lines into
// (name, value) pairs, splitting on the first colon and trimming whitespace.
// Use when hand-rolling a minimal HTTP request reader without a full parser crate.
// Guarantees strict shape validation: the request line must have exactly three
// whitespace-separated parts and a version beginning "HTTP/", and every header line
// must contain a colon — malformed inputs (missing version, extra parts, colon-less
// header, empty line) return Err rather than being silently accepted.
struct HttpParser;

impl HttpParser {
    fn parse_request_line(line: &str) -> Result<(String, String, String), String> {
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() != 3 {
            return Err(format!("expected 3 parts, got {}", parts.len()));
        }

        let method = parts[0].to_string();
        let path = parts[1].to_string();
        let version = parts[2].to_string();

        // "strict shape validation" must actually validate the version NUMBER, not just the
        // "HTTP/" prefix — the shipped version accepted "HTTP/" (empty) and "HTTP/one.two"
        // (non-numeric) as valid (E012 validation-theater; snapshot at
        // http_request_line_parser.BROKEN.rs).
        let num = match version.strip_prefix("HTTP/") {
            Some(n) => n,
            None => return Err(format!("invalid HTTP version: {}", version)),
        };
        let valid_num = !num.is_empty()
            && num.split('.').all(|part| !part.is_empty() && part.chars().all(|c| c.is_ascii_digit()));
        if !valid_num {
            return Err(format!("invalid HTTP version number: {}", version));
        }

        Ok((method, path, version))
    }

    fn parse_headers(headers: &str) -> Result<Vec<(String, String)>, String> {
        let mut result = Vec::new();

        for line in headers.lines() {
            let line = line.trim();
            if line.is_empty() {
                continue;
            }

            if let Some(colon_pos) = line.find(':') {
                let name = line[..colon_pos].trim().to_string();
                let value = line[colon_pos + 1..].trim().to_string();
                if name.is_empty() {
                    return Err(format!("header with empty name: {}", line));
                }
                result.push((name, value));
            } else {
                return Err(format!("header without colon: {}", line));
            }
        }

        Ok(result)
    }
}

fn main() {
    // Ground truth: valid request line
    let req1 = "GET /index.html HTTP/1.1";
    let (method, path, version) = HttpParser::parse_request_line(req1).unwrap();
    assert_eq!(method, "GET");
    assert_eq!(path, "/index.html");
    assert_eq!(version, "HTTP/1.1");

    // Ground truth: POST with path
    let req2 = "POST /api/data HTTP/1.1";
    let (m2, p2, v2) = HttpParser::parse_request_line(req2).unwrap();
    assert_eq!(m2, "POST");
    assert_eq!(p2, "/api/data");
    assert_eq!(v2, "HTTP/1.1");

    // Ground truth: headers
    let headers1 = "Host: example.com\nContent-Type: application/json\nContent-Length: 42";
    let hdrs1 = HttpParser::parse_headers(headers1).unwrap();
    assert_eq!(hdrs1[0], ("Host".to_string(), "example.com".to_string()));
    assert_eq!(hdrs1[1], ("Content-Type".to_string(), "application/json".to_string()));

    // Adversarial: request line missing version
    let req3 = "GET /path";
    assert!(HttpParser::parse_request_line(req3).is_err());

    // Adversarial: invalid HTTP version
    let req4 = "GET /path HTTPS/1.1";
    assert!(HttpParser::parse_request_line(req4).is_err());

    // Adversarial: header without colon
    let headers2 = "Valid-Header: ok\nInvalidHeader";
    assert!(HttpParser::parse_headers(headers2).is_err());

    // Adversarial: request line with too many parts
    let req5 = "GET /path HTTP/1.1 EXTRA";
    assert!(HttpParser::parse_request_line(req5).is_err());

    // Adversarial: empty request line
    let req6 = "";
    assert!(HttpParser::parse_request_line(req6).is_err());

    println!("http_request_line_parser: PASS");
}
