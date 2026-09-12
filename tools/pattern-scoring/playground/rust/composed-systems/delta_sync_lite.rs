#![forbid(unsafe_code)]
//! delta_sync_lite — rsync-style block delta: match shared blocks old↔new, transfer + RECONSTRUCT.
//!
//! Core idea: chunk OLD into fixed blocks and index them by hash. Scan NEW: where a window
//! matches an old block, emit a COPY(offset) (no data sent); otherwise emit a LITERAL byte. The
//! delta = that op stream. Applying the delta against OLD must reconstruct NEW EXACTLY — that
//! reconstruction is the whole point (a rolling hash alone does not sync). THE LAW: build the
//! delta, reconstruct and assert bytes-identical to NEW, prove blocks were actually reused (fewer
//! literals than a full copy), then CORRUPT the source and assert reconstruction diverges.
//! When to use: rsync-like transfer, incremental backup, block dedup.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashMap;

const B: usize = 4; // block size

#[derive(Clone, PartialEq, Debug)]
enum Op {
    Copy(usize), // copy B bytes from old at this offset
    Literal(u8),
}

fn block_hash(block: &[u8]) -> u64 {
    let mut h = 1469598103934665603u64; // FNV-1a
    for &b in block {
        h ^= b as u64;
        h = h.wrapping_mul(1099511628211);
    }
    h
}

fn diff(old: &[u8], new: &[u8]) -> Vec<Op> {
    // Index non-overlapping old blocks by hash (first offset wins).
    let mut index: HashMap<u64, usize> = HashMap::new();
    let mut off = 0;
    while off + B <= old.len() {
        index.entry(block_hash(&old[off..off + B])).or_insert(off);
        off += B;
    }

    let mut ops = Vec::new();
    let mut i = 0;
    while i < new.len() {
        if i + B <= new.len() {
            if let Some(&o) = index.get(&block_hash(&new[i..i + B])) {
                if old[o..o + B] == new[i..i + B] {
                    // real match (guard against hash collision)
                    ops.push(Op::Copy(o));
                    i += B;
                    continue;
                }
            }
        }
        ops.push(Op::Literal(new[i]));
        i += 1;
    }
    ops
}

fn apply(old: &[u8], ops: &[Op]) -> Vec<u8> {
    let mut out = Vec::new();
    for op in ops {
        match *op {
            Op::Copy(o) => out.extend_from_slice(&old[o..o + B]),
            Op::Literal(b) => out.push(b),
        }
    }
    out
}

fn main() {
    let old = b"the quick brown fox jumps over the lazy dog!".to_vec(); // len 44 (multiple of 4)
    // NEW differs by a single byte in the middle (alignment preserved → most blocks reused).
    let mut new = old.clone();
    new[21] ^= 0x20; // flip one byte

    let ops = diff(&old, &new);

    // THE CORE: applying the delta to OLD reconstructs NEW byte-for-byte.
    let rebuilt = apply(&old, &ops);
    assert_eq!(rebuilt, new, "reconstruction must equal NEW exactly");

    // Blocks were genuinely reused — far fewer literals than a full-literal transfer.
    let literals = ops.iter().filter(|o| matches!(o, Op::Literal(_))).count();
    let copies = ops.iter().filter(|o| matches!(o, Op::Copy(_))).count();
    assert!(copies > 0, "at least one shared block must be COPY-referenced");
    assert!(literals < new.len(), "delta sends fewer literals than the whole file ({literals} < {})", new.len());

    // Identical old==new → an all-Copy delta, zero literals.
    let ops_same = diff(&old, &old);
    assert_eq!(apply(&old, &ops_same), old, "identical inputs reconstruct exactly");
    assert_eq!(ops_same.iter().filter(|o| matches!(o, Op::Literal(_))).count(), 0, "identical → no literals");

    // THE DISASTER: corrupt the SOURCE the delta copies from → reconstruction diverges from NEW.
    let mut corrupted_old = old.clone();
    corrupted_old[0] ^= 0x01; // a byte inside a block that COPY references
    let rebuilt_bad = apply(&corrupted_old, &ops);
    assert_ne!(rebuilt_bad, new, "corrupting the copy source must break reconstruction");

    println!("delta_sync_lite: {copies} copies + {literals} literals reconstruct NEW exactly — PASS");
}
