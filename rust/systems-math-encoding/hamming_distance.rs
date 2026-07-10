#![forbid(unsafe_code)]
//! Hamming distance: bit-difference count between byte sequences.
//! Core idea: XOR the bytes and count set bits in result.
//! When to use: error detection in transmission, code similarity, bit-pattern diff.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn hamming_distance_bytes(a: &[u8], b: &[u8]) -> Option<u32> {
    if a.len() != b.len() {
        return None;
    }
    let mut distance = 0u32;
    for (x, y) in a.iter().zip(b.iter()) {
        distance += (x ^ y).count_ones();
    }
    Some(distance)
}

fn main() {
    // CANONICAL test cases
    assert_eq!(hamming_distance_bytes(b"", b""), Some(0));
    assert_eq!(hamming_distance_bytes(b"\x00", b"\x00"), Some(0));
    assert_eq!(hamming_distance_bytes(b"\x01", b"\x00"), Some(1));
    assert_eq!(hamming_distance_bytes(b"\xff", b"\x00"), Some(8));
    assert_eq!(hamming_distance_bytes(b"\xaa", b"\x55"), Some(8)); // alternating bits differ completely
    assert_eq!(hamming_distance_bytes(b"abc", b"abc"), Some(0));

    // Known test vectors
    let tests = [
        (&b"1011"[..], &b"1001"[..], 1u32), // strings are ASCII bytes, differ in 1 position
        (&b"abc"[..], &b"abd"[..], (b'c' ^ b'd').count_ones()), // 'c' vs 'd'
    ];

    for (a, b, expected) in &tests {
        let dist = hamming_distance_bytes(a, b).unwrap();
        assert_eq!(dist, *expected, "hamming_distance({:?}, {:?}) = {}, expected {}",
                   std::str::from_utf8(a).unwrap_or("?"),
                   std::str::from_utf8(b).unwrap_or("?"),
                   dist, expected);
    }

    // PROPERTY: symmetry (distance(a, b) == distance(b, a))
    let pairs = [
        (&b"hello"[..], &b"hallo"[..]),
        (&b"\x55\xaa"[..], &b"\x00\xff"[..]),
    ];

    for (a, b) in &pairs {
        let d1 = hamming_distance_bytes(a, b).unwrap();
        let d2 = hamming_distance_bytes(b, a).unwrap();
        assert_eq!(d1, d2, "hamming distance not symmetric");
    }

    // PROPERTY: triangle inequality (distance(a, c) <= distance(a, b) + distance(b, c))
    // Using XOR: ham(a, c) <= ham(a, b) + ham(b, c)
    let a = b"\x00\x00";
    let b = b"\xff\x00";
    let c = b"\xff\xff";

    let d_ac = hamming_distance_bytes(a, c).unwrap();
    let d_ab = hamming_distance_bytes(a, b).unwrap();
    let d_bc = hamming_distance_bytes(b, c).unwrap();
    assert!(d_ac <= d_ab + d_bc, "triangle inequality failed: {} > {} + {}", d_ac, d_ab, d_bc);

    // Length mismatch returns None
    assert_eq!(hamming_distance_bytes(b"ab", b"abc"), None);

    println!("hamming_distance ... PASS");
}
