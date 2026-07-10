#![forbid(unsafe_code)]
//! Reverse bit order in an integer.
//! Core idea: swap bits from outside-in; double reverse is identity.
//! When to use: bitstream reversal, certain signal processing, DSP algorithms.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn reverse_bits_8(n: u8) -> u8 {
    let mut result = 0u8;
    let mut m = n;
    for _ in 0..8 {
        result = (result << 1) | (m & 1);
        m >>= 1;
    }
    result
}

fn reverse_bits_16(n: u16) -> u16 {
    let mut result = 0u16;
    let mut m = n;
    for _ in 0..16 {
        result = (result << 1) | (m & 1) as u16;
        m >>= 1;
    }
    result
}

fn reverse_bits_32(n: u32) -> u32 {
    let mut result = 0u32;
    let mut m = n;
    for _ in 0..32 {
        result = (result << 1) | (m & 1);
        m >>= 1;
    }
    result
}

fn reverse_bits_64(n: u64) -> u64 {
    let mut result = 0u64;
    let mut m = n;
    for _ in 0..64 {
        result = (result << 1) | (m & 1);
        m >>= 1;
    }
    result
}

fn main() {
    // CANONICAL 8-bit tests
    assert_eq!(reverse_bits_8(0x01), 0x80);  // 00000001 → 10000000
    assert_eq!(reverse_bits_8(0x80), 0x01);  // 10000000 → 00000001
    assert_eq!(reverse_bits_8(0xaa), 0x55);  // 10101010 → 01010101
    assert_eq!(reverse_bits_8(0x55), 0xaa);  // 01010101 → 10101010
    assert_eq!(reverse_bits_8(0xff), 0xff);  // 11111111 → 11111111
    assert_eq!(reverse_bits_8(0x00), 0x00);  // 00000000 → 00000000
    assert_eq!(reverse_bits_8(0b00001010), 0b01010000); // 0000_1010 → 0101_0000

    // CANONICAL 16-bit tests
    assert_eq!(reverse_bits_16(0x0001), 0x8000);
    assert_eq!(reverse_bits_16(0x8000), 0x0001);
    assert_eq!(reverse_bits_16(0xaaaa), 0x5555);
    assert_eq!(reverse_bits_16(0xffff), 0xffff);

    // CANONICAL 32-bit tests
    assert_eq!(reverse_bits_32(0x00000001), 0x80000000);
    assert_eq!(reverse_bits_32(0x80000000), 0x00000001);
    assert_eq!(reverse_bits_32(0xaaaaaaaa), 0x55555555);

    // 64-bit tests
    assert_eq!(reverse_bits_64(0x0000000000000001), 0x8000000000000000);
    assert_eq!(reverse_bits_64(0x8000000000000000), 0x0000000000000001);

    // PROPERTY: double reverse == identity
    let test_values_8 = [0, 1, 0x7f, 0x80, 0xaa, 0x55, 0xab, 0xff];
    for val in test_values_8 {
        let rev1 = reverse_bits_8(val);
        let rev2 = reverse_bits_8(rev1);
        assert_eq!(rev2, val, "8-bit double reverse failed for {:#x}", val);
    }

    let test_values_16 = [0, 1, 0x7fff, 0x8000, 0xaaaa, 0x5555, 0xffff];
    for val in test_values_16 {
        let rev1 = reverse_bits_16(val);
        let rev2 = reverse_bits_16(rev1);
        assert_eq!(rev2, val, "16-bit double reverse failed for {:#x}", val);
    }

    let test_values_32 = [0, 1, 0x7fffffff, 0x80000000, 0xaaaaaaaa, 0x55555555, 0xffffffff];
    for val in test_values_32 {
        let rev1 = reverse_bits_32(val);
        let rev2 = reverse_bits_32(rev1);
        assert_eq!(rev2, val, "32-bit double reverse failed for {:#x}", val);
    }

    println!("reverse_bits ... PASS");
}
