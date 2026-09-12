#![forbid(unsafe_code)]
//! Run-length encoding: compress sequences of identical bytes.
//! Core idea: emit (run_byte, count) pairs; single byte encoded as (byte, 1).
//! When to use: simple compression, image data, sparse patterns.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn rle_encode(data: &[u8]) -> Vec<u8> {
    if data.is_empty() {
        return Vec::new();
    }
    let mut result = Vec::new();
    let mut i = 0;
    while i < data.len() {
        let byte = data[i];
        let mut count = 1u8;
        while i + (count as usize) < data.len() && data[i + (count as usize)] == byte && count < 255 {
            count += 1;
        }
        result.push(byte);
        result.push(count);
        i += count as usize;
    }
    result
}

fn rle_decode(encoded: &[u8]) -> Option<Vec<u8>> {
    if encoded.len() % 2 != 0 {
        return None;
    }
    let mut result = Vec::new();
    for chunk in encoded.chunks(2) {
        let byte = chunk[0];
        let count = chunk[1];
        for _ in 0..count {
            result.push(byte);
        }
    }
    Some(result)
}

fn main() {
    // CANONICAL test cases: simple runs
    let tests = vec![
        (b"".to_vec(), b"\x00\x00".to_vec()), // empty → ... wait, encoding empty should yield empty
        (b"aaa".to_vec(), vec![b'a', 3]),
        (b"aaabbb".to_vec(), vec![b'a', 3, b'b', 3]),
        (b"a".to_vec(), vec![b'a', 1]),
        (b"ababab".to_vec(), vec![b'a', 1, b'b', 1, b'a', 1, b'b', 1, b'a', 1, b'b', 1]),
    ];

    for (input, expected_encoded) in &tests[1..] { // skip empty case for now
        let encoded = rle_encode(input);
        assert_eq!(&encoded, expected_encoded, "rle_encode mismatch for {:?}", std::str::from_utf8(input).ok());
        let decoded = rle_decode(&encoded).expect("decode failed");
        assert_eq!(&decoded, input, "rle round-trip mismatch");
    }

    // Test empty
    let empty_encoded = rle_encode(b"");
    assert_eq!(empty_encoded.len(), 0);

    // Long run (up to 255)
    let long_run = vec![42u8; 255];
    let encoded = rle_encode(&long_run);
    assert_eq!(encoded, vec![42, 255]);
    let decoded = rle_decode(&encoded).unwrap();
    assert_eq!(decoded, long_run);

    // Very long run (splits into multiple chunks of 255)
    let very_long_run = vec![99u8; 300];
    let encoded = rle_encode(&very_long_run);
    assert_eq!(encoded, vec![99, 255, 99, 45]); // 255 + 45 = 300
    let decoded = rle_decode(&encoded).unwrap();
    assert_eq!(decoded, very_long_run);

    // Mixed pattern
    let mixed = b"aaaabbccccccaa".to_vec();
    let encoded = rle_encode(&mixed);
    let decoded = rle_decode(&encoded).unwrap();
    assert_eq!(decoded, mixed, "mixed pattern round-trip failed");

    // Property: encoding is reversible
    for pattern in [
        b"".to_vec(),
        b"a".to_vec(),
        b"aabbcc".to_vec(),
        b"aaaaaabbbbbbcccccc".to_vec(),
    ] {
        let enc = rle_encode(&pattern);
        if !pattern.is_empty() {
            let dec = rle_decode(&enc).unwrap();
            assert_eq!(dec, pattern, "reversibility failed for {:?}", pattern);
        } else {
            assert!(enc.is_empty());
        }
    }

    println!("run_length_encode ... PASS");
}
