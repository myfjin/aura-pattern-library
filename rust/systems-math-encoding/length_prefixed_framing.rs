#![forbid(unsafe_code)]
//! Length-prefixed framing: u32 big-endian length prefix + message bytes.
//! Core idea: each message preceded by 4-byte big-endian length; streams are parsed sequentially.
//! When to use: binary protocols, framed message transmission, delimited records.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn encode_frame(msg: &[u8]) -> Vec<u8> {
    let len = msg.len() as u32;
    let mut result = Vec::new();
    result.extend(&len.to_be_bytes());
    result.extend(msg);
    result
}

fn decode_frames(data: &[u8]) -> Result<Vec<Vec<u8>>, &'static str> {
    let mut frames = Vec::new();
    let mut offset = 0;

    while offset < data.len() {
        if offset + 4 > data.len() {
            return Err("incomplete length prefix");
        }

        let len_bytes = [data[offset], data[offset + 1], data[offset + 2], data[offset + 3]];
        let len = u32::from_be_bytes(len_bytes) as usize;
        offset += 4;

        if offset + len > data.len() {
            return Err("incomplete message");
        }

        frames.push(data[offset..offset + len].to_vec());
        offset += len;
    }

    Ok(frames)
}

fn main() {
    // Test single message
    let msg1 = b"hello";
    let encoded1 = encode_frame(msg1);
    let expected1 = [0, 0, 0, 5, b'h', b'e', b'l', b'l', b'o'];
    assert_eq!(&encoded1, &expected1);

    let decoded1 = decode_frames(&encoded1).expect("decode failed");
    assert_eq!(decoded1.len(), 1);
    assert_eq!(&decoded1[0], msg1);

    // Test multiple messages
    let msg_a = b"foo";
    let msg_b = b"bar";
    let msg_c = b"baz";

    let mut stream = Vec::new();
    stream.extend(&encode_frame(msg_a));
    stream.extend(&encode_frame(msg_b));
    stream.extend(&encode_frame(msg_c));

    let decoded = decode_frames(&stream).expect("decode failed");
    assert_eq!(decoded.len(), 3);
    assert_eq!(&decoded[0], msg_a);
    assert_eq!(&decoded[1], msg_b);
    assert_eq!(&decoded[2], msg_c);

    // Test empty message
    let empty = b"";
    let encoded_empty = encode_frame(empty);
    assert_eq!(&encoded_empty, &[0, 0, 0, 0]);
    let decoded_empty = decode_frames(&encoded_empty).expect("decode failed");
    assert_eq!(decoded_empty.len(), 1);
    assert_eq!(decoded_empty[0].len(), 0);

    // Test incomplete frames (should fail)
    assert!(decode_frames(&[0, 0, 0]).is_err(), "incomplete length should fail");
    assert!(decode_frames(&[0, 0, 0, 5, b'h', b'i']).is_err(), "incomplete message should fail");

    // Test large message
    let large_msg: Vec<u8> = (0..1000).map(|i| (i % 256) as u8).collect();
    let encoded_large = encode_frame(&large_msg);
    let decoded_large = decode_frames(&encoded_large).expect("decode large failed");
    assert_eq!(decoded_large.len(), 1);
    assert_eq!(&decoded_large[0], &large_msg);

    // Test multiple frames with various sizes
    let mut multi = Vec::new();
    let messages = [
        vec![],
        vec![1],
        vec![1, 2, 3, 4, 5],
        vec![255; 100],
        vec![0; 1000],
    ];

    for msg in &messages {
        multi.extend(&encode_frame(msg));
    }

    let decoded_multi = decode_frames(&multi).expect("decode multi failed");
    assert_eq!(decoded_multi.len(), messages.len());
    for (i, msg) in messages.iter().enumerate() {
        assert_eq!(&decoded_multi[i], msg, "message {} mismatch", i);
    }

    // Test exact byte-for-byte stream reconstruction
    let reconstructed: Vec<u8> = decoded_multi.iter()
        .flat_map(|msg| {
            let mut frame = Vec::new();
            frame.extend(&(msg.len() as u32).to_be_bytes());
            frame.extend(msg);
            frame
        })
        .collect();
    assert_eq!(reconstructed, multi, "stream reconstruction mismatch");

    println!("length_prefixed_framing ... PASS");
}
