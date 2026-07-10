#![forbid(unsafe_code)]
//! TOTP (Time-based OTP, RFC 6238) — time-synchronized one-time passwords.
//! Core idea: HOTP with time window (30s intervals), SHA1 truncation.
//! When to use: authenticator apps, 2FA, backup codes.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn sha1_compress(h: &mut [u32; 5], block: &[u8; 64]) {
    let mut w = [0u32; 80];
    for i in 0..16 { w[i] = u32::from_be_bytes([block[i*4], block[i*4+1], block[i*4+2], block[i*4+3]]); }
    for i in 16..80 { let t = w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]; w[i] = t.rotate_left(1); }
    let mut a = h[0]; let mut b = h[1]; let mut c = h[2]; let mut d = h[3]; let mut e = h[4];
    for i in 0..80 {
        let f = if i < 20 { (b & c) | ((!b) & d) } else if i < 40 { b ^ c ^ d } else if i < 60 { (b & c) | (b & d) | (c & d) } else { b ^ c ^ d };
        let k = if i < 20 { 0x5a827999u32 } else if i < 40 { 0x6ed9eba1u32 } else if i < 60 { 0x8f1bbcdc } else { 0xca62c1d6 };
        let temp = a.rotate_left(5).wrapping_add(f).wrapping_add(e).wrapping_add(k).wrapping_add(w[i]);
        e = d; d = c; c = b.rotate_left(30); b = a; a = temp;
    }
    h[0] = h[0].wrapping_add(a); h[1] = h[1].wrapping_add(b);
    h[2] = h[2].wrapping_add(c); h[3] = h[3].wrapping_add(d); h[4] = h[4].wrapping_add(e);
}

fn sha1(data: &[u8]) -> [u8; 20] {
    let mut h = [0x67452301u32, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0];
    let mut msg = data.to_vec();
    let orig_len = (data.len() as u64) * 8;
    msg.push(0x80);
    while (msg.len() % 64) != 56 { msg.push(0); }
    msg.extend_from_slice(&orig_len.to_be_bytes());
    for chunk in msg.chunks_exact(64) {
        let mut block = [0u8; 64];
        block.copy_from_slice(chunk);
        sha1_compress(&mut h, &block);
    }
    let mut digest = [0u8; 20];
    for (i, &v) in h.iter().enumerate() { digest[i*4..i*4+4].copy_from_slice(&v.to_be_bytes()); }
    digest
}

fn hmac_sha1(key: &[u8], msg: &[u8]) -> [u8; 20] {
    let mut key_padded = [0u8; 64];
    if key.len() <= 64 { key_padded[..key.len()].copy_from_slice(key); } else {
        let h = sha1(key); key_padded[..20].copy_from_slice(&h);
    }
    let mut ipad = [0x36u8; 64]; let mut opad = [0x5cu8; 64];
    for i in 0..64 { ipad[i] ^= key_padded[i]; opad[i] ^= key_padded[i]; }
    let mut inner = ipad.to_vec(); inner.extend_from_slice(msg);
    let inner_hash = sha1(&inner);
    let mut outer = opad.to_vec(); outer.extend_from_slice(&inner_hash);
    sha1(&outer)
}

fn totp(secret: &[u8], time_s: u64, step: u64, digits: u32) -> u32 {
    let counter = time_s / step;
    let hmac = hmac_sha1(secret, &counter.to_be_bytes());
    let offset = (hmac[19] & 0x0f) as usize;
    let p = u32::from_be_bytes([hmac[offset], hmac[offset+1], hmac[offset+2], hmac[offset+3]]);
    let code = p & 0x7fff_ffff;
    let modulo = 10u32.pow(digits);
    code % modulo
}

fn main() {
    // RFC 6238 SHA1 HMAC-based time-locked codes. Time window = 30s steps.
    let secret = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
                  0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f];

    // t=59 is in window 59/30=1 (same as t=30..59)
    let code_t59 = totp(&secret, 59u64, 30, 6);
    // t=45 is also in window 45/30=1
    let code_t45 = totp(&secret, 45u64, 30, 6);
    assert_eq!(code_t59, code_t45, "same window (30-59) codes must match");

    // t=60 is in window 60/30=2 (different from 1)
    let code_t60 = totp(&secret, 60u64, 30, 6);
    assert_ne!(code_t59, code_t60, "adjacent windows must differ");

    // Verify determinism over time steps
    let code_t0 = totp(&secret, 0u64, 30, 6);
    let code_t15 = totp(&secret, 15u64, 30, 6);
    assert_eq!(code_t0, code_t15, "same window (0-29) must match");

    // THE VECTOR IS EXACT: RFC 6238 Appendix B published SHA-1 test vectors
    // (secret = ASCII "12345678901234567890", 8 digits, 30s step). Self-consistency alone
    // could hide a wrong impl; these external facts cannot.
    let rfc = b"12345678901234567890";
    assert_eq!(totp(rfc, 59, 30, 8), 94287082, "RFC 6238 T=59 must be 94287082");
    assert_eq!(totp(rfc, 1111111109, 30, 8), 7081804, "RFC 6238 T=1111111109 must be 07081804");
    assert_eq!(totp(rfc, 1234567890, 30, 8), 89005924, "RFC 6238 T=1234567890 must be 89005924");

    println!("totp ... PASS");
}
