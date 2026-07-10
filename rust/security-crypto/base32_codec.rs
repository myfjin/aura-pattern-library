#![forbid(unsafe_code)]
//! Base32 codec (RFC 4648) — encode/decode binary to case-insensitive ASCII.
//! Core idea: 5-bit groups mapped to 32-char alphabet, padding on remainder.
//! When to use: case-insensitive transmission, DNS records, TOTP secrets.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
const ALPHABET: &[u8] = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";

fn base32_encode(data: &[u8]) -> String {
    let mut result = String::new();
    for chunk in data.chunks(5) {
        let n = match chunk.len() {
            1 => (chunk[0] as u64) << 32,
            2 => ((chunk[0] as u64) << 32) | ((chunk[1] as u64) << 24),
            3 => ((chunk[0] as u64) << 32) | ((chunk[1] as u64) << 24) | ((chunk[2] as u64) << 16),
            4 => ((chunk[0] as u64) << 32) | ((chunk[1] as u64) << 24) | ((chunk[2] as u64) << 16) | ((chunk[3] as u64) << 8),
            5 => ((chunk[0] as u64) << 32) | ((chunk[1] as u64) << 24) | ((chunk[2] as u64) << 16) | ((chunk[3] as u64) << 8) | (chunk[4] as u64),
            _ => 0,
        };
        result.push(ALPHABET[((n >> 35) & 0x1f) as usize] as char);
        result.push(ALPHABET[((n >> 30) & 0x1f) as usize] as char);
        if chunk.len() >= 2 {
            result.push(ALPHABET[((n >> 25) & 0x1f) as usize] as char);
            result.push(ALPHABET[((n >> 20) & 0x1f) as usize] as char);
        } else {
            result.push_str("======");
            break;
        }
        if chunk.len() >= 3 {
            result.push(ALPHABET[((n >> 15) & 0x1f) as usize] as char);
        } else {
            result.push_str("====");
            break;
        }
        if chunk.len() >= 4 {
            result.push(ALPHABET[((n >> 10) & 0x1f) as usize] as char);
            result.push(ALPHABET[((n >> 5) & 0x1f) as usize] as char);
        } else {
            result.push_str("===");
            break;
        }
        if chunk.len() >= 5 {
            result.push(ALPHABET[(n & 0x1f) as usize] as char);
        } else {
            result.push('=');
            break;
        }
    }
    result
}

fn base32_decode(s: &str) -> Option<Vec<u8>> {
    let mut table = [255u8; 256];
    for (i, &c) in ALPHABET.iter().enumerate() {
        table[c as usize] = i as u8;
    }
    let bytes = s.as_bytes();
    if bytes.len() % 8 != 0 { return None; }
    let mut result = Vec::new();
    for chunk in bytes.chunks(8) {
        if table[chunk[0] as usize] == 255 || table[chunk[1] as usize] == 255 { return None; }
        let c0 = table[chunk[0] as usize];
        let c1 = table[chunk[1] as usize];
        let c2 = if chunk[2] == b'=' { 0 } else { table[chunk[2] as usize] };
        let c3 = if chunk[3] == b'=' { 0 } else { table[chunk[3] as usize] };
        let c4 = if chunk[4] == b'=' { 0 } else { table[chunk[4] as usize] };
        let c5 = if chunk[5] == b'=' { 0 } else { table[chunk[5] as usize] };
        let c6 = if chunk[6] == b'=' { 0 } else { table[chunk[6] as usize] };
        let c7 = if chunk[7] == b'=' { 0 } else { table[chunk[7] as usize] };
        let n = ((c0 as u64) << 35) | ((c1 as u64) << 30) | ((c2 as u64) << 25) |
                ((c3 as u64) << 20) | ((c4 as u64) << 15) | ((c5 as u64) << 10) |
                ((c6 as u64) << 5) | (c7 as u64);
        result.push((n >> 32) as u8);
        if chunk[2] != b'=' && chunk[3] != b'=' { result.push((n >> 24) as u8); }
        if chunk[4] != b'=' { result.push((n >> 16) as u8); }
        if chunk[5] != b'=' && chunk[6] != b'=' { result.push((n >> 8) as u8); }
        if chunk[7] != b'=' { result.push(n as u8); }
    }
    Some(result)
}

fn main() {
    // RFC 4648 test vectors
    let tests = vec![
        ("f", "MY======"),
        ("fo", "MZXQ===="),
        ("foobar", "MZXW6YTBOI======"),
    ];
    for (input, expected) in tests {
        let encoded = base32_encode(input.as_bytes());
        assert_eq!(encoded, expected, "base32_encode('{}') mismatch", input);
        let decoded = base32_decode(expected).expect("decode failed");
        assert_eq!(decoded, input.as_bytes(), "base32_decode('{}') round-trip mismatch", expected);
    }
    println!("base32_codec ... PASS");
}
