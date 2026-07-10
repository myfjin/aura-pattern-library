#![forbid(unsafe_code)]
//! rotating_log_checksum — size-triggered rotation + per-segment CRC32; corruption isolated.
//!
//! Core idea: logs rotate every N bytes; when a segment is sealed its CRC32 is STORED. Verify
//! recomputes each segment's CRC and compares to the stored value — so a bit-flip in one segment
//! fails ONLY that segment, others still verify. THE LAW: seal a multi-segment log, corrupt one
//! segment's bytes, and assert exactly that segment fails verification while the rest pass. (A
//! verify that only checks "crc != 0" would miss the corruption entirely.)
//! When to use: rotated log files with integrity, corruption isolation, archival.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn crc32(data: &[u8]) -> u32 {
    let mut crc = 0xffffffff_u32;
    for &byte in data {
        crc ^= byte as u32;
        for _ in 0..8 {
            crc = if crc & 1 == 1 { (crc >> 1) ^ 0xedb88320 } else { crc >> 1 };
        }
    }
    crc ^ 0xffffffff
}

struct RotatingLog {
    segments: Vec<Vec<u8>>,
    stored_crc: Vec<u32>, // CRC captured when the segment was sealed
    segment_size: usize,
}

impl RotatingLog {
    fn new(segment_size: usize) -> Self {
        RotatingLog { segments: vec![Vec::new()], stored_crc: vec![], segment_size }
    }

    fn append(&mut self, data: &[u8]) {
        let current = self.segments.last_mut().unwrap();
        if current.len() + data.len() > self.segment_size && !current.is_empty() {
            self.segments.push(Vec::new());
        }
        self.segments.last_mut().unwrap().extend_from_slice(data);
    }

    /// Seal every segment: record its current CRC as the integrity baseline.
    fn seal(&mut self) {
        self.stored_crc = self.segments.iter().map(|s| crc32(s)).collect();
    }

    /// A segment verifies iff its recomputed CRC matches the STORED one.
    fn verify_segment(&self, i: usize) -> bool {
        match (self.segments.get(i), self.stored_crc.get(i)) {
            (Some(seg), Some(&stored)) => crc32(seg) == stored,
            _ => false,
        }
    }

    fn corrupt_segment(&mut self, i: usize, byte_pos: usize) {
        if let Some(seg) = self.segments.get_mut(i) {
            if byte_pos < seg.len() {
                seg[byte_pos] ^= 0x42;
            }
        }
    }
}

fn main() {
    let mut log = RotatingLog::new(20);
    log.append(b"segment_a_data_");
    log.append(b"segment_b_data_");
    log.append(b"segment_c_data_");
    assert!(log.segments.len() >= 3, "data rotated across ≥3 segments");
    log.seal();

    // All segments verify against their sealed CRC.
    for i in 0..log.segments.len() {
        assert!(log.verify_segment(i), "sealed segment {i} verifies");
    }

    // THE LAW: corrupt exactly segment 1 → ONLY it fails; the others still verify.
    log.corrupt_segment(1, 3);
    assert!(!log.verify_segment(1), "corrupted segment 1 must FAIL verification");
    for i in 0..log.segments.len() {
        if i != 1 {
            assert!(log.verify_segment(i), "uncorrupted segment {i} still verifies");
        }
    }

    // Empty sealed log: segment 0 (empty) verifies against its stored CRC.
    let mut empty = RotatingLog::new(10);
    empty.seal();
    assert!(empty.verify_segment(0), "empty sealed segment verifies");
    assert!(!empty.verify_segment(5), "out-of-range segment does not verify");

    println!("rotating_log_checksum: per-segment stored CRC isolates corruption to one segment — PASS");
}
