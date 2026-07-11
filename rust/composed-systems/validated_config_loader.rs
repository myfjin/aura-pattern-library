#![forbid(unsafe_code)]
// composes: parse-ini-kv-config + validate-schema-types + checksum-verify + reject-violations

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashMap;

#[derive(Clone, Debug)]
struct Config {
    port: usize,
    timeout: usize,
    host: String,
}

fn parse_config(text: &str) -> Option<HashMap<String, String>> {
    let mut config = HashMap::new();
    for line in text.lines() {
        if let Some(eq_pos) = line.find('=') {
            let key = line[..eq_pos].trim().to_string();
            let value = line[eq_pos+1..].trim().to_string();
            config.insert(key, value);
        }
    }
    Some(config)
}

fn validate_config(raw: &HashMap<String, String>) -> Option<Config> {
    // Stage 1: Parse KV
    // Stage 2: Validate schema/types
    let port: usize = raw.get("port")?.parse().ok()?;
    let timeout: usize = raw.get("timeout")?.parse().ok()?;
    let host = raw.get("host")?.clone();

    // Validation rules: port in range, timeout positive, host not empty
    if port == 0 || port > 65535 { return None; }
    if timeout == 0 { return None; }
    if host.is_empty() { return None; }

    Some(Config { port, timeout, host })
}

fn compute_config_checksum(config: &Config) -> u32 {
    let mut sum: u32 = 0;
    for &b in config.port.to_string().as_bytes() {
        sum = sum.wrapping_add(b as u32);
    }
    for &b in config.timeout.to_string().as_bytes() {
        sum = sum.wrapping_add(b as u32);
    }
    for &b in config.host.as_bytes() {
        sum = sum.wrapping_add(b as u32);
    }
    sum
}

fn main() {
    // Stage 1: Parse valid config
    let valid_text = "port=8080\ntimeout=30\nhost=localhost";
    let raw = parse_config(valid_text).expect("parse failed");

    // Stage 2: Validate and create config
    let config = validate_config(&raw).expect("validation failed");
    assert_eq!(config.port, 8080, "Port parsed correctly");
    assert_eq!(config.timeout, 30, "Timeout parsed correctly");
    assert_eq!(config.host, "localhost", "Host parsed correctly");

    // Stage 3: Checksum-verify against a STORED checksum, and prove tampering is caught.
    let stored_checksum = compute_config_checksum(&config);
    // A faithful reload recomputes the same checksum → verification passes.
    let reloaded = validate_config(&raw).expect("reload failed");
    assert_eq!(compute_config_checksum(&reloaded), stored_checksum, "untampered config verifies");
    // Now tamper the loaded config and re-verify: the checksum MUST mismatch (tamper detected).
    let mut tampered = config.clone();
    tampered.port = 9090; // silently change a field
    assert_ne!(
        compute_config_checksum(&tampered),
        stored_checksum,
        "tampered config must fail checksum verification"
    );

    // Stage 4: Reject violations
    let invalid_cases = vec![
        "port=99999\ntimeout=30\nhost=localhost",  // Port out of range
        "port=8080\ntimeout=0\nhost=localhost",     // Timeout is 0
        "port=8080\ntimeout=30\nhost=",            // Host empty
        "port=abc\ntimeout=30\nhost=localhost",     // Port not a number
    ];

    for invalid_text in invalid_cases {
        let raw = parse_config(invalid_text).expect("parse should work");
        let result = validate_config(&raw);
        assert!(result.is_none(), "Invalid config rejected: {}", invalid_text);
    }

    println!("validated_config_loader: PASS");
}
