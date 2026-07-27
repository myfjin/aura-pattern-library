# mount disk usage

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 15 · Process/system introspection

**Signature:** `(df_text: str) → ?`

## What it does

mount_disk_usage: Parse mount output and extract filesystem usage.
THE ONE LAW: Parse real df-style output, assert exact usage percentages.

## Guarantee

When it runs, mount disk usage guarantees root['size_kb'] == 1024000; root['used_kb'] == 512000; root['avail_kb'] == 512000 (proven by run).

**Checkable constraints:**

- `len(filesystems) == 3`
- `len(root_fs) == 1`
- `root['fs'] == '/dev/sda1'`
- `root['size_kb'] == 1024000`
- `root['used_kb'] == 512000`
- `root['avail_kb'] == 512000`
- `root['use_pct'] == 50`
- `home['use_pct'] == 50`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
