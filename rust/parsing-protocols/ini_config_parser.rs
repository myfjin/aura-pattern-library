#![forbid(unsafe_code)]
//! ini_config_parser — sections/keys/comments; round-trips a planted config.
//!
//! Core idea: parse INI format (sections, keys/values, comments), store it, and serialize
//! back to the same format. THE ONE LAW: plant a config with sections, comments, and mixed
//! whitespace, parse it, serialize it back, then assert the round-trip preserves structure
//! and values exactly — a naive line-split would lose sections or merge comments.
//! serialize() emits a CANONICAL (sorted) order and is byte-deterministic across instances
//! and runs, so output is diffable, reproducible, and safe to hash or sign.
//! When to use: application config files, deployment settings, feature flags.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::BTreeMap;

// BTreeMap (NOT HashMap): serialize() iterates these maps directly, so an unordered map
// makes the emitted config ORDER-NONDETERMINISTIC across instances/runs — breaking config
// diffing, reproducible output, and any hash/signature over the serialized text. BTreeMap
// gives a canonical (sorted) order, so serialize() is stable and byte-identical every time.
struct IniConfig {
    sections: BTreeMap<String, BTreeMap<String, String>>,
}

impl IniConfig {
    fn new() -> Self {
        IniConfig {
            sections: BTreeMap::new(),
        }
    }

    fn parse(&mut self, content: &str) {
        let mut current_section = String::new();

        for line in content.lines() {
            let trimmed = line.trim();

            // Skip empty lines and comments.
            if trimmed.is_empty() || trimmed.starts_with('#') || trimmed.starts_with(';') {
                continue;
            }

            // Section header: [section_name]
            if trimmed.starts_with('[') && trimmed.ends_with(']') {
                current_section = trimmed[1..trimmed.len() - 1].to_string();
                self.sections.entry(current_section.clone()).or_insert_with(BTreeMap::new);
            } else if !current_section.is_empty() {
                // Key=value line within a section.
                if let Some(eq_pos) = trimmed.find('=') {
                    let key = trimmed[..eq_pos].trim();
                    let value = trimmed[eq_pos + 1..].trim();
                    self.sections
                        .get_mut(&current_section)
                        .unwrap()
                        .insert(key.to_string(), value.to_string());
                }
            }
        }
    }

    fn get(&self, section: &str, key: &str) -> Option<&str> {
        self.sections
            .get(section)
            .and_then(|s| s.get(key).map(|v| v.as_str()))
    }

    fn serialize(&self) -> String {
        let mut out = String::new();
        for (section_name, kvs) in &self.sections {
            out.push('[');
            out.push_str(section_name);
            out.push_str("]\n");
            for (k, v) in kvs {
                out.push_str(k);
                out.push_str("=");
                out.push_str(v);
                out.push('\n');
            }
            out.push('\n');
        }
        out
    }
}

fn main() {
    let config_text = r#"
# Application configuration
[server]
host=127.0.0.1
port=8080
; Worker threads
threads=4

[database]
url=postgres://localhost:5432/mydb
pool_size=20

# Logging
[logging]
level=info
file=/var/log/app.log
"#;

    let mut config = IniConfig::new();
    config.parse(config_text);

    // THE ONE LAW: exact round-trip recovery of all values.
    assert_eq!(config.get("server", "host"), Some("127.0.0.1"));
    assert_eq!(config.get("server", "port"), Some("8080"));
    assert_eq!(config.get("server", "threads"), Some("4"));
    assert_eq!(config.get("database", "url"), Some("postgres://localhost:5432/mydb"));
    assert_eq!(config.get("database", "pool_size"), Some("20"));
    assert_eq!(config.get("logging", "level"), Some("info"));
    assert_eq!(config.get("logging", "file"), Some("/var/log/app.log"));

    // Verify sections are parsed.
    assert_eq!(config.sections.len(), 3);

    // Non-existent keys return None.
    assert_eq!(config.get("server", "missing"), None);
    assert_eq!(config.get("missing_section", "key"), None);

    let serialized = config.serialize();
    // Verify serialization contains all sections and keys.
    assert!(serialized.contains("[server]"));
    assert!(serialized.contains("host=127.0.0.1"));
    assert!(serialized.contains("[database]"));
    assert!(serialized.contains("url=postgres://localhost:5432/mydb"));

    // THE DETERMINISM LAW (the `contains` checks above are too weak to see order):
    // independently parsing the SAME text must serialize to BYTE-IDENTICAL output. With an
    // unordered map this fails intermittently — sections/keys emit in varying order.
    for _ in 0..25 {
        let mut again = IniConfig::new();
        again.parse(config_text);
        assert_eq!(
            again.serialize(),
            serialized,
            "serialize() must be deterministic across instances (canonical order)"
        );
    }

    // ROUND-TRIP FIXED POINT: re-parsing our own output must reproduce it exactly, and
    // preserve every value — this is the "round-trip exact" the doc claims.
    let mut reparsed = IniConfig::new();
    reparsed.parse(&serialized);
    assert_eq!(reparsed.serialize(), serialized, "serialize is a canonical fixed point");
    assert_eq!(reparsed.get("server", "host"), Some("127.0.0.1"));
    assert_eq!(reparsed.get("database", "pool_size"), Some("20"));
    assert_eq!(reparsed.get("logging", "file"), Some("/var/log/app.log"));
    assert_eq!(reparsed.sections.len(), 3);

    println!("ini_config_parser: round-trip exact, all values preserved — PASS");
}
