#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#[derive(Debug, PartialEq)]
struct Authority {
    userinfo: Option<String>,
    host: String,
    port: Option<u16>,
}

fn parse_authority(auth: &str) -> Result<Authority, &'static str> {
    let mut userinfo = None;
    let mut rest = auth;

    // Check for userinfo
    if let Some(at_pos) = auth.find('@') {
        userinfo = Some(auth[..at_pos].to_string());
        rest = &auth[at_pos + 1..];
    }

    // Split host and port
    let (host, port_str) = if let Some(colon_pos) = rest.rfind(':') {
        (&rest[..colon_pos], Some(&rest[colon_pos + 1..]))
    } else {
        (rest, None)
    };

    if host.is_empty() {
        return Err("Empty host");
    }

    let port = if let Some(ps) = port_str {
        if ps.is_empty() {
            return Err("Empty port");
        }
        match ps.parse::<u32>() {
            Ok(p) if p > 65535 => return Err("Port overflow"),
            Ok(p) => Some(p as u16),
            Err(_) => return Err("Invalid port"),
        }
    } else {
        None
    };

    Ok(Authority {
        userinfo,
        host: host.to_string(),
        port,
    })
}

fn main() {
    // Test 1: Simple host
    let auth = parse_authority("example.com").unwrap();
    assert_eq!(auth.host, "example.com");
    assert_eq!(auth.userinfo, None);
    assert_eq!(auth.port, None);

    // Test 2: Host with port
    let auth = parse_authority("example.com:8080").unwrap();
    assert_eq!(auth.host, "example.com");
    assert_eq!(auth.port, Some(8080));

    // Test 3: Userinfo + host + port
    let auth = parse_authority("user:pass@example.com:443").unwrap();
    assert_eq!(auth.userinfo, Some("user:pass".to_string()));
    assert_eq!(auth.host, "example.com");
    assert_eq!(auth.port, Some(443));

    // Test 4: Port overflow
    assert!(parse_authority("example.com:99999").is_err(), "Port > 65535 should fail");

    // Test 5: Invalid port (non-numeric)
    assert!(parse_authority("example.com:abc").is_err(), "Non-numeric port should fail");

    // Test 6: Empty port
    assert!(parse_authority("example.com:").is_err(), "Empty port should fail");

    // Test 7: Empty host
    assert!(parse_authority(":8080").is_err(), "Empty host should fail");

    // Test 8: Boundary port values
    let auth = parse_authority("example.com:1").unwrap();
    assert_eq!(auth.port, Some(1));

    let auth = parse_authority("example.com:65535").unwrap();
    assert_eq!(auth.port, Some(65535));

    // Test 9: Exact parsing
    let auth = parse_authority("admin@server.local:3000").unwrap();
    assert_eq!(auth.userinfo, Some("admin".to_string()));
    assert_eq!(auth.host, "server.local");
    assert_eq!(auth.port, Some(3000));

    println!("url_authority_parser: PASS");
}
