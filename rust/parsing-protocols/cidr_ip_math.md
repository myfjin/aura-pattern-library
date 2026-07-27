# cidr ip math

**Language:** Rust · **Sphere:** rust · **Category:** parsing-protocols

**Signature:** `(s: &str) → Option<Self>`

## What it does

cidr_ip_math — IPv4 parse, CIDR contains, subnet split.

Core idea: parse IPv4 addresses and CIDR blocks, check containment, split subnets in half.
THE ONE LAW: plant known IPs and CIDR blocks with exact containment and split results,
then assert all checks are correct — a miscalculated netmask or byte order error would
fail the containment or split asserts. When to use: IP routing, firewall rules, ACLs.

## Guarantee

When it runs, cidr ip math guarantees assert_eq!(first_half.prefix_len, 17); assert_eq!(second_half.prefix_len, 17) (proven by rustc-run).

**Checkable constraints:**

- `assert!(cidr1.contains(&ip1), "192.168.1.5 should be in 192.168.0.0/16")`
- `assert!(!cidr2.contains(&ip1), "192.168.1.5 should not be in 10.0.0.0/8")`
- `assert!(cidr2.contains(&ip2), "10.0.0.5 should be in 10.0.0.0/8")`
- `assert!(!cidr1.contains(&ip2), "10.0.0.5 should not be in 192.168.0.0/16")`
- `assert_eq!(first_half.prefix_len, 17)`
- `assert_eq!(second_half.prefix_len, 17)`
- `assert!(first_half.contains(&ip_low), "first half must contain 192.168.0.5")`
- `assert!(!first_half.contains(&ip_high), "first half must NOT contain 192.168.200.5")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
