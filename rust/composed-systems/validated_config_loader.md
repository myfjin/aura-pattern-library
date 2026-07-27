# validated config loader

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(text: &str) → Option<HashMap<String, String>>`

## What it does

composes: parse-ini-kv-config + validate-schema-types + checksum-verify + reject-violations

## Guarantee

When it runs, validated config loader guarantees assert_eq!(config.port, 8080, "Port parsed correctly"); assert_eq!(config.timeout, 30, "Timeout parsed correctly"); assert_eq!(config.host, "localhost", "Host parsed correctly") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(config.port, 8080, "Port parsed correctly")`
- `assert_eq!(config.timeout, 30, "Timeout parsed correctly")`
- `assert_eq!(config.host, "localhost", "Host parsed correctly")`
- `assert_eq!(compute_config_checksum(&reloaded), stored_checksum, "untampered config verifies")`
- `assert_ne!(compute_config_checksum(&tampered), stored_checksum, "tampered config must fail checksum verification")`
- `assert!(result.is_none(), "Invalid config rejected: {}", invalid_text)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
