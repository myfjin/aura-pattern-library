#![forbid(unsafe_code)]
// composes: length-prefixed-deframing + type-header-parse + type-routed-dispatch
//
// Real deframing: messages arrive as ONE concatenated byte stream, each framed as
// [len:u8][type:u8][payload…] where len = 1 + payload.len(). The deframer walks the buffer using
// the length prefixes to recover message boundaries (a truncated trailing frame is left buffered,
// not mis-parsed), THEN the type byte routes each payload.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashMap;

#[derive(Debug, Clone, PartialEq)]
enum MsgType {
    Ping,
    Data,
    Ack,
}

fn type_of(b: u8) -> Option<MsgType> {
    match b {
        1 => Some(MsgType::Ping),
        2 => Some(MsgType::Data),
        3 => Some(MsgType::Ack),
        _ => None,
    }
}

// Deframe as many complete frames as the buffer holds; return (frames, bytes_consumed).
// Each frame is (type_byte, payload). A partial trailing frame is NOT consumed.
fn deframe(buf: &[u8]) -> (Vec<(u8, Vec<u8>)>, usize) {
    let mut frames = Vec::new();
    let mut pos = 0;
    while pos < buf.len() {
        let len = buf[pos] as usize; // length of (type + payload)
        if len == 0 || pos + 1 + len > buf.len() {
            break; // incomplete frame → stop, leave it buffered
        }
        let frame = &buf[pos + 1..pos + 1 + len];
        frames.push((frame[0], frame[1..].to_vec()));
        pos += 1 + len;
    }
    (frames, pos)
}

fn main() {
    // Stage 1: a single concatenated stream of 5 complete frames + a truncated 6th.
    let mut stream: Vec<u8> = Vec::new();
    let msgs: [(u8, &[u8]); 5] = [
        (1, &[72, 105]), // Ping "Hi"
        (2, &[72, 73]),  // Data "HI"
        (1, &[72, 105]), // Ping "Hi"
        (3, &[]),        // Ack (empty payload)
        (2, &[88]),      // Data "X"
    ];
    for (t, payload) in msgs.iter() {
        stream.push((1 + payload.len()) as u8); // len = type + payload
        stream.push(*t);
        stream.extend_from_slice(payload);
    }
    // Append a truncated frame: claims a 3-byte body but only 1 byte follows.
    stream.push(3);
    stream.push(1);
    stream.push(72); // missing the rest

    // Stage 2: deframe using the length prefixes.
    let (frames, consumed) = deframe(&stream);
    assert_eq!(frames.len(), 5, "exactly 5 complete frames deframed; the truncated one is left buffered");
    assert!(consumed < stream.len(), "the truncated trailing frame was NOT consumed");

    // Stage 3: parse type + route.
    let mut routed: HashMap<String, Vec<Vec<u8>>> = HashMap::new();
    for (type_byte, payload) in frames {
        if let Some(mt) = type_of(type_byte) {
            routed.entry(format!("{mt:?}")).or_default().push(payload);
        }
    }

    assert_eq!(routed.get("Ping").map(|v| v.len()).unwrap_or(0), 2, "2 Ping");
    assert_eq!(routed.get("Data").map(|v| v.len()).unwrap_or(0), 2, "2 Data");
    assert_eq!(routed.get("Ack").map(|v| v.len()).unwrap_or(0), 1, "1 Ack");
    // Payloads were deframed cleanly (the length byte is NOT part of the payload).
    assert_eq!(routed.get("Data").unwrap()[1], vec![88], "second Data payload is exactly [88]");

    println!("framed_message_router: PASS");
}
