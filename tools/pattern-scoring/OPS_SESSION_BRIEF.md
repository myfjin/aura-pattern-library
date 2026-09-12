Fresh ops session — mesh health + RAG cleanup. Do these IN ORDER. Access: `ssh au@172.20.10.8`
(Linux, passwordless sudo), `ssh bu@172.20.10.8` (6E's user), Ver = steward gateway on .5.
GOLDEN RULE this session: VERIFY before you claim — open/run/curl the thing and show the result;
never assert "X is down/fixed" you haven't just observed. (Don't repeat the "gateway is down while
I'm speaking through it" hallucination.) The library docs are DONE (1399/1399, two-stage) — this
session is INFRA only.

=== 1. OLLAMA / SESSION-BLOAT FIRST (root cause of the agent timeouts) ===
Symptom: agents (4Q especially) hang "waiting for stream response", then APITimeoutError /
"model provider failed after retries". ROOT CAUSE (Ver confirmed): the agent's hermes session grows
huge (4Q hit ~133K tokens / 271 msgs) and ollama-CLOUD times out on that context — NOT quota, NOT
gateway-down. ALL mesh agents use ollama-cloud models (kimi-k2.7-code:cloud, deepseek-v4-flash:cloud).
CHECK & FIX:
  - Is ollama itself alive? `ssh au@172.20.10.8 "curl -s --max-time 10 http://127.0.0.1:11434/api/tags | head -c 100"` (should list models). A quick ping/generate test = alive.
  - List sessions + sizes: `ssh au@172.20.10.8 "hermes sessions list"` (or the store under ~/.hermes/). Find the bloated one (highest msgs/tokens).
  - PURGE the bloated session (Ver did this for 4Q's `20260721_091313_9fabf8`) so a fresh conversation starts clean. Also clear stray `request_dump_*` files.
  - VERIFY: gateway process alive (`ps aux | grep 'hermes.*gateway'`), ollama answers a ping, then a fresh message to the agent goes through. Gateway restart if needed: `sudo systemctl restart hermes-gateway.service` (on .8; slow graceful stop → new PID). Ver's gateway (.5): `launchctl kickstart -k ai.hermes.gateway-steward`.
  - PREVENTION: agents route to ollama.com cloud — big contexts time out. Keep sessions small / reset on bloat. Local fallback models exist on .8 if cloud is unusable: `qwen2.5:7b`, `llama3.1:8b`.

=== 2. FIX THE BOARD (hermes /board on :8090 not serving) ===
Symptom: `curl http://localhost:8090/board` returns EMPTY / nothing listening on 8090 — but the
gateway PROCESS is alive (don't misread this as "gateway down"). Ver found the steward config
(~/.hermes/config.yaml + ~/.hermes/profiles/steward*) has NO `board` block (only dashboard, privacy,
tts, onboarding, updates), so the board endpoint/plugin never loads.
FIX: add/enable the board (dashboard) service in the steward profile config so port 8090 serves
/board (and /family). Confirm the port after: `lsof -i :8090`. Then `curl -s http://localhost:8090/board`
should return real content. Restart the gateway to load the config (launchctl kickstart on .5).
VERIFY by actually curling the endpoint and showing the output — not by asserting it's fixed.

=== 3. MAKE 5S HEALTHY / CONSISTENT LIKE THE OTHERS ===
Symptom: 5S (fifth_state, au@.8 relay+tmux) gives STALE/confused status (thinks R is mid-flight,
reports old July-14 work) — its session is stale/bloated like 4Q's was. 6E and 4Q are healthy now.
FIX: same as #1 for 5S's session — purge/reset its bloated hermes/relay session so it starts clean,
then it'll report current reality. 5S relay restart if needed: on au, `tmux kill-session -t aura-relay`
then relaunch `tmux new-session -d -s aura-relay -n fifth_state 'python3 /home/au/relay.py fifth_state
/home/au/.claude/channels/telegram/.env /home/au/.local/bin/fifthstate-headless 8668187769,8851737309'`.
(6E is the same pattern on bu with sixelement / sixelement-headless.) Goal: 5S answers a "how are you"
oriented + current, like everyone else.

=== 4. CLEAR THE RAG WASTE (the "81 GB is a wrong number") — DO LAST, BACK UP FIRST ===
Diagnosis (verified): `/home/au/ai-lab/rag-daemon/chroma_db_v2/` = 81 GB real, but the actual data is
tiny — `chroma.sqlite3` = 2.3 GB (221K vectors + 1.8M metadata rows), the real HNSW index
`data_level0.bin` = 188 MB. The 81 GB is almost entirely ONE bloated/sparse HNSW file:
`chroma_db_v2/f708204c-cd62-.../link_lists.bin` = 78 GB real / 563 GB apparent (sparse, zero-holes from
hnswlib pathology under the big Telegram-history ingest). A VACUUM / index rebuild drops the whole db
to ~2.5-3 GB (reclaims ~78 GB). This is a LIVE db — care required.
STEPS (Illia's plan): 
  1. BACK UP FIRST to /mnt/ussd (check it's mounted: `df -h /mnt/ussd`). Copy at minimum the real data:
     `cp /home/au/ai-lab/rag-daemon/chroma_db_v2/chroma.sqlite3 /mnt/ussd/` (and the whole
     chroma_db_v2 dir if space allows — use `cp --sparse=always` or rsync -S so the sparse 563G file
     doesn't balloon).
  2. Stop the rag-daemon writing (find/stop its process so nothing writes mid-rebuild).
  3. Rebuild the HNSW index: recreate the chroma collection's index from the sqlite vectors (VACUUM
     the sqlite, delete + rebuild the `f708204c.../` HNSW segment) so link_lists.bin regenerates small.
  4. VERIFY: db size dropped to ~2.5-3 GB; a real RAG query still returns correct results (don't
     declare done until you've run a retrieval and it answers). Then restart the rag-daemon.
  Earlier (23:40) already reclaimed 38 GB by deleting a corrupt QUARANTINED backup + old openclaw
  tarballs — that's separate/done; this is the LIVE index rebuild.

=== CONTEXT / STATE ===
Full detail: ~/ai-lab/pattern-scoring/LINES_STATE.md · CROSS_SESSION_HANDOFF.md (library fix-and-ship).
The .8 wifi (wlp3s0/.2) was disabled to fix dual-route flakiness — verify still down / persist with
`nmcli radio wifi off` if wanted.
