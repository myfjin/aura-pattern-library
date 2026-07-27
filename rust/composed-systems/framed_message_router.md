# framed message router

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(b: u8) → Option<MsgType>`

## What it does

composes: length-prefixed-deframing + type-header-parse + type-routed-dispatch

Real deframing: messages arrive as ONE concatenated byte stream, each framed as
[len:u8][type:u8][payload…] where len = 1 + payload.len(). The deframer walks the buffer using
the length prefixes to recover message boundaries (a truncated trailing frame is left buffered,
not mis-parsed), THEN the type byte routes each payload.

## Guarantee

When it runs, framed message router guarantees assert_eq!(frames.len(), 5, "exactly 5 complete frames deframed; the truncated one is left buffered"); assert_eq!(routed.get("Ping").map(|v| v.len()).unwrap_or(0), 2, "2 Ping"); assert_eq!(routed.get("Data").map(|v| v.len()).unwrap_or(0), 2, "2 Data") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(frames.len(), 5, "exactly 5 complete frames deframed; the truncated one is left buffered")`
- `assert!(consumed < stream.len(), "the truncated trailing frame was NOT consumed")`
- `assert_eq!(routed.get("Ping").map(|v| v.len()).unwrap_or(0), 2, "2 Ping")`
- `assert_eq!(routed.get("Data").map(|v| v.len()).unwrap_or(0), 2, "2 Data")`
- `assert_eq!(routed.get("Ack").map(|v| v.len()).unwrap_or(0), 1, "1 Ack")`
- `assert_eq!(routed.get("Data").unwrap()[1], vec![88], "second Data payload is exactly [88]")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
