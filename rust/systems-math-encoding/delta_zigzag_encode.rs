#![forbid(unsafe_code)]
//! Delta-encoding + zigzag: compress sequences with small deltas.
//! Core idea: store first value, then encode (value[i] - value[i-1]) as zigzag varints.
//! When to use: time series, monotonic sequences, low-entropy deltas.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn zigzag_encode(n: i64) -> u64 {
    ((n << 1) ^ (n >> 63)) as u64
}

fn zigzag_decode(n: u64) -> i64 {
    ((n >> 1) as i64) ^ -((n & 1) as i64)
}

fn varint_encode(mut n: u64) -> Vec<u8> {
    let mut result = Vec::new();
    loop {
        let mut byte = (n & 0x7f) as u8;
        n >>= 7;
        if n != 0 {
            byte |= 0x80;
        }
        result.push(byte);
        if n == 0 { break; }
    }
    result
}

fn varint_decode(bytes: &[u8], offset: &mut usize) -> Option<u64> {
    let mut result = 0u64;
    for i in 0..10 {
        if *offset >= bytes.len() { return None; }
        let byte = bytes[*offset];
        *offset += 1;
        result |= ((byte & 0x7f) as u64) << (7 * i);
        if byte & 0x80 == 0 {
            return Some(result);
        }
    }
    None
}

fn delta_zigzag_encode(values: &[i64]) -> Vec<u8> {
    if values.is_empty() {
        return Vec::new();
    }
    let mut result = Vec::new();
    // Store first value as zigzag varint
    let zig = zigzag_encode(values[0]);
    result.extend(varint_encode(zig));
    // Store deltas
    for i in 1..values.len() {
        let delta = values[i] - values[i - 1];
        let zig = zigzag_encode(delta);
        result.extend(varint_encode(zig));
    }
    result
}

fn delta_zigzag_decode(data: &[u8]) -> Option<Vec<i64>> {
    if data.is_empty() {
        return Some(Vec::new());
    }
    let mut result = Vec::new();
    let mut offset = 0;
    // Decode first value
    let first_zig = varint_decode(data, &mut offset)?;
    let first = zigzag_decode(first_zig);
    result.push(first);
    // Decode deltas
    while offset < data.len() {
        let delta_zig = varint_decode(data, &mut offset)?;
        let delta = zigzag_decode(delta_zig);
        result.push(result.last().unwrap() + delta);
    }
    Some(result)
}

fn main() {
    // CANONICAL test: known sequence with encoded bytes
    let sequence = vec![0i64, 1, 3, 6, 10]; // triangular numbers: 0, 0+1, 1+2, 3+3, 6+4
    let encoded = delta_zigzag_encode(&sequence);

    // Manually verify encoding:
    // first value: zigzag(0) = 0 → varint [0x00]
    // deltas: 1, 2, 3, 4 → zigzag: 2, 4, 6, 8 → varint: [0x02, 0x04, 0x06, 0x08]
    // Expected: [0x00, 0x02, 0x04, 0x06, 0x08]
    let expected = vec![0x00, 0x02, 0x04, 0x06, 0x08];
    assert_eq!(encoded, expected, "delta_zigzag encode mismatch for {:?}", sequence);

    // Round-trip
    let decoded = delta_zigzag_decode(&encoded).expect("decode failed");
    assert_eq!(decoded, sequence, "delta_zigzag round-trip failed");

    // Test case 2: negative values with small deltas
    let sequence2 = vec![-10i64, -9, -7, -4, 0]; // deltas: 1, -2, 3, 4
    let encoded2 = delta_zigzag_encode(&sequence2);
    let decoded2 = delta_zigzag_decode(&encoded2).expect("decode failed");
    assert_eq!(decoded2, sequence2, "delta_zigzag round-trip failed for {:?}", sequence2);

    // Test case 3: empty
    let empty: Vec<i64> = vec![];
    let enc_empty = delta_zigzag_encode(&empty);
    assert_eq!(enc_empty.len(), 0);
    let dec_empty = delta_zigzag_decode(&enc_empty).unwrap();
    assert_eq!(dec_empty.len(), 0);

    // Test case 4: single value
    let single = vec![42i64];
    let enc_single = delta_zigzag_encode(&single);
    let dec_single = delta_zigzag_decode(&enc_single).unwrap();
    assert_eq!(dec_single, single);

    // Property: small deltas compress better than absolute values
    let large_sequence = vec![1000000i64, 1000001, 1000003, 1000006, 1000010];
    let delta_encoded = delta_zigzag_encode(&large_sequence);

    // Compare with direct zigzag encoding (no delta)
    let mut direct_encoded = Vec::new();
    for &val in &large_sequence {
        let zig = zigzag_encode(val);
        direct_encoded.extend(varint_encode(zig));
    }

    // delta encoding should be significantly smaller due to small deltas
    assert!(delta_encoded.len() < direct_encoded.len(),
            "delta encoding {} should be < direct {}", delta_encoded.len(), direct_encoded.len());

    println!("delta_zigzag_encode ... PASS");
}
