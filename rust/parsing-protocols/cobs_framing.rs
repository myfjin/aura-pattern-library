#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Consistent Overhead Byte Stuffing (COBS) encoder/decoder for zero-free framing.
// encode replaces zero bytes with a code-byte scheme so the output contains no 0x00 (letting a
// separate 0x00 delimit frames), including the 255-run split for blocks with no zero; decode walks
// the code bytes to restore the original, reinserting an implicit zero only after a short (<0xFF) block.
// Use to frame binary packets over a byte stream where 0x00 marks packet boundaries.
// Guarantees: exact round-trip for arbitrary data (embedded/leading/trailing zeros, all 256 values),
// no 0x00 in the encoding, and decode errors on a 0 code byte or a code that runs past the buffer.
struct Cobs;

impl Cobs {
    fn encode(data: &[u8]) -> Vec<u8> {
        let mut result = Vec::new();
        let mut code_index = 0;
        result.push(0); // Placeholder for code byte

        for &byte in data {
            if byte == 0 {
                result[code_index] = (result.len() - code_index) as u8;
                code_index = result.len();
                result.push(0); // New code byte placeholder
            } else {
                result.push(byte);
                if result.len() - code_index == 255 {
                    result[code_index] = 255;
                    code_index = result.len();
                    result.push(0);
                }
            }
        }

        result[code_index] = (result.len() - code_index) as u8;
        result
    }

    fn decode(data: &[u8]) -> Result<Vec<u8>, String> {
        if data.is_empty() {
            return Ok(Vec::new());
        }

        let mut result = Vec::new();
        let mut pos = 0;

        while pos < data.len() {
            let code = data[pos];
            if code == 0 {
                return Err("invalid COBS code 0".to_string());
            }

            let next_code_pos = pos + code as usize;
            if next_code_pos > data.len() {
                return Err("COBS code points beyond buffer".to_string());
            }

            for i in (pos + 1)..next_code_pos {
                result.push(data[i]);
            }

            pos = next_code_pos;

            // A full block (code == 0xFF) carries 254 data bytes and is NOT terminated by an
            // implicit zero — it was split for length, not by a zero in the input. Only a
            // short block (code < 0xFF) implies a zero, and only if more data follows.
            if code != 0xFF && pos < data.len() {
                result.push(0);
            }
        }

        Ok(result)
    }
}

fn main() {
    // Ground truth: data without null bytes
    let data1 = b"hello";
    let encoded1 = Cobs::encode(data1);
    assert!(!encoded1.contains(&0), "encoded data should not contain 0x00");
    let decoded1 = Cobs::decode(&encoded1).unwrap();
    assert_eq!(decoded1, data1);

    // Ground truth: data with null byte (the key test)
    let data2 = vec![b'a', b'b', 0, b'c', b'd'];
    let encoded2 = Cobs::encode(&data2);
    assert!(!encoded2.contains(&0), "encoded data should not contain 0x00");
    let decoded2 = Cobs::decode(&encoded2).unwrap();
    assert_eq!(decoded2, data2, "roundtrip failed with embedded null");

    // Ground truth: data with multiple null bytes
    let data3 = vec![0, b'a', 0, 0, b'b'];
    let encoded3 = Cobs::encode(&data3);
    assert!(!encoded3.contains(&0));
    let decoded3 = Cobs::decode(&encoded3).unwrap();
    assert_eq!(decoded3, data3);

    // Ground truth: empty data
    let data4: Vec<u8> = vec![];
    let encoded4 = Cobs::encode(&data4);
    let decoded4 = Cobs::decode(&encoded4).unwrap();
    assert_eq!(decoded4, vec![]);

    // Adversarial: all bytes from 0..=255
    let data5: Vec<u8> = (0..=255).collect();
    let encoded5 = Cobs::encode(&data5);
    assert!(!encoded5.contains(&0));
    let decoded5 = Cobs::decode(&encoded5).unwrap();
    assert_eq!(decoded5, data5);

    // Adversarial: repeated nulls
    let data6 = vec![0, 0, 0, 0];
    let encoded6 = Cobs::encode(&data6);
    assert!(!encoded6.contains(&0));
    let decoded6 = Cobs::decode(&encoded6).unwrap();
    assert_eq!(decoded6, data6);

    // Adversarial: corrupt code byte (0x00 in encoded)
    let mut bad = encoded2.clone();
    bad[0] = 0;
    assert!(Cobs::decode(&bad).is_err());

    // Adversarial: code byte points past buffer
    let bad2 = vec![0xFF, b'a', b'b'];
    assert!(Cobs::decode(&bad2).is_err());

    println!("cobs_framing: PASS");
}
