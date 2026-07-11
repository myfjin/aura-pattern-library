#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#[derive(Clone, Debug)]
struct CidrRule {
    ip: u32,
    mask_bits: u32,
    allow: bool,
}

struct CidrAllowlist {
    rules: Vec<CidrRule>,
}

impl CidrAllowlist {
    fn new() -> Self {
        Self {
            rules: Vec::new(),
        }
    }

    fn add_rule(&mut self, ip: u32, mask_bits: u32, allow: bool) {
        self.rules.push(CidrRule { ip, mask_bits, allow });
    }

    fn matches(&self, ip: u32) -> bool {
        let mut best_match: Option<(u32, bool)> = None;

        for rule in &self.rules {
            let mask = if rule.mask_bits == 0 {
                0u32
            } else {
                !0u32 << (32 - rule.mask_bits)
            };

            if (ip & mask) == (rule.ip & mask) {
                if best_match.is_none()
                    || rule.mask_bits > best_match.unwrap().0
                {
                    best_match = Some((rule.mask_bits, rule.allow));
                }
            }
        }

        best_match.map(|(_, allow)| allow).unwrap_or(false)
    }
}

fn main() {
    // Test 1: Simple allow rule
    let mut acl = CidrAllowlist::new();
    acl.add_rule(0xC0A80000, 24, true); // 192.168.0.0/24 allow
    assert!(acl.matches(0xC0A80001), "192.168.0.1 should match");
    assert!(acl.matches(0xC0A800FF), "192.168.0.255 should match");
    assert!(!acl.matches(0xC0A80100), "192.168.1.0 should not match");

    // Test 2: Deny rule
    let mut acl2 = CidrAllowlist::new();
    acl2.add_rule(0xC0A80000, 24, false); // 192.168.0.0/24 deny
    assert!(!acl2.matches(0xC0A80001), "Should be denied");

    // Test 3: Longest prefix wins
    let mut acl3 = CidrAllowlist::new();
    acl3.add_rule(0xC0A80000, 16, true);  // 192.168.0.0/16 allow
    acl3.add_rule(0xC0A80000, 24, false); // 192.168.0.0/24 deny
    assert!(!acl3.matches(0xC0A80050), "Most specific (/24 deny) should win");
    assert!(acl3.matches(0xC0A81050), "Should match /16 allow (not /24)");

    // Test 4: Planted exact IPs
    let mut acl4 = CidrAllowlist::new();
    acl4.add_rule(0x08080808, 32, true);  // 8.8.8.8/32 allow (Google DNS)
    acl4.add_rule(0x00000000, 0, false); // 0.0.0.0/0 deny all (default)
    assert!(acl4.matches(0x08080808), "8.8.8.8 should be allowed");
    assert!(!acl4.matches(0x08080809), "8.8.8.9 should be denied");
    assert!(!acl4.matches(0x01020304), "1.2.3.4 should be denied");

    // Test 5: Multiple overlapping rules
    let mut acl5 = CidrAllowlist::new();
    acl5.add_rule(0x0A000000, 8, true);   // 10.0.0.0/8 allow
    acl5.add_rule(0x0A0A0000, 16, false); // 10.10.0.0/16 deny
    acl5.add_rule(0x0A0A0A00, 24, true); // 10.10.10.0/24 allow
    assert!(acl5.matches(0x0A000001), "10.0.0.1 in /8 allow");
    assert!(!acl5.matches(0x0A0A0001), "10.10.0.1 in /16 deny (more specific)");
    assert!(acl5.matches(0x0A0A0A01), "10.10.10.1 in /24 allow (most specific)");

    println!("cidr_allowlist_match: PASS");
}
