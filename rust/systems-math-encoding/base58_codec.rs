#![forbid(unsafe_code)]
//! Base58 codec (Bitcoin alphabet): encode/decode arbitrary-length bytes.
//! Core idea: treat the byte string as a big-endian base-256 number and re-base it to 58 by
//! processing each input byte with carry propagation — so it works for ANY length (a real
//! 25-byte address), unlike a fixed u128 which overflows past 16 bytes. Leading zero bytes map
//! to leading '1's (and '1' is itself the digit 0 — decoded normally, not skipped). THE ONE LAW:
//! assert against published base58 vectors (including a 20-byte input that a u128 impl fails).
//! When to use: Bitcoin addresses, human-readable binary without 0/O/I/l ambiguity.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
const ALPHABET: &[u8] = b"123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz";

fn base58_encode(data: &[u8]) -> String {
    // base-256 → base-58 by carry propagation (O(n^2), correct for any length).
    let mut digits: Vec<u8> = Vec::new(); // base-58 digits, least-significant first
    for &byte in data {
        let mut carry = byte as u32;
        for d in digits.iter_mut() {
            let acc = (*d as u32) * 256 + carry;
            *d = (acc % 58) as u8;
            carry = acc / 58;
        }
        while carry > 0 {
            digits.push((carry % 58) as u8);
            carry /= 58;
        }
    }
    let mut s = String::new();
    for _ in data.iter().take_while(|&&b| b == 0) {
        s.push('1'); // each leading zero byte → one '1'
    }
    for &d in digits.iter().rev() {
        s.push(ALPHABET[d as usize] as char);
    }
    s
}

fn base58_decode(s: &str) -> Option<Vec<u8>> {
    let mut table = [255u8; 128];
    for (i, &c) in ALPHABET.iter().enumerate() {
        table[c as usize] = i as u8;
    }
    // base-58 → base-256 by carry propagation.
    let mut bytes: Vec<u8> = Vec::new(); // base-256, least-significant first
    for ch in s.chars() {
        let ci = ch as usize;
        if ci >= 128 || table[ci] == 255 {
            return None;
        }
        let mut carry = table[ci] as u32; // '1' → 0, processed normally (no skipping)
        for b in bytes.iter_mut() {
            let acc = (*b as u32) * 58 + carry;
            *b = (acc % 256) as u8;
            carry = acc / 256;
        }
        while carry > 0 {
            bytes.push((carry % 256) as u8);
            carry /= 256;
        }
    }
    let mut out: Vec<u8> = Vec::new();
    for _ in s.chars().take_while(|&c| c == '1') {
        out.push(0); // each leading '1' → one zero byte
    }
    for &b in bytes.iter().rev() {
        out.push(b);
    }
    Some(out)
}

fn main() {
    // THE VECTORS ARE EXACT — from the Bitcoin base58 test suite:
    assert_eq!(base58_encode(b"a"), "2g", "0x61 → 2g");
    assert_eq!(base58_encode(&[0x62, 0x62, 0x62]), "a3gV");
    assert_eq!(base58_encode(&[0x63, 0x63, 0x63]), "aPEr");
    // A 20-byte input — the OLD u128 impl (max 16 bytes) could not encode this.
    assert_eq!(
        base58_encode(b"simply a long string"),
        "2cFupjhnEsSn59qHXstmK2ffpLv2",
        "20-byte input must encode correctly (u128 would overflow)"
    );

    // Leading-zero handling: each zero byte → one '1'.
    assert_eq!(base58_encode(b""), "");
    assert_eq!(base58_encode(&[0x00]), "1");
    assert_eq!(base58_encode(&[0x00, 0x00]), "11");
    assert_eq!(base58_encode(&[0x00, 0x00, 0x61]), "112g");

    // Round-trip over arbitrary lengths, including the 20-byte and leading-zero cases.
    for case in [
        &b""[..], &b"a"[..], &b"simply a long string"[..], &[0x00, 0x00, 0x01, 0x02, 0x03][..],
        &[0xff; 25][..], &[0x00, 0xff, 0x80, 0x40, 0x20][..],
    ] {
        let enc = base58_encode(case);
        let dec = base58_decode(&enc).expect("decode");
        assert_eq!(dec, case, "round-trip failed for {enc}");
    }

    // A mid-string '1' is the digit 0, decoded normally (not skipped): decode(encode(x)) holds above,
    // and an invalid character is rejected.
    assert!(base58_decode("0OIl").is_none(), "characters outside the alphabet are rejected");

    println!("base58_codec ... PASS");
}
