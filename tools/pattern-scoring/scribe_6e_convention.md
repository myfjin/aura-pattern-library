
## Building files & running commands — the SCRIBE convention (your hands are external)

Your Write/Bash tool-calls do not always fire — you reason correctly but the execution step
can be skipped, so a file you "wrote" may not exist. Do NOT trust your own tool-calls for
creating artifacts. Instead, emit the artifact as TEXT and let the relay's scribe (which runs
OUTSIDE your execution and cannot be confabulated) do the real write and report the real result.

To create a file, emit exactly:

    ===FILE:/absolute/path/to/file===
    <the full file content, verbatim>
    ===END===

To run a command, emit exactly:

    ===RUN:<shell command>===

The scribe materializes these on real disk / runs them for real, and appends a
`SCRIBE_OK: <path> (N bytes on disk)` or `SCRIBE_FAIL: ...` line to your reply — that line is
disk truth, not your claim. Destructive commands (rm, mv, dd…) are refused by the scribe guard.

RULE: never say "I built X" or "the file exists." Emit the ===FILE=== block and let the
SCRIBE_OK line prove it. Your text is reliable; your tool-hands are not; the scribe is the hand
you can trust.
