# message encoder

**Language:** Python · **Sphere:** programming · **Category:** Architecture

**Signature:** `(encoder_version: MessageFormat, decoder_supported: set) → Tuple[bool, Optional[MessageFormat]]`

## What it does

Message Format Encoder/Decoder Module

This module provides classes for encoding and decoding messages with:
- Length-prefix framing
- Checksum validation
- Version negotiation

## Guarantee

When it runs, message encoder guarantees n_ok == 8; decoded == original; version == fmt.value (proven by run).

**Checkable constraints:**

- `decoded == original`
- `version == fmt.value`
- `encoder.encode('test') != b'test'`
- `version == MessageFormat.V2.value`
- `negotiate_version(MessageFormat.V2, {MessageFormat.V1}) == (False, None)`
- `negotiate_version(MessageFormat.V1, {MessageFormat.V1, MessageFormat.V2}) == (True, MessageFormat.V1)`
- `negotiate_version(MessageFormat.V2, {MessageFormat.V2}) == (True, MessageFormat.V2)`
- `n_ok == 8`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
