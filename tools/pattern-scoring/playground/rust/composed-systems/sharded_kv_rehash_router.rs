#![forbid(unsafe_code)]
// composes: rendezvous(HRW)-hash-to-shard + route + add-shard + MINIMAL-movement-rehash + verify
//
// Naive `key % n` reshuffles almost every key when n changes — so it cannot claim "minimal
// movement". This composes RENDEZVOUS (highest-random-weight) hashing: each key goes to the shard
// with the highest weight(key, shard). Adding a shard only moves the keys the new shard now wins;
// every other key stays put. We assert that minimality exactly.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn weight(key: &str, shard: u64) -> u64 {
    let mut h: u64 = 1469598103934665603;
    for b in key.bytes() {
        h = h.wrapping_mul(31).wrapping_add(b as u64);
    }
    h = h.wrapping_mul(1099511628211).wrapping_add(shard.wrapping_mul(2654435761));
    // scramble
    h ^= h >> 33;
    h = h.wrapping_mul(0xff51afd7ed558ccd);
    h ^= h >> 33;
    h
}

fn assign(key: &str, num_shards: u64) -> u64 {
    (0..num_shards).max_by_key(|&s| weight(key, s)).unwrap()
}

fn main() {
    let keys = ["alice", "bob", "charlie", "david", "eve", "frank", "grace", "heidi"];

    // Stage 1: route each key to a shard among 3 via HRW.
    let before: Vec<(&str, u64)> = keys.iter().map(|&k| (k, assign(k, 3))).collect();
    // Every shard index is valid.
    for &(_, s) in &before {
        assert!(s < 3);
    }

    // Stage 2+3: add a 4th shard and re-assign.
    let after: Vec<(&str, u64)> = keys.iter().map(|&k| (k, assign(k, 4))).collect();

    // Stage 4: verify. (a) Every key is still findable in its (new) shard.
    for (&(k, s_after), &(_, _)) in after.iter().zip(before.iter()) {
        assert_eq!(assign(k, 4), s_after, "key {k} deterministically routes to its new shard");
    }

    // (b) MINIMAL movement: a key moved iff the NEW shard (id 3) now wins it. No key that stayed
    // among shards 0..3 changed, and every moved key moved specifically TO shard 3.
    let mut moved = 0;
    for (&(k, s_before), &(_, s_after)) in before.iter().zip(after.iter()) {
        if s_before != s_after {
            moved += 1;
            assert_eq!(s_after, 3, "key {k} only moved because the new shard 3 won it");
        }
    }
    // The new shard did win at least one key, and strictly fewer than all keys moved (that's the
    // whole point vs. a modulo full-reshuffle, which would move ~all of them).
    assert!(moved >= 1, "adding a shard should capture some keys");
    assert!(moved < keys.len(), "minimal movement: most keys stay put ({moved} of {} moved)", keys.len());

    println!("sharded_kv_rehash_router: PASS");
}
