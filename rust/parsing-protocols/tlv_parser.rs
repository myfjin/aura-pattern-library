#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Parses a byte buffer of consecutive Type-Length-Value records, each a 1-byte type, a
// 1-byte length, then that many value bytes, into a Vec of (type, value) records.
// Use to decode a simple binary wire format with length-prefixed fields.
// Guarantees bounds safety against malicious or truncated input: a length that overruns
// the remaining bytes, or a buffer ending mid-header (missing the length byte), returns
// Err instead of panicking or reading past the end. An empty buffer is valid (zero
// records) and a zero-length value is accepted.
#[derive(Debug, PartialEq, Clone)]
struct TlvRecord {
    type_: u8,
    value: Vec<u8>,
}

struct TlvParser;

impl TlvParser {
    fn parse(data: &[u8]) -> Result<Vec<TlvRecord>, String> {
        let mut records = Vec::new();
        let mut offset = 0;

        while offset < data.len() {
            if offset + 2 > data.len() {
                return Err("truncated TLV: missing type or length".to_string());
            }

            let type_ = data[offset];
            let length = data[offset + 1] as usize;
            offset += 2;

            if offset + length > data.len() {
                return Err(format!(
                    "truncated TLV: length={} but only {} bytes remaining",
                    length,
                    data.len() - offset
                ));
            }

            let value = data[offset..offset + length].to_vec();
            offset += length;

            records.push(TlvRecord { type_, value });
        }

        Ok(records)
    }
}

fn main() {
    // Ground truth: simple TLV record
    let data1 = vec![1, 3, b'a', b'b', b'c'];
    let records1 = TlvParser::parse(&data1).unwrap();
    assert_eq!(records1[0].type_, 1);
    assert_eq!(records1[0].value, vec![b'a', b'b', b'c']);

    // Ground truth: multiple TLV records
    let data2 = vec![
        1, 2, b'a', b'b',
        2, 3, b'x', b'y', b'z',
        3, 1, b'q',
    ];
    let records2 = TlvParser::parse(&data2).unwrap();
    assert_eq!(records2.len(), 3);
    assert_eq!(records2[0].type_, 1);
    assert_eq!(records2[1].type_, 2);
    assert_eq!(records2[2].type_, 3);

    // Ground truth: zero-length value
    let data3 = vec![1, 0, 2, 2, b'x', b'y'];
    let records3 = TlvParser::parse(&data3).unwrap();
    assert_eq!(records3[0].value.len(), 0);
    assert_eq!(records3[1].value, vec![b'x', b'y']);

    // Adversarial: truncated TLV (length says 5 but only 2 bytes available)
    let data4 = vec![1, 5, b'a', b'b'];
    assert!(TlvParser::parse(&data4).is_err());

    // Adversarial: missing type byte
    let data5 = vec![];
    assert!(TlvParser::parse(&data5).is_ok()); // empty stream is valid

    // Adversarial: missing length byte
    let data6 = vec![1];
    assert!(TlvParser::parse(&data6).is_err());

    // Adversarial: length exactly matches remaining, next record starts at buffer end
    let data7 = vec![1, 2, b'a', b'b', 2, 2, b'x', b'y'];
    let records7 = TlvParser::parse(&data7).unwrap();
    assert_eq!(records7.len(), 2);

    // Adversarial: trailing incomplete record
    let data8 = vec![1, 2, b'a', b'b', 2];
    assert!(TlvParser::parse(&data8).is_err());

    println!("tlv_parser: PASS");
}
