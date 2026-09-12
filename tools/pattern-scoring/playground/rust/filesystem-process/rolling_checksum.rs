#![forbid(unsafe_code)]
//! rolling_checksum — polynomial rolling checksum for delta sync; O(1) window updates.
//!
//! Core idea: as the window slides one byte, the hash is updated INCREMENTALLY — subtract the
//! outgoing byte's contribution, shift, add the incoming byte — in O(1), not by re-hashing the
//! whole window. THE ONE LAW: compute the rolled hashes, then assert each equals a from-scratch
//! recompute of the same window. If the roll math were wrong, rolled ≠ recompute would catch it
//! (a naive impl that just recomputes would make this test vacuous — so we roll for real).
//! When to use: rsync-like delta detection, content-defined chunking, dedup across chunks.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
const BASE: u64 = 257;
const MODULUS: u64 = 1_000_000_007;

/// From-scratch polynomial hash of a window: sum(byte[j] * BASE^(w-1-j)) mod MODULUS.
fn hash_window(window: &[u8]) -> u64 {
    let mut h = 0u64;
    for &b in window {
        h = (h * BASE + b as u64) % MODULUS;
    }
    h
}

/// Rolling hashes over every window of `w` bytes — each derived from the previous in O(1).
fn rolling_checksums(data: &[u8], w: usize) -> Vec<u64> {
    let n = data.len();
    if w == 0 || w > n {
        return Vec::new();
    }
    // BASE^(w-1) mod MODULUS — the weight of the outgoing (leading) byte.
    let mut base_pow = 1u64;
    for _ in 0..w - 1 {
        base_pow = base_pow * BASE % MODULUS;
    }

    let mut hashes = Vec::with_capacity(n - w + 1);
    let mut h = hash_window(&data[0..w]); // seed the first window from scratch
    hashes.push(h);

    for i in 1..=n - w {
        let outgoing = data[i - 1] as u64;
        let incoming = data[i + w - 1] as u64;
        // Remove the outgoing byte's contribution, shift left one position, add the incoming byte.
        h = (h + MODULUS - outgoing * base_pow % MODULUS) % MODULUS;
        h = (h * BASE + incoming) % MODULUS;
        hashes.push(h);
    }
    hashes
}

fn main() {
    // Case 1: rolled hashes must equal a from-scratch recompute at EVERY position.
    let data = b"hello world";
    let w = 4;
    let rolled = rolling_checksums(data, w);
    assert_eq!(rolled.len(), data.len() - w + 1);
    assert_eq!(rolled.len(), 8);
    for (i, &rh) in rolled.iter().enumerate() {
        let recomputed = hash_window(&data[i..i + w]);
        assert_eq!(rh, recomputed, "rolled hash at {i} disagrees with recompute");
    }

    // Case 2: identical windows produce identical hashes ("abc" at 0, 3, 6); different windows differ.
    let data2 = b"abcabcabc";
    let r2 = rolling_checksums(data2, 3);
    let h_abc = hash_window(b"abc");
    assert_eq!(r2[0], h_abc);
    assert_eq!(r2[3], h_abc);
    assert_eq!(r2[6], h_abc);
    assert_ne!(r2[1], r2[0], "\"bca\" must differ from \"abc\"");

    // Case 3: distinct 5-grams in a string with no repeats → all hashes distinct.
    let data3 = b"thequickbrownfox";
    let r3 = rolling_checksums(data3, 5);
    let distinct = r3.iter().collect::<std::collections::HashSet<_>>().len();
    assert_eq!(distinct, r3.len(), "distinct windows must hash distinctly here");

    // Case 4: prove the roll is REAL — an off-by-one in the update would break the recompute match.
    // Exhaustively re-verify over a longer buffer and a few window sizes.
    let data4 = b"the quick brown fox jumps over the lazy dog";
    for w in [1usize, 2, 3, 7, 11] {
        let rolled = rolling_checksums(data4, w);
        for (i, &rh) in rolled.iter().enumerate() {
            assert_eq!(rh, hash_window(&data4[i..i + w]), "w={w} pos={i} roll≠recompute");
        }
    }

    println!("rolling_checksum: O(1) rolled hashes equal from-scratch recompute at every window — PASS");
}
