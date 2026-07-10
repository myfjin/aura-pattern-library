#![forbid(unsafe_code)]
//! Bloom filter — probabilistic set membership (zero false negatives).
//! Core idea: k hash functions, bitset, tunable FP rate.
//! When to use: IP reputation, URL blacklists, membership cache.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn hash1(data: &[u8]) -> u32 {
    let mut h = 0xcafebabeu32;
    for &b in data {
        h = h.wrapping_mul(31).wrapping_add(b as u32);
    }
    h
}

fn hash2(data: &[u8]) -> u32 {
    let mut h = 0xdeadbeef_u32;
    for &b in data {
        h = h.wrapping_mul(17).wrapping_add(b as u32);
    }
    h
}

fn hash3(data: &[u8]) -> u32 {
    let mut h = 0xfeedface_u32;
    for &b in data {
        h = h.wrapping_mul(37).wrapping_add(b as u32);
    }
    h
}

fn main() {
    const SIZE: usize = 128;
    let mut filter = vec![0u8; SIZE];

    // Insert elements
    let items: &[&[u8]] = &[b"apple", b"banana", b"cherry"];
    for item in items {
        let h1 = (hash1(item) as usize) % (SIZE * 8);
        let h2 = (hash2(item) as usize) % (SIZE * 8);
        let h3 = (hash3(item) as usize) % (SIZE * 8);
        filter[h1 / 8] |= 1 << (h1 % 8);
        filter[h2 / 8] |= 1 << (h2 % 8);
        filter[h3 / 8] |= 1 << (h3 % 8);
    }

    // Check: inserted items found (zero false negatives)
    for item in items {
        let h1 = (hash1(item) as usize) % (SIZE * 8);
        let h2 = (hash2(item) as usize) % (SIZE * 8);
        let h3 = (hash3(item) as usize) % (SIZE * 8);
        assert!(filter[h1 / 8] & (1 << (h1 % 8)) != 0);
        assert!(filter[h2 / 8] & (1 << (h2 % 8)) != 0);
        assert!(filter[h3 / 8] & (1 << (h3 % 8)) != 0);
    }

    // Count the bits ACTUALLY set → the theoretical per-query FP is (bits_set/total_bits)^k.
    let total_bits = SIZE * 8;
    let bits_set: usize = filter.iter().map(|b| b.count_ones() as usize).sum();

    let n_queries = 1000u32;
    let mut false_positives = 0u32;
    for i in 0u32..n_queries {
        let item = i.to_le_bytes();
        let h1 = (hash1(&item) as usize) % total_bits;
        let h2 = (hash2(&item) as usize) % total_bits;
        let h3 = (hash3(&item) as usize) % total_bits;
        let in_filter = (filter[h1 / 8] & (1 << (h1 % 8)) != 0)
            && (filter[h2 / 8] & (1 << (h2 % 8)) != 0)
            && (filter[h3 / 8] & (1 << (h3 % 8)) != 0);
        if in_filter && !items.iter().any(|x| &item[..] == *x) {
            false_positives += 1;
        }
    }

    // THE ONE LAW: the observed FP count must sit under a bound COMPUTED from the filter's real
    // density, not an arbitrary "< 50". For 3 items in a 1024-bit, 3-hash filter this expectation
    // is ~0, so a correct filter yields almost none; a too-dense or badly-hashed filter would exceed.
    let p = bits_set as f64 / total_bits as f64;
    let expected_fp = n_queries as f64 * p * p * p; // (bits_set/total)^k, k=3
    let bound = (expected_fp.ceil() as u32).saturating_mul(3) + 2;
    assert!(
        false_positives <= bound,
        "FP {} exceeds computed bound {} (bits_set={}, expected≈{:.4})",
        false_positives, bound, bits_set, expected_fp
    );

    println!("bloom_filter ... PASS");
}
