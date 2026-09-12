#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Decoder for HTTP/1.1-style chunked transfer encoding (line-oriented variant).
// Reads a hex chunk-size line, then a data line, appends it, and repeats until a size of 0
// terminates the stream; the declared hex size is checked against the actual data-line length.
// Use to reassemble a body sent in length-prefixed chunks and to reject a malformed/lying stream.
// Guarantees: errors on a size/data length mismatch (a chunk that lies about its length), invalid
// hex in the size line, an empty size line, or a stream that ends before the terminating 0 chunk.
struct ChunkedDecoder;

impl ChunkedDecoder {
    fn decode(data: &str) -> Result<String, String> {
        let mut result = String::new();
        let mut lines = data.lines();

        loop {
            let size_line = match lines.next() {
                Some(line) => line.trim(),
                None => return Err("unexpected end of chunked stream".to_string()),
            };

            if size_line.is_empty() {
                return Err("empty size line".to_string());
            }

            let chunk_size = usize::from_str_radix(size_line, 16)
                .map_err(|_| format!("invalid chunk size: {}", size_line))?;

            if chunk_size == 0 {
                // End of chunks
                break;
            }

            let chunk = match lines.next() {
                Some(line) => line,
                None => return Err("missing chunk data".to_string()),
            };

            if chunk.len() != chunk_size {
                return Err(format!(
                    "chunk size mismatch: expected {}, got {}",
                    chunk_size,
                    chunk.len()
                ));
            }

            result.push_str(chunk);
        }

        Ok(result)
    }
}

fn main() {
    // Ground truth: simple chunked message
    let chunked1 = "5\nhello\n5\nworld\n0\n";
    let decoded1 = ChunkedDecoder::decode(chunked1).unwrap();
    assert_eq!(decoded1, "helloworld");

    // Ground truth: single chunk
    let chunked2 = "4\ntest\n0\n";
    let decoded2 = ChunkedDecoder::decode(chunked2).unwrap();
    assert_eq!(decoded2, "test");

    // Ground truth: hex chunk size
    let chunked3 = "a\n0123456789\n0\n";
    let decoded3 = ChunkedDecoder::decode(chunked3).unwrap();
    assert_eq!(decoded3, "0123456789");

    // Ground truth: multiple chunks
    let chunked4 = "3\nabc\n2\nde\n4\nfghi\n0\n";
    let decoded4 = ChunkedDecoder::decode(chunked4).unwrap();
    assert_eq!(decoded4, "abcdefghi");

    // Adversarial: lying chunk size (claims 5 but provides 3)
    let chunked5 = "5\nabc\n0\n";
    assert!(ChunkedDecoder::decode(chunked5).is_err());

    // Adversarial: invalid hex in chunk size
    let chunked6 = "zz\ndata\n0\n";
    assert!(ChunkedDecoder::decode(chunked6).is_err());

    // Adversarial: truncated stream (missing final 0 chunk)
    let chunked7 = "3\nabc\n";
    assert!(ChunkedDecoder::decode(chunked7).is_err());

    // Adversarial: empty size line
    let chunked8 = "\ndata\n0\n";
    assert!(ChunkedDecoder::decode(chunked8).is_err());

    // Adversarial: chunk size underflow (expects more than provided)
    let chunked9 = "10\nhello\n0\n";
    assert!(ChunkedDecoder::decode(chunked9).is_err());

    println!("chunked_transfer_decoder: PASS");
}
