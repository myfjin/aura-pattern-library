#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct SlipCodec;

impl SlipCodec {
    const END: u8 = 0xC0;
    const ESC: u8 = 0xDB;
    const ESC_END: u8 = 0xDC;
    const ESC_ESC: u8 = 0xDD;

    fn encode(data: &[u8]) -> Vec<u8> {
        let mut result = vec![Self::END];
        for &byte in data {
            match byte {
                Self::END => {
                    result.push(Self::ESC);
                    result.push(Self::ESC_END);
                }
                Self::ESC => {
                    result.push(Self::ESC);
                    result.push(Self::ESC_ESC);
                }
                _ => result.push(byte),
            }
        }
        result.push(Self::END);
        result
    }

    fn decode(data: &[u8]) -> Result<Vec<u8>, String> {
        let mut result = Vec::new();
        let mut i = 0;

        // Skip leading END if present
        if i < data.len() && data[i] == Self::END {
            i += 1;
        }

        while i < data.len() {
            let byte = data[i];
            if byte == Self::END {
                break; // Frame ends
            } else if byte == Self::ESC {
                i += 1;
                if i >= data.len() {
                    return Err("incomplete escape sequence at end".to_string());
                }
                match data[i] {
                    Self::ESC_END => result.push(Self::END),
                    Self::ESC_ESC => result.push(Self::ESC),
                    _ => return Err(format!("invalid escape sequence: ESC 0x{:02x}", data[i])),
                }
            } else {
                result.push(byte);
            }
            i += 1;
        }

        Ok(result)
    }
}

fn main() {
    // Ground truth: simple data without flag/escape bytes
    let data1 = b"hello";
    let encoded1 = SlipCodec::encode(data1);
    assert_eq!(encoded1[0], SlipCodec::END);
    assert_eq!(encoded1[encoded1.len() - 1], SlipCodec::END);
    let decoded1 = SlipCodec::decode(&encoded1).unwrap();
    assert_eq!(decoded1, data1);

    // Ground truth: data containing END byte (the critical test)
    let data2 = vec![b'a', b'b', SlipCodec::END, b'c', b'd'];
    let encoded2 = SlipCodec::encode(&data2);
    // Should not contain END except at frame boundaries
    for (i, &byte) in encoded2.iter().enumerate() {
        if i == 0 || i == encoded2.len() - 1 {
            assert_eq!(byte, SlipCodec::END);
        } else {
            assert_ne!(byte, SlipCodec::END, "unescaped END byte in middle");
        }
    }
    let decoded2 = SlipCodec::decode(&encoded2).unwrap();
    assert_eq!(decoded2, data2, "roundtrip failed with embedded END");

    // Ground truth: data containing ESC byte. Note: unlike END, a raw ESC (0xDB) MUST appear
    // in the framed output — it is the escape-introducer itself (ESC ESC_ESC encodes a data
    // ESC). The real invariant is that every ESC in the frame introduces a valid escape pair,
    // which the roundtrip verifies: a data ESC survives encode→decode intact.
    let data3 = vec![b'x', b'y', SlipCodec::ESC, b'z'];
    let encoded3 = SlipCodec::encode(&data3);
    // The escape marker must be present (data contained an ESC) and always paired with ESC_ESC.
    let esc_pos = encoded3.iter().position(|&b| b == SlipCodec::ESC).expect("ESC must be emitted");
    assert_eq!(encoded3[esc_pos + 1], SlipCodec::ESC_ESC, "ESC must introduce a valid escape");
    let decoded3 = SlipCodec::decode(&encoded3).unwrap();
    assert_eq!(decoded3, data3);

    // Ground truth: all bytes from 0..=255
    let data4: Vec<u8> = (0..=255).collect();
    let encoded4 = SlipCodec::encode(&data4);
    let decoded4 = SlipCodec::decode(&encoded4).unwrap();
    assert_eq!(decoded4, data4);

    // Adversarial: adjacent END and ESC
    let data5 = vec![SlipCodec::END, SlipCodec::ESC];
    let encoded5 = SlipCodec::encode(&data5);
    let decoded5 = SlipCodec::decode(&encoded5).unwrap();
    assert_eq!(decoded5, data5);

    // Adversarial: truncated escape sequence
    let mut bad = SlipCodec::encode(b"test");
    bad.pop(); // Remove final END
    bad.push(SlipCodec::ESC); // Add incomplete escape
    assert!(SlipCodec::decode(&bad).is_err());

    // Adversarial: invalid escape code
    let bad2 = vec![SlipCodec::END, SlipCodec::ESC, 0xFF, SlipCodec::END];
    assert!(SlipCodec::decode(&bad2).is_err());

    println!("slip_escape_framer: PASS");
}
