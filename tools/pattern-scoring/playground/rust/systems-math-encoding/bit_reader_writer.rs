#![forbid(unsafe_code)]
//! Bit-level reader/writer: pack arbitrary-width bit fields and read them back exactly.
//! Core idea: maintain bit position in a byte buffer; write/read N bits at cursor.
//! When to use: binary protocols, image compression, bitfield serialization.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct BitWriter {
    bytes: Vec<u8>,
    bit_pos: usize,
}

impl BitWriter {
    fn new() -> Self {
        BitWriter { bytes: Vec::new(), bit_pos: 0 }
    }

    fn write_bits(&mut self, value: u64, n_bits: usize) {
        assert!(n_bits <= 64);
        for i in 0..n_bits {
            let bit = (value >> i) & 1;
            let byte_idx = self.bit_pos / 8;
            let bit_idx = self.bit_pos % 8;
            if byte_idx >= self.bytes.len() {
                self.bytes.push(0);
            }
            if bit != 0 {
                self.bytes[byte_idx] |= 1 << bit_idx;
            }
            self.bit_pos += 1;
        }
    }

    fn finish(self) -> Vec<u8> {
        self.bytes
    }
}

struct BitReader {
    bytes: Vec<u8>,
    bit_pos: usize,
}

impl BitReader {
    fn new(bytes: Vec<u8>) -> Self {
        BitReader { bytes, bit_pos: 0 }
    }

    fn read_bits(&mut self, n_bits: usize) -> Option<u64> {
        assert!(n_bits <= 64);
        let mut result = 0u64;
        for i in 0..n_bits {
            let byte_idx = self.bit_pos / 8;
            let bit_idx = self.bit_pos % 8;
            if byte_idx >= self.bytes.len() {
                return None;
            }
            let bit = (self.bytes[byte_idx] >> bit_idx) & 1;
            result |= (bit as u64) << i;
            self.bit_pos += 1;
        }
        Some(result)
    }
}

fn main() {
    // Test case 1: 3-bit + 5-bit + 12-bit fields
    let mut writer = BitWriter::new();
    writer.write_bits(0b101u64, 3);    // 5 in 3 bits
    writer.write_bits(0b11010u64, 5);  // 26 in 5 bits
    writer.write_bits(0xabcu64, 12);   // 2748 in 12 bits
    let packed = writer.finish();

    // Expected bit pattern (LSB first per byte):
    // Bits [0..3): 0b101 = 5
    // Bits [3..8): 0b11010 = 26
    // Bits [8..20): 0xabc = 0b101010111100
    // Byte 0: bits[0..8) = 0b_11_101 (lower 3 bits=101, next 2 bits from 26=11) = 0b00011101 = 0x1d
    // Byte 1: bits[8..16) = bits[3..5)from field2 + bits[0..6)from field3 = 0b11 + 0b111100 = 0b11111100 = 0xfc
    // Byte 2: bits[16..20) = bits[6..10)from field3 = 0b1010 (upper 4 bits of 0xabc>>6 = 0xa) = 0x0a
    assert_eq!(packed.len(), 3);

    let mut reader = BitReader::new(packed.clone());
    let v1 = reader.read_bits(3).expect("read 3 bits");
    let v2 = reader.read_bits(5).expect("read 5 bits");
    let v3 = reader.read_bits(12).expect("read 12 bits");

    assert_eq!(v1, 5, "3-bit field mismatch");
    assert_eq!(v2, 26, "5-bit field mismatch");
    assert_eq!(v3, 0xabc, "12-bit field mismatch");

    // Test case 2: single byte all bits
    let mut writer2 = BitWriter::new();
    for _ in 0..8 {
        writer2.write_bits(1u64, 1);
    }
    let packed2 = writer2.finish();
    assert_eq!(packed2, vec![0xff]);

    let mut reader2 = BitReader::new(packed2);
    for i in 0..8 {
        let bit = reader2.read_bits(1).expect("read bit");
        assert_eq!(bit, 1, "bit {} mismatch", i);
    }

    // Test case 3: mixed pattern
    let mut writer3 = BitWriter::new();
    writer3.write_bits(0b10u64, 2);
    writer3.write_bits(0b11u64, 2);
    writer3.write_bits(0b00u64, 2);
    writer3.write_bits(0b01u64, 2);
    let packed3 = writer3.finish();
    assert_eq!(packed3[0], 0b01_00_11_10); // LSB first

    let mut reader3 = BitReader::new(packed3);
    assert_eq!(reader3.read_bits(2).unwrap(), 0b10);
    assert_eq!(reader3.read_bits(2).unwrap(), 0b11);
    assert_eq!(reader3.read_bits(2).unwrap(), 0b00);
    assert_eq!(reader3.read_bits(2).unwrap(), 0b01);

    println!("bit_reader_writer ... PASS");
}
