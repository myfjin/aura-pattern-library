#![forbid(unsafe_code)]
//! Dynamic bitset: set/clear/test bits with and/or/xor operations.
//! Core idea: Vec<u8> backing store, 8 bits per byte; operations match Vec<bool> exactly.
//! When to use: sparse bitmaps, large bit arrays, membership tests, permissions.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct DynamicBitset {
    bytes: Vec<u8>,
    len: usize,
}

impl DynamicBitset {
    fn new(len: usize) -> Self {
        let byte_len = (len + 7) / 8;
        DynamicBitset {
            bytes: vec![0; byte_len],
            len,
        }
    }

    fn set(&mut self, bit: usize) {
        assert!(bit < self.len);
        let byte_idx = bit / 8;
        let bit_idx = bit % 8;
        self.bytes[byte_idx] |= 1 << bit_idx;
    }

    fn clear(&mut self, bit: usize) {
        assert!(bit < self.len);
        let byte_idx = bit / 8;
        let bit_idx = bit % 8;
        self.bytes[byte_idx] &= !(1 << bit_idx);
    }

    fn test(&self, bit: usize) -> bool {
        assert!(bit < self.len);
        let byte_idx = bit / 8;
        let bit_idx = bit % 8;
        (self.bytes[byte_idx] >> bit_idx) & 1 != 0
    }

    fn count_ones(&self) -> usize {
        self.bytes.iter().map(|b| b.count_ones() as usize).sum()
    }

    fn and(&self, other: &DynamicBitset) -> DynamicBitset {
        assert_eq!(self.len, other.len);
        let mut result = DynamicBitset::new(self.len);
        for i in 0..self.bytes.len() {
            result.bytes[i] = self.bytes[i] & other.bytes[i];
        }
        result
    }

    fn or(&self, other: &DynamicBitset) -> DynamicBitset {
        assert_eq!(self.len, other.len);
        let mut result = DynamicBitset::new(self.len);
        for i in 0..self.bytes.len() {
            result.bytes[i] = self.bytes[i] | other.bytes[i];
        }
        result
    }

    fn xor(&self, other: &DynamicBitset) -> DynamicBitset {
        assert_eq!(self.len, other.len);
        let mut result = DynamicBitset::new(self.len);
        for i in 0..self.bytes.len() {
            result.bytes[i] = self.bytes[i] ^ other.bytes[i];
        }
        result
    }
}

fn main() {
    // Test basic set/clear/test
    let mut bs = DynamicBitset::new(16);
    assert_eq!(bs.test(0), false);
    bs.set(0);
    assert_eq!(bs.test(0), true);
    bs.clear(0);
    assert_eq!(bs.test(0), false);

    // Test count_ones
    let mut bs2 = DynamicBitset::new(8);
    assert_eq!(bs2.count_ones(), 0);
    bs2.set(0);
    bs2.set(2);
    bs2.set(7);
    assert_eq!(bs2.count_ones(), 3);

    // Compare with Vec<bool> reference
    let mut vec_ref = vec![false; 32];
    let mut bs_ref = DynamicBitset::new(32);

    // Set specific bits and verify against Vec<bool>
    for bit in [0, 1, 5, 7, 15, 16, 31] {
        vec_ref[bit] = true;
        bs_ref.set(bit);
    }

    for i in 0..32 {
        assert_eq!(bs_ref.test(i), vec_ref[i], "test mismatch at bit {}", i);
    }
    assert_eq!(bs_ref.count_ones(), vec_ref.iter().filter(|&&b| b).count());

    // Test AND operation
    let mut a = DynamicBitset::new(16);
    let mut b = DynamicBitset::new(16);
    a.set(0);
    a.set(1);
    a.set(2);
    b.set(1);
    b.set(2);
    b.set(3);

    let and_result = a.and(&b);
    assert_eq!(and_result.test(0), false);
    assert_eq!(and_result.test(1), true);
    assert_eq!(and_result.test(2), true);
    assert_eq!(and_result.test(3), false);

    // Test OR operation
    let or_result = a.or(&b);
    assert_eq!(or_result.test(0), true);
    assert_eq!(or_result.test(1), true);
    assert_eq!(or_result.test(2), true);
    assert_eq!(or_result.test(3), true);

    // Test XOR operation
    let xor_result = a.xor(&b);
    assert_eq!(xor_result.test(0), true);
    assert_eq!(xor_result.test(1), false);
    assert_eq!(xor_result.test(2), false);
    assert_eq!(xor_result.test(3), true);

    // Test exact byte alignment
    let mut byte_aligned = DynamicBitset::new(8);
    for i in 0..8 {
        byte_aligned.set(i);
    }
    assert_eq!(byte_aligned.bytes[0], 0xff);

    // Test multi-byte operations
    let mut multi = DynamicBitset::new(16);
    multi.set(0);  // byte 0, bit 0
    multi.set(15); // byte 1, bit 7
    assert_eq!(multi.bytes[0], 0x01);
    assert_eq!(multi.bytes[1], 0x80);

    // Verify operations against Vec<bool> for larger set
    let mut vec_a = vec![false; 256];
    let mut vec_b = vec![false; 256];
    let mut bs_a = DynamicBitset::new(256);
    let mut bs_b = DynamicBitset::new(256);

    for i in (0..256).step_by(3) {
        vec_a[i] = true;
        bs_a.set(i);
    }
    for i in (0..256).step_by(5) {
        vec_b[i] = true;
        bs_b.set(i);
    }

    let and_result = bs_a.and(&bs_b);
    for i in 0..256 {
        let expected = vec_a[i] && vec_b[i];
        assert_eq!(and_result.test(i), expected, "AND mismatch at bit {}", i);
    }

    let or_result = bs_a.or(&bs_b);
    for i in 0..256 {
        let expected = vec_a[i] || vec_b[i];
        assert_eq!(or_result.test(i), expected, "OR mismatch at bit {}", i);
    }

    let xor_result = bs_a.xor(&bs_b);
    for i in 0..256 {
        let expected = vec_a[i] != vec_b[i];
        assert_eq!(xor_result.test(i), expected, "XOR mismatch at bit {}", i);
    }

    println!("dynamic_bitset ... PASS");
}
