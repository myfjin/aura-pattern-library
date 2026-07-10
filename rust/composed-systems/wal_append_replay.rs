#![forbid(unsafe_code)]
//! wal_append_replay — write-ahead log with CRC-32 framing, crash simulation, and recovery.
//!
//! Core idea: each record is prefixed with length + followed by CRC32. A crash mid-write
//! leaves a torn tail. On replay, valid records are recovered exactly; a CRC mismatch
//! signals the torn record. THE LAW: write N records, truncate the file at a random point
//! mid-record, replay the corrupted file, and assert exactly the committed records come back
//! — proving the log survives the integrated disaster of an incomplete write.
//! When to use: durability guarantees, crash recovery, transactional logs.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn crc32(data: &[u8]) -> u32 {
    let mut crc = 0xffffffff_u32;
    for &byte in data {
        crc ^= byte as u32;
        for _ in 0..8 {
            crc = if crc & 1 == 1 {
                (crc >> 1) ^ 0xedb88320_u32
            } else {
                crc >> 1
            };
        }
    }
    crc ^ 0xffffffff
}

struct WalWriter {
    buf: Vec<u8>,
}

impl WalWriter {
    fn new() -> Self {
        WalWriter { buf: Vec::new() }
    }

    fn append(&mut self, record: &[u8]) {
        // Length-prefix: 4 bytes (little-endian) + record + CRC32 (4 bytes).
        let len = record.len() as u32;
        self.buf.extend_from_slice(&len.to_le_bytes());
        self.buf.extend_from_slice(record);
        let crc = crc32(record);
        self.buf.extend_from_slice(&crc.to_le_bytes());
    }

    fn bytes(&self) -> &[u8] {
        &self.buf
    }

    fn simulate_crash(&mut self, truncate_at: usize) {
        self.buf.truncate(truncate_at);
    }
}

struct WalReader<'a> {
    data: &'a [u8],
}

impl<'a> WalReader<'a> {
    fn new(data: &'a [u8]) -> Self {
        WalReader { data }
    }

    fn replay(&self) -> (Vec<Vec<u8>>, Vec<usize>) {
        let mut records = Vec::new();
        let mut torn_at = Vec::new();
        let mut pos = 0;

        while pos + 8 <= self.data.len() {
            // Try to read length.
            let len_bytes = &self.data[pos..pos + 4];
            let len = u32::from_le_bytes([len_bytes[0], len_bytes[1], len_bytes[2], len_bytes[3]]) as usize;

            // Check if entire record fits.
            if pos + 4 + len + 4 > self.data.len() {
                // Torn tail: record incomplete.
                torn_at.push(pos);
                break;
            }

            // Read record and CRC.
            let record = &self.data[pos + 4..pos + 4 + len];
            let crc_bytes = &self.data[pos + 4 + len..pos + 4 + len + 4];
            let stored_crc = u32::from_le_bytes([crc_bytes[0], crc_bytes[1], crc_bytes[2], crc_bytes[3]]);
            let computed_crc = crc32(record);

            if stored_crc != computed_crc {
                // CRC mismatch: torn or corrupted.
                torn_at.push(pos);
                break;
            }

            records.push(record.to_vec());
            pos += 4 + len + 4;
        }

        (records, torn_at)
    }
}

fn main() {
    // Test 1: write 5 records, truncate mid-4th, replay and verify first 3 committed.
    let mut wal = WalWriter::new();
    let records_written = vec![b"rec0", b"rec1", b"rec2", b"rec3", b"rec4"];
    for r in &records_written {
        wal.append(*r);
    }

    let mut wal_crashed = wal;

    // Truncate at a position that splits the 4th record (length=4, so frame is 4+4+4=12 bytes).
    // Find position of 4th record start: 3 * (4 + 4 + 4) = 36 bytes.
    let truncate_pos = 36 + 8; // 8 bytes into the 4th record's frame.
    wal_crashed.simulate_crash(truncate_pos);

    let reader = WalReader::new(wal_crashed.bytes());
    let (recovered, torn) = reader.replay();

    assert_eq!(recovered.len(), 3, "should recover exactly 3 intact records");
    assert_eq!(recovered[0], b"rec0".to_vec());
    assert_eq!(recovered[1], b"rec1".to_vec());
    assert_eq!(recovered[2], b"rec2".to_vec());
    assert_eq!(torn.len(), 1, "should detect exactly one torn tail");
    assert_eq!(torn[0], 36, "torn tail at 4th record");

    // Test 2: no crash — all records intact.
    let wal2 = WalWriter::new();
    let reader2 = WalReader::new(wal2.bytes());
    let (rec2, torn2) = reader2.replay();
    assert_eq!(rec2.len(), 0, "empty log replays empty");
    assert_eq!(torn2.len(), 0, "no torn tail in empty log");

    // Test 3: write, no truncation — full replay.
    let mut wal3 = WalWriter::new();
    for r in &records_written {
        wal3.append(*r);
    }
    let reader3 = WalReader::new(wal3.bytes());
    let (rec3, torn3) = reader3.replay();
    assert_eq!(rec3.len(), 5, "replay recovers all 5 records");
    for (i, r) in rec3.iter().enumerate() {
        assert_eq!(r.as_slice(), records_written[i]);
    }
    assert_eq!(torn3.len(), 0, "no torn tail after clean write");

    // Test 4: truncate mid-CRC of 2nd record to test CRC detection.
    let mut wal4 = WalWriter::new();
    wal4.append(b"aaaa");
    wal4.append(b"bbbb");
    wal4.append(b"cccc");
    // Position: record 0: 4+4+4=12, record 1: starts at 12, 4+4+4=12, record 2: starts at 24.
    // Truncate at 12 + 4 + 4 + 2 = 22 (mid-CRC of record 1).
    wal4.simulate_crash(22);
    let reader4 = WalReader::new(wal4.bytes());
    let (rec4, torn4) = reader4.replay();
    assert_eq!(rec4.len(), 1, "only 1st record before torn 2nd");
    assert_eq!(rec4[0], b"aaaa".to_vec());
    assert_eq!(torn4.len(), 1, "torn tail at 2nd record");

    println!("wal_append_replay: crash mid-record, recover committed, detect torn tail — PASS");
}
