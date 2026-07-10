#![forbid(unsafe_code)]
//! cidr_ip_math — IPv4 parse, CIDR contains, subnet split.
//!
//! Core idea: parse IPv4 addresses and CIDR blocks, check containment, split subnets in half.
//! THE ONE LAW: plant known IPs and CIDR blocks with exact containment and split results,
//! then assert all checks are correct — a miscalculated netmask or byte order error would
//! fail the containment or split asserts. When to use: IP routing, firewall rules, ACLs.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct IPv4 {
    octets: [u8; 4],
}

impl IPv4 {
    fn from_str(s: &str) -> Option<Self> {
        let parts: Vec<&str> = s.split('.').collect();
        if parts.len() != 4 {
            return None;
        }
        let mut octets = [0u8; 4];
        for (i, part) in parts.iter().enumerate() {
            octets[i] = part.parse::<u8>().ok()?;
        }
        Some(IPv4 { octets })
    }

    fn to_u32(&self) -> u32 {
        ((self.octets[0] as u32) << 24)
            | ((self.octets[1] as u32) << 16)
            | ((self.octets[2] as u32) << 8)
            | (self.octets[3] as u32)
    }

    fn from_u32(val: u32) -> Self {
        IPv4 {
            octets: [
                ((val >> 24) & 0xFF) as u8,
                ((val >> 16) & 0xFF) as u8,
                ((val >> 8) & 0xFF) as u8,
                (val & 0xFF) as u8,
            ],
        }
    }
}

struct CIDR {
    network: IPv4,
    prefix_len: u8,
}

impl CIDR {
    fn from_str(s: &str) -> Option<Self> {
        let parts: Vec<&str> = s.split('/').collect();
        if parts.len() != 2 {
            return None;
        }
        let network = IPv4::from_str(parts[0])?;
        let prefix_len = parts[1].parse::<u8>().ok()?;
        if prefix_len > 32 {
            return None;
        }
        Some(CIDR { network, prefix_len })
    }

    fn mask(&self) -> u32 {
        if self.prefix_len == 0 {
            0
        } else {
            0xFFFFFFFF << (32 - self.prefix_len)
        }
    }

    fn contains(&self, ip: &IPv4) -> bool {
        (self.network.to_u32() & self.mask()) == (ip.to_u32() & self.mask())
    }

    fn split(&self) -> (CIDR, CIDR) {
        if self.prefix_len >= 32 {
            panic!("cannot split /32");
        }
        let new_prefix = self.prefix_len + 1;
        let net_u32 = self.network.to_u32();
        let mask_u32 = if new_prefix == 32 {
            0xFFFFFFFF
        } else {
            0xFFFFFFFF << (32 - new_prefix)
        };

        // First half keeps the new subnet bit at 0; second half sets it to 1.
        let base = net_u32 & mask_u32;
        let subnet_bit = 1u32 << (32 - new_prefix);
        let net1 = IPv4::from_u32(base);
        let net2 = IPv4::from_u32(base | subnet_bit);

        (
            CIDR {
                network: net1,
                prefix_len: new_prefix,
            },
            CIDR {
                network: net2,
                prefix_len: new_prefix,
            },
        )
    }
}

fn main() {
    // Planted case: 192.168.1.5 is in 192.168.0.0/16 but not in 10.0.0.0/8.
    let ip1 = IPv4::from_str("192.168.1.5").unwrap();
    let ip2 = IPv4::from_str("10.0.0.5").unwrap();

    let cidr1 = CIDR::from_str("192.168.0.0/16").unwrap();
    let cidr2 = CIDR::from_str("10.0.0.0/8").unwrap();

    assert!(cidr1.contains(&ip1), "192.168.1.5 should be in 192.168.0.0/16");
    assert!(!cidr2.contains(&ip1), "192.168.1.5 should not be in 10.0.0.0/8");

    assert!(cidr2.contains(&ip2), "10.0.0.5 should be in 10.0.0.0/8");
    assert!(!cidr1.contains(&ip2), "10.0.0.5 should not be in 192.168.0.0/16");

    // THE ONE LAW: split a /16 into two /17s; each half must contain ITS OWN range and
    // EXCLUDE the other's — a broken split (both halves equal) fails these exclusions.
    let (first_half, second_half) = cidr1.split();
    assert_eq!(first_half.prefix_len, 17);
    assert_eq!(second_half.prefix_len, 17);

    let ip_low = IPv4::from_str("192.168.0.5").unwrap(); // 0 < 128 → first /17
    let ip_high = IPv4::from_str("192.168.200.5").unwrap(); // 200 ≥ 128 → second /17

    assert!(first_half.contains(&ip_low), "first half must contain 192.168.0.5");
    assert!(!first_half.contains(&ip_high), "first half must NOT contain 192.168.200.5");
    assert!(second_half.contains(&ip_high), "second half must contain 192.168.200.5");
    assert!(!second_half.contains(&ip_low), "second half must NOT contain 192.168.0.5");

    // The halves are distinct and both sit inside the parent /16.
    assert_ne!(
        first_half.network.to_u32(),
        second_half.network.to_u32(),
        "the two halves must have different network addresses"
    );
    assert!(
        cidr1.contains(&first_half.network) && cidr1.contains(&second_half.network),
        "both halves must sit within the parent block"
    );

    println!("cidr_ip_math: containment exact, /16 split into disjoint /17s verified — PASS");
}
