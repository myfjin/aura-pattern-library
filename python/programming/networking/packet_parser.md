# packet parser

**Language:** Python · **Sphere:** programming · **Category:** Networking

## What it does

Binary network-packet builder and parser with a trailing checksum.

Use to build and decode a small framed binary protocol: create_packet emits
DATA / ACK / NACK / CONTROL frames (a struct-packed header, optional payload, and
a 2-byte checksum trailer), and parse() decodes fields per the type's field
definitions (which are configurable). Guarantees (proven by self-test): each
type's create->parse round-trip returns every field exactly, including empty and
raw-binary payloads; validate_checksum catches a bit flip anywhere in the frame;
and an unknown packet type is refused at parse and at create.

## Guarantee

When it runs, packet parser guarantees parsed['sequence'] == 42; data_packet.data[0] == 170 and data_packet.data[1] == PacketType.DATA.value; ack_fields['sequence'] == 1000 (proven by run).

**Checkable constraints:**

- `parsed['sequence'] == 42`
- `parsed['payload'] == b'Hello, World!'`
- `parsed['length'] == 6 + 13`
- `data_packet.validate_checksum() is True`
- `data_packet.data[0] == 170 and data_packet.data[1] == PacketType.DATA.value`
- `ack_fields['sequence'] == 1000`
- `ack.validate_checksum() is True`
- `len(ack.data) == 8`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
