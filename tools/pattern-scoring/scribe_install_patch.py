#!/usr/bin/env python3
"""Idempotent patcher: add scribe to relay.py. Adds import + the hook before send(chat_id, reply)."""
import io, sys, ast
P = sys.argv[1] if len(sys.argv) > 1 else "/home/bu/relay.py"
s = io.open(P, encoding="utf-8").read()
if "scribe_process" in s:
    print("ALREADY PATCHED — no change"); sys.exit(0)

IMPORT_ANCHOR = "import sys, os, re, json, time, subprocess, urllib.request, urllib.parse, urllib.error"
if IMPORT_ANCHOR not in s:
    print("FAIL: import anchor not found"); sys.exit(2)
s = s.replace(IMPORT_ANCHOR, IMPORT_ANCHOR + "\nfrom scribe import scribe_process", 1)

SEND = "                send(chat_id, reply)"
if s.count(SEND) != 1:
    print(f"FAIL: expected exactly 1 send(chat_id, reply), found {s.count(SEND)}"); sys.exit(3)
HOOK = (
    "                # --- SCRIBE HOOK (external materializer; never crash the forward path) ---\n"
    "                try:\n"
    "                    reply, _scribe_notes = scribe_process(reply)\n"
    "                    if _scribe_notes:\n"
    "                        reply += \"\\n\\n--- scribe ---\\n\" + _scribe_notes\n"
    "                except Exception as _e:\n"
    "                    log(f\"scribe error: {_e}\")\n"
    "                send(chat_id, reply)"
)
s = s.replace(SEND, HOOK, 1)

ast.parse(s)  # must still be valid Python
io.open(P, "w", encoding="utf-8").write(s)
print("PATCH-OK: scribe import + hook installed; file parses.")
