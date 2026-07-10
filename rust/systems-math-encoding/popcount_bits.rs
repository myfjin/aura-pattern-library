#![forbid(unsafe_code)]
//! Bit population count (Hamming weight) and bit operations from scratch.
//! Core idea: count set bits in an integer; also provide ctz (trailing zeros) and clz (leading zeros).
//! When to use: bit manipulation in protocols, sparse set operations, instruction simulation.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn popcount(mut n: u64) -> u32 {
    let mut count = 0u32;
    while n != 0 {
        count += 1;
        n &= n - 1; // Clear lowest set bit
    }
    count
}

fn ctz(n: u64) -> u32 {
    if n == 0 { return 64; }
    let mut count = 0u32;
    let mut m = n;
    while m & 1 == 0 {
        count += 1;
        m >>= 1;
    }
    count
}

fn clz(n: u64) -> u32 {
    if n == 0 { return 64; }
    let mut count = 0u32;
    let mut m = n;
    while m & (1u64 << 63) == 0 {
        count += 1;
        m <<= 1;
    }
    count
}

fn main() {
    // CANONICAL test vectors: known popcount values
    let tests: Vec<(u64, u32)> = vec![
        (0u64, 0),
        (1u64, 1),
        (3u64, 2),           // 0b11
        (7u64, 3),           // 0b111
        (0xffu64, 8),        // 0xff
        (0xaaaau64, 8),      // alternating bits (10101010...)
        (0x5555u64, 8),      // alternating bits (01010101...)
        (0xffffffffu64, 32), // 32 bits set
        (u64::MAX, 64),      // all bits set
        (0x123456789abcdefu64, 32), // verify against Rust built-in
    ];

    for (value, expected_count) in tests {
        let count = popcount(value);
        assert_eq!(count, expected_count, "popcount({:#x}) = {}, expected {}", value, count, expected_count);
        // Verify against Rust built-in
        let builtin = value.count_ones();
        assert_eq!(count, builtin, "popcount({:#x}) {} != builtin {}", value, count, builtin);
    }

    // ctz (count trailing zeros)
    let ctz_tests: Vec<(u64, u32)> = vec![
        (1u64, 0),
        (2u64, 1),
        (4u64, 2),
        (8u64, 3),
        (0x80u64, 7),
        (0x100u64, 8),
        (u64::MAX & !1, 1), // all but LSB
    ];

    for (value, expected_ctz) in ctz_tests {
        let result = ctz(value);
        assert_eq!(result, expected_ctz, "ctz({:#x}) = {}, expected {}", value, result, expected_ctz);
        let builtin = value.trailing_zeros();
        assert_eq!(result, builtin, "ctz({:#x}) {} != builtin {}", value, result, builtin);
    }

    // clz (count leading zeros)
    let clz_tests: Vec<(u64, u32)> = vec![
        (1u64, 63),
        (0x80u64, 56),
        (0x8000u64, 48),
        (0x8000000000000000u64, 0),
        (0x4000000000000000u64, 1),
    ];

    for (value, expected_clz) in clz_tests {
        let result = clz(value);
        assert_eq!(result, expected_clz, "clz({:#x}) = {}, expected {}", value, result, expected_clz);
        let builtin = value.leading_zeros();
        assert_eq!(result, builtin, "clz({:#x}) {} != builtin {}", value, result, builtin);
    }

    println!("popcount_bits ... PASS");
}
