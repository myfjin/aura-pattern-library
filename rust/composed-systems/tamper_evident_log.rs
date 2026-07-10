#![forbid(unsafe_code)]
//! tamper_evident_log — HMAC-SHA256 hash-chained log; tampering detected at exact point.
//!
//! Core idea: each log entry includes the HMAC of (previous_hash || current_record).
//! If any past entry is tampered, the chain breaks at that exact index. THE LAW: write
//! N entries, tamper one in the middle, verify, and assert the chain breaks exactly
//! at the tampered entry — proving the log detects and pinpoints corruption.
//! When to use: audit logs, blockchain-lite, integrity chains, tamper detection.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn sha256(data: &[u8]) -> [u8; 32] {
    const K: [u32; 64] = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
    ];

    let mut h0 = 0x6a09e667u32;
    let mut h1 = 0xbb67ae85u32;
    let mut h2 = 0x3c6ef372u32;
    let mut h3 = 0xa54ff53au32;
    let mut h4 = 0x510e527fu32;
    let mut h5 = 0x9b05688cu32;
    let mut h6 = 0x1f83d9abu32;
    let mut h7 = 0x5be0cd19u32;

    let mut msg = Vec::from(data);
    let orig_len = (data.len() as u64) * 8;
    msg.push(0x80);
    while msg.len() % 64 != 56 {
        msg.push(0x00);
    }
    msg.extend_from_slice(&orig_len.to_be_bytes());

    for chunk in msg.chunks_exact(64) {
        let mut w = [0u32; 64];
        for i in 0..16 {
            w[i] = u32::from_be_bytes([chunk[i * 4], chunk[i * 4 + 1], chunk[i * 4 + 2], chunk[i * 4 + 3]]);
        }
        for i in 16..64 {
            let s0 = w[i - 15].rotate_right(7) ^ w[i - 15].rotate_right(18) ^ (w[i - 15] >> 3);
            let s1 = w[i - 2].rotate_right(17) ^ w[i - 2].rotate_right(19) ^ (w[i - 2] >> 10);
            w[i] = w[i - 16].wrapping_add(s0).wrapping_add(w[i - 7]).wrapping_add(s1);
        }

        let mut a = h0;
        let mut b = h1;
        let mut c = h2;
        let mut d = h3;
        let mut e = h4;
        let mut f = h5;
        let mut g = h6;
        let mut h = h7;

        for i in 0..64 {
            let s1 = e.rotate_right(6) ^ e.rotate_right(11) ^ e.rotate_right(25);
            let ch = (e & f) ^ ((!e) & g);
            let temp1 = h.wrapping_add(s1).wrapping_add(ch).wrapping_add(K[i]).wrapping_add(w[i]);
            let s0 = a.rotate_right(2) ^ a.rotate_right(13) ^ a.rotate_right(22);
            let maj = (a & b) ^ (a & c) ^ (b & c);
            let temp2 = s0.wrapping_add(maj);

            h = g;
            g = f;
            f = e;
            e = d.wrapping_add(temp1);
            d = c;
            c = b;
            b = a;
            a = temp1.wrapping_add(temp2);
        }

        h0 = h0.wrapping_add(a);
        h1 = h1.wrapping_add(b);
        h2 = h2.wrapping_add(c);
        h3 = h3.wrapping_add(d);
        h4 = h4.wrapping_add(e);
        h5 = h5.wrapping_add(f);
        h6 = h6.wrapping_add(g);
        h7 = h7.wrapping_add(h);
    }

    let mut digest = [0u8; 32];
    digest[0..4].copy_from_slice(&h0.to_be_bytes());
    digest[4..8].copy_from_slice(&h1.to_be_bytes());
    digest[8..12].copy_from_slice(&h2.to_be_bytes());
    digest[12..16].copy_from_slice(&h3.to_be_bytes());
    digest[16..20].copy_from_slice(&h4.to_be_bytes());
    digest[20..24].copy_from_slice(&h5.to_be_bytes());
    digest[24..28].copy_from_slice(&h6.to_be_bytes());
    digest[28..32].copy_from_slice(&h7.to_be_bytes());
    digest
}

fn hmac_sha256(key: &[u8], msg: &[u8]) -> [u8; 32] {
    const BLOCK_SIZE: usize = 64;
    let mut k = [0u8; BLOCK_SIZE];
    if key.len() <= BLOCK_SIZE {
        k[..key.len()].copy_from_slice(key);
    } else {
        let hash = sha256(key);
        k[..32].copy_from_slice(&hash);
    }

    let mut opad = [0x5cu8; BLOCK_SIZE];
    let mut ipad = [0x36u8; BLOCK_SIZE];
    for i in 0..BLOCK_SIZE {
        opad[i] ^= k[i];
        ipad[i] ^= k[i];
    }

    let mut inner = Vec::from(&ipad[..]);
    inner.extend_from_slice(msg);
    let inner_hash = sha256(&inner);

    let mut outer = Vec::from(&opad[..]);
    outer.extend_from_slice(&inner_hash);
    sha256(&outer)
}

struct TamperEvidenceLog {
    entries: Vec<Vec<u8>>,
    hashes: Vec<[u8; 32]>,
}

impl TamperEvidenceLog {
    fn new() -> Self {
        TamperEvidenceLog {
            entries: Vec::new(),
            hashes: Vec::new(),
        }
    }

    fn append(&mut self, entry: &[u8], key: &[u8]) {
        let prev_hash = if let Some(h) = self.hashes.last() {
            *h
        } else {
            [0u8; 32]
        };

        let mut payload = Vec::from(&prev_hash[..]);
        payload.extend_from_slice(entry);
        let hash = hmac_sha256(key, &payload);

        self.entries.push(entry.to_vec());
        self.hashes.push(hash);
    }

    fn verify(&self, key: &[u8]) -> Result<(), usize> {
        for (i, entry) in self.entries.iter().enumerate() {
            let prev_hash = if i == 0 {
                [0u8; 32]
            } else {
                self.hashes[i - 1]
            };

            let mut payload = Vec::from(&prev_hash[..]);
            payload.extend_from_slice(entry);
            let computed_hash = hmac_sha256(key, &payload);

            if computed_hash != self.hashes[i] {
                return Err(i);
            }
        }
        Ok(())
    }

    fn tamper_at(&mut self, index: usize, new_data: &[u8]) {
        if index < self.entries.len() {
            self.entries[index] = new_data.to_vec();
            // Intentionally do NOT recompute the hash chain.
        }
    }
}

fn main() {
    // Test 1: write 5 entries, verify chain.
    let key = b"secret_key_12345";
    let mut log = TamperEvidenceLog::new();
    let entries = vec![b"entry_0", b"entry_1", b"entry_2", b"entry_3", b"entry_4"];
    for e in &entries {
        log.append(*e, key);
    }
    assert!(log.verify(key).is_ok(), "clean log verifies");

    // Test 2: tamper with entry 2, verify breaks at index 2.
    let mut log2 = log.clone();
    log2.tamper_at(2, b"entry_TAMPERED");
    match log2.verify(key) {
        Err(idx) => assert_eq!(idx, 2, "tamper at 2 breaks chain at 2"),
        Ok(()) => panic!("tampered log should fail verification"),
    }

    // Test 3: tamper with entry 0, chain breaks at 0, and all subsequent entries invalid.
    let mut log3 = log.clone();
    log3.tamper_at(0, b"entry_0_TAMPERED");
    match log3.verify(key) {
        Err(idx) => assert_eq!(idx, 0, "tamper at 0 breaks chain at 0"),
        Ok(()) => panic!("tampered entry 0 should fail"),
    }

    // Test 4: tamper with last entry.
    let mut log4 = log.clone();
    log4.tamper_at(4, b"entry_4_TAMPERED");
    match log4.verify(key) {
        Err(idx) => assert_eq!(idx, 4, "tamper at 4 breaks chain at 4"),
        Ok(()) => panic!("tampered entry 4 should fail"),
    }

    // Test 5: empty log verifies.
    let empty_log = TamperEvidenceLog::new();
    assert!(empty_log.verify(key).is_ok(), "empty log verifies");

    println!("tamper_evident_log: hash chain detects tampering at exact point — PASS");
}

impl Clone for TamperEvidenceLog {
    fn clone(&self) -> Self {
        TamperEvidenceLog {
            entries: self.entries.clone(),
            hashes: self.hashes.clone(),
        }
    }
}
