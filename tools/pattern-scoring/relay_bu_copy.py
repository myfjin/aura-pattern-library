#!/usr/bin/env python3
"""
AURA telegram relay — bridges a Telegram bot to a headless Claude Code agent.

Why this exists: on .8 the agents run on Ollama, and native Claude Code
telegram "channels" require the Anthropic backend, so they are unavailable.
This relay needs no channels: it polls the bot with the plain Telegram Bot API
and feeds each message to `<launcher> -p --continue`, then sends the reply back.
Keeps the agent as Claude Code on Ollama (its plugins + MCPs intact).

Usage:
  relay.py <name> <env_file> <launcher> <allowed_csv>
    name        label (e.g. fifth_state) -> state dir ~/.claude/relay/<name>
    env_file    path to a file containing TELEGRAM_BOT_TOKEN=...
    launcher    command that runs the agent headless (accepts -p "prompt")
    allowed_csv comma-separated Telegram user ids allowed to talk to it
"""
import sys, os, re, json, time, subprocess, urllib.request, urllib.parse, urllib.error

BOT_USERNAME = ""  # set from getMe at startup

NAME, ENV_FILE, LAUNCHER, ALLOWED_CSV = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
ALLOWED = {x.strip() for x in ALLOWED_CSV.split(",") if x.strip()}

STATE_DIR = os.path.expanduser(f"~/.claude/relay/{NAME}")
os.makedirs(STATE_DIR, exist_ok=True)
OFFSET_FILE = os.path.join(STATE_DIR, "offset")
STARTED_FLAG = os.path.join(STATE_DIR, "started")
LOG_FILE = os.path.join(STATE_DIR, "relay.log")

CLAUDE_TIMEOUT = 600   # seconds per agent turn (bumped for DeepSeek's slower responses)
POLL_TIMEOUT = 55      # telegram long-poll seconds


def read_token():
    for line in open(ENV_FILE):
        line = line.strip()
        if line.startswith("TELEGRAM_BOT_TOKEN="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit(f"no TELEGRAM_BOT_TOKEN in {ENV_FILE}")


TOKEN = read_token()
API = f"https://api.telegram.org/bot{TOKEN}"


def log(msg):
    line = f"{time.strftime('%Y-%m-%dT%H:%M:%S')} [{NAME}] {msg}"
    print(line, flush=True)
    try:
        with open(LOG_FILE, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass


def tg(method, params, timeout=65):
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(f"{API}/{method}", data=data)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def send(chat_id, text):
    if not text:
        text = "(empty reply)"
    for i in range(0, len(text), 3800):
        try:
            tg("sendMessage", {"chat_id": chat_id, "text": text[i:i + 3800]}, timeout=30)
        except Exception as e:
            log(f"send error: {e}")


def get_offset():
    try:
        return int(open(OFFSET_FILE).read().strip())
    except Exception:
        return 0


def set_offset(o):
    tmp = OFFSET_FILE + ".tmp"
    with open(tmp, "w") as f:
        f.write(str(o))
    os.replace(tmp, OFFSET_FILE)


def run_agent(prompt):
    base = [LAUNCHER, "-p"]
    use_continue = os.path.exists(STARTED_FLAG)
    args = base + (["--continue"] if use_continue else []) + [prompt]
    try:
        p = subprocess.run(args, capture_output=True, text=True, timeout=CLAUDE_TIMEOUT)
        out = (p.stdout or "").strip()
        if (p.returncode != 0 or not out) and use_continue:
            log(f"--continue rc={p.returncode}/empty, retrying fresh")
            p = subprocess.run(base + [prompt], capture_output=True, text=True, timeout=CLAUDE_TIMEOUT)
            out = (p.stdout or "").strip()
        if p.returncode == 0:
            with open(STARTED_FLAG, "w") as f:
                f.write("1")
        if not out:
            out = f"(agent gave no output; rc={p.returncode})\n{(p.stderr or '')[:800]}"
        return out
    except subprocess.TimeoutExpired:
        return f"(agent timed out after {CLAUDE_TIMEOUT}s)"
    except Exception as e:
        return f"(error running agent: {e})"


def main():
    global BOT_USERNAME
    log(f"relay start; launcher={LAUNCHER}; allowed={sorted(ALLOWED)}")
    try:
        me = tg("getMe", {}, timeout=15)
        BOT_USERNAME = me.get("result", {}).get("username", "") or ""
        log(f"getMe ok: @{BOT_USERNAME}")
    except Exception as e:
        log(f"getMe failed: {e}")
    while True:
        try:
            resp = tg("getUpdates", {"offset": get_offset(), "timeout": POLL_TIMEOUT},
                      timeout=POLL_TIMEOUT + 10)
            if not resp.get("ok"):
                log(f"getUpdates not ok: {resp}")
                time.sleep(5)
                continue
            for upd in resp.get("result", []):
                set_offset(upd["update_id"] + 1)  # at-most-once: never loop a poison msg
                msg = upd.get("message") or upd.get("edited_message")
                if not msg:
                    continue
                chat = msg.get("chat", {})
                chat_id = chat.get("id")
                chat_type = chat.get("type", "private")
                frm = str(msg.get("from", {}).get("id", ""))
                text = msg.get("text", "") or ""
                if not text.strip():
                    continue  # ignore service / non-text messages silently (joins, stickers, etc.)
                if frm not in ALLOWED:
                    continue
                # In group chats, only respond when this bot is @mentioned or directly replied-to,
                # so multiple bots in one room don't all answer every message.
                if chat_type in ("group", "supergroup"):
                    reply_user = msg.get("reply_to_message", {}).get("from", {}).get("username", "") or ""
                    mentioned = BOT_USERNAME and f"@{BOT_USERNAME}".lower() in text.lower()
                    replied = BOT_USERNAME and reply_user.lower() == BOT_USERNAME.lower()
                    if mentioned:
                        text = re.sub(f"@{re.escape(BOT_USERNAME)}", "", text, flags=re.IGNORECASE).strip()
                    elif not replied:
                        continue  # not addressed to this bot
                    if not text.strip():
                        text = "(hello)"
                cmd = text.strip().split()[0].lower()
                if cmd in ("/start", "/help"):
                    send(chat_id, f"{NAME} online (Claude Code on Ollama via relay). "
                                  f"Send any message and I'll respond. /new = fresh conversation.")
                    continue
                if cmd == "/new":
                    try:
                        os.remove(STARTED_FLAG)
                    except OSError:
                        pass
                    send(chat_id, "Started a fresh conversation.")
                    continue
                log(f"msg from {frm} in {chat_type} chat_id={chat_id}: {text[:100]!r}")
                reply = run_agent(text)
                log(f"reply {len(reply)} chars: {reply[:100]!r}")
                send(chat_id, reply)
        except urllib.error.HTTPError as e:
            body = ""
            try:
                body = e.read().decode()[:200]
            except Exception:
                pass
            log(f"HTTPError {e.code}: {body}")
            time.sleep(5)
        except urllib.error.URLError as e:
            log(f"URLError: {e}")
            time.sleep(5)
        except Exception as e:
            log(f"loop error: {e}")
            time.sleep(5)


if __name__ == "__main__":
    main()
