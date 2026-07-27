# graceful shutdown sigterm

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 1 · Process Supervision & Immortality

## What it does

graceful_shutdown_sigterm: install SIGTERM handler, save state gracefully, and exit.

On receiving SIGTERM the handler writes a state file, then the process exits
 cleanly. The disaster test sends SIGTERM to a child process and asserts that
 the handler ran and the expected state was saved.

## Guarantee

When it runs, graceful shutdown sigterm guarantees content == expected_content; os.path.exists(state_file) (proven by run).

**Checkable constraints:**

- `os.path.exists(state_file)`
- `content == expected_content`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
