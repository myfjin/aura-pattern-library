# log pattern matcher

**Language:** Python · **Sphere:** programming · **Category:** Monitoring

## What it does

Ordered regex log parser that extracts named groups into structured records.

Use to turn heterogeneous log lines into dicts: register named patterns (each a
regex with named groups, e.g. apache/app/login formats), then parse a line or a
batch. The first registered pattern that matches wins, and per-pattern match
counts are tracked. Guarantees (proven by self-test): each format's named fields
are extracted exactly; a line matching no pattern returns (None, None) rather
than being force-fit; match counts are exact per pattern; ordering (first-wins)
is respected; and an invalid regex is refused at registration, not at match time.

## Guarantee

When it runs, log pattern matcher guarantees int(data['status']) + int(data['size']) == 2526; name == 'apache_common'; data == {'ip': '192.168.1.1', 'timestamp': '10/Oct/2023:13:55:36 +0000', 'method': 'GET', 'path': '/index.html', 'status': '200', 'size': '2326'} (proven by run).

**Checkable constraints:**

- `name == 'apache_common'`
- `data == {'ip': '192.168.1.1', 'timestamp': '10/Oct/2023:13:55:36 +0000', 'method': 'GET', 'path': '/index.html', 'status': '200', 'size': '2326'}`
- `int(data['status']) + int(data['size']) == 2526`
- `name == 'app_log' and data['level'] == 'ERROR'`
- `data['message'] == 'Database connection failed'`
- `name == 'login_event'`
- `data == {'user': 'john', 'ip': '192.168.1.3'}`
- `results[7] == (None, None)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
