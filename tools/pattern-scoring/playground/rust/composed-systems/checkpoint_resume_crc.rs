#![forbid(unsafe_code)]
//! checkpoint_resume_crc — checkpoint + CRC; crash after N records, resume without dups.
//!
//! Core idea: records are logged with a checkpoint marker every K records. On crash,
//! resume from the last checkpoint, replaying only the records between checkpoints.
//! CRC detects partial writes. THE LAW: log N records, truncate mid-record after
//! checkpoint M, resume, and assert each record is processed exactly once.
//! When to use: crash recovery with duplication avoidance, resumable operations.

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

struct CheckpointLog {
    records: Vec<Vec<u8>>,
    checkpoints: Vec<usize>, // indices where checkpoints occur
}

impl CheckpointLog {
    fn new() -> Self {
        CheckpointLog {
            records: Vec::new(),
            checkpoints: Vec::new(),
        }
    }

    fn append_and_checkpoint(&mut self, record: &[u8], checkpoint_interval: usize) {
        self.records.push(record.to_vec());
        if self.records.len() % checkpoint_interval == 0 {
            self.checkpoints.push(self.records.len());
        }
    }

    fn serialize(&self) -> Vec<u8> {
        let mut buf = Vec::new();
        for (i, record) in self.records.iter().enumerate() {
            let len = record.len() as u32;
            buf.extend_from_slice(&len.to_le_bytes());
            buf.extend_from_slice(record);
            let crc = crc32(record);
            buf.extend_from_slice(&crc.to_le_bytes());

            if self.checkpoints.contains(&(i + 1)) {
                // Write checkpoint marker.
                buf.push(0xFF);
                buf.push(0xFF);
                buf.push(0xFF);
                buf.push(0xFF);
            }
        }
        buf
    }

    fn recover(&self) -> Vec<Vec<u8>> {
        Self::recover_from(&self.serialize())
    }

    /// Recover from a (possibly truncated) byte image — the real crash-recovery entry point.
    fn recover_from(buf: &[u8]) -> Vec<Vec<u8>> {
        let mut recovered = Vec::new();
        let mut pos = 0;

        while pos + 8 <= buf.len() {
            // Check for checkpoint marker.
            if pos + 4 <= buf.len() && buf[pos..pos + 4] == [0xFF, 0xFF, 0xFF, 0xFF] {
                pos += 4;
                continue;
            }

            if pos + 8 > buf.len() {
                break; // Incomplete frame.
            }

            let len_bytes = &buf[pos..pos + 4];
            let len = u32::from_le_bytes([len_bytes[0], len_bytes[1], len_bytes[2], len_bytes[3]]) as usize;

            if pos + 4 + len + 4 > buf.len() {
                // Torn record after checkpoint.
                break;
            }

            let record = &buf[pos + 4..pos + 4 + len];
            let crc_bytes = &buf[pos + 4 + len..pos + 4 + len + 4];
            let stored_crc = u32::from_le_bytes([crc_bytes[0], crc_bytes[1], crc_bytes[2], crc_bytes[3]]);
            let computed_crc = crc32(record);

            if stored_crc == computed_crc {
                recovered.push(record.to_vec());
            } else {
                break; // CRC mismatch.
            }

            pos += 4 + len + 4;
        }

        recovered
    }

}

fn main() {
    // Log 10 records ("record_0".."record_9", each 8 bytes → frame = 4+8+4 = 16), checkpoint every 3.
    let mut log = CheckpointLog::new();
    for i in 0..10 {
        log.append_and_checkpoint(format!("record_{}", i).as_bytes(), 3);
    }
    assert_eq!(log.recover().len(), 10, "clean recover returns all 10");

    // THE LAW — cause the real disaster: serialize, TRUNCATE mid-record-7, recover from the
    // truncated image, and assert EXACTLY records 0..=6 come back (each once), the torn 7th dropped.
    let buf = log.serialize();
    // Layout: rec0..2 (48) + ckpt(4) + rec3..5 (48) + ckpt(4) + rec6 (16) = 120; rec7 starts at 120.
    let truncate_pos = 128; // 8 bytes into record 7's 16-byte frame
    let mut crashed = buf.clone();
    crashed.truncate(truncate_pos);
    assert!(crashed.len() < buf.len(), "truncation actually shortened the image");

    let recovered = CheckpointLog::recover_from(&crashed);
    assert_eq!(recovered.len(), 7, "exactly the 7 committed records (0..=6) recover; torn 7th dropped");
    for i in 0..7 {
        assert_eq!(recovered[i], format!("record_{}", i).as_bytes().to_vec(), "record {i} exact, once");
    }

    // A CRC corruption in a COMPLETE record halts recovery at that record (flip a byte in record 0's data).
    let mut corrupted = buf.clone();
    corrupted[4] ^= 0x01; // first data byte of record 0
    let rec_corrupt = CheckpointLog::recover_from(&corrupted);
    assert_eq!(rec_corrupt.len(), 0, "CRC mismatch on record 0 stops recovery immediately");

    // Empty log.
    assert_eq!(CheckpointLog::recover_from(&[]).len(), 0, "empty image recovers nothing");

    println!("checkpoint_resume_crc: real crash recovery, exactly-once, CRC detects corruption — PASS");
}
