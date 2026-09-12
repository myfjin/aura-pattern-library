#!/usr/bin/env python3
"""
roundtrip_probes.py — ASSISTED round-trip positive oracles. Each entry supplies the per-pattern
setup a generic builder can't guess (construct/train/typed-input), and the harness verifies the
positive oracle:  inverse(forward(x)) == x  (exact or within a stated tolerance) over several
inputs. NOTHING is mutated — these run against unmodified library files. A survivor earns a
SEMANTIC positive oracle = a real PASS candidate for the exam (Illia's gate to freeze).

Triple gate per pattern: identity holds on all inputs · pattern self-test still green ·
deterministic across two subprocess runs.
"""
import os, importlib.util, io, contextlib, subprocess, sys, glob, json, math

LIB = os.path.expanduser("~/aura-pattern-library")
HERE = os.path.dirname(os.path.abspath(__file__))

def _load(rel):
    s = importlib.util.spec_from_file_location("rtp_" + str(abs(hash(rel))), os.path.join(LIB, rel))
    m = importlib.util.module_from_spec(s)
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        s.loader.exec_module(m)
    return m

def _rel(name):
    hits = glob.glob(os.path.join(LIB, "**", name), recursive=True)
    return os.path.relpath(hits[0], LIB) if hits else None


# --- per-pattern assisted oracles: return (held, total, pair-label) ---
# each closes over the module; identity check is the positive oracle.

def rt_geohash(m):
    held = total = 0
    for lat, lon in [(37.7749, -122.4194), (0.0, 0.0), (51.5074, -0.1278),
                     (-33.8688, 151.2093), (89.9, 179.9), (-89.9, -179.9)]:
        total += 1
        g = m.encode(lat, lon, 9)
        dlat, dlon, elat, elon = m.decode(g)
        if abs(dlat - lat) <= elat and abs(dlon - lon) <= elon:
            held += 1
    return held, total, "encode<->decode (within error bounds)"

def rt_bpe(m):
    t = m.BPETokenizer(vocab_size=120)
    t.learn_merges("the cat sat on the mat the dog ran in the park the cat and dog played "
                   "a bird flew over the lazy fox near the river bank", num_merges=40)
    held = total = 0
    for txt in ["the cat", "the dog ran", "on the mat", "the park", "a bird flew", "the lazy fox"]:
        total += 1
        if t.decode(t.encode(txt)) == txt:
            held += 1
    return held, total, "encode<->decode (trained, in-vocab)"

def rt_message_encoder(m):
    enc = m.Encoder(); dec = m.Decoder()
    held = total = 0
    for data in [b"hello", b"", b"\x00\x01\xff", b"A" * 50, b"payload 123", b"\x7f\x80\x81"]:
        total += 1
        try:
            fmt, back = dec.decode(enc.encode(data))
            if back == data:
                held += 1
        except Exception:
            pass
    return held, total, "Encoder.encode<->Decoder.decode"


def rt_model_persistence(m):
    """to_dict/from_dict must preserve predictions exactly (serialization identity)."""
    X = [[1.0, 2.0, 3.0], [-1.0, 0.5, 2.0], [3.0, -2.0, 1.0], [0.0, 0.0, 0.0]]
    y = [10 + 2*x[0] - 1.5*x[1] + 0.5*x[2] for x in X]
    model = m.fit_linear_model(X, y)
    restored = m.SimpleLinearModel.from_dict(model.to_dict())
    held = total = 0
    for row in X + [[5.0, 5.0, 5.0], [-3.0, 1.0, -1.0]]:
        total += 1
        if abs(model.predict([row])[0] - restored.predict([row])[0]) < 1e-12:
            held += 1
    return held, total, "to_dict<->from_dict (prediction identity)"


class RoundtripDefect(Exception):
    """The round-trip oracle found a real defect (harness panicked / crashed mid-identity)."""

# --- rust round-trip harness: rename main->pattern_main, append probe main that round-trips ---
def _rust_rt(rel, probe_main, label):
    src = open(os.path.join(LIB, rel), encoding="utf-8").read()
    src = src.replace("fn main()", "fn pattern_main()") + "\n" + probe_main
    import tempfile
    d = tempfile.mkdtemp(prefix="aura_rt_")
    p = os.path.join(d, "probe.rs"); open(p, "w").write(src)
    exe = os.path.join(d, "probe")
    c = subprocess.run(["rustc", "-O", "--edition", "2021", "-A", "warnings", "-o", exe, p],
                       capture_output=True, text=True, timeout=180)
    if c.returncode != 0:
        raise RuntimeError("rustc: " + c.stderr[-200:])
    r = subprocess.run([exe], capture_output=True, text=True, timeout=60)
    held, total = 0, 0
    for line in r.stdout.splitlines():
        if line.startswith("RT "):
            _, h, t = line.split(); held, total = int(h), int(t)
    if r.returncode != 0:   # the round-trip harness CRASHED mid-identity = real defect
        panic = next((l for l in r.stderr.splitlines() if "panicked" in l), r.stderr.strip()[:120])
        raise RoundtripDefect(f"{label}: harness crashed rc={r.returncode} — {panic}")
    return held, total, label

def rt_backslash(_m=None):
    return _rust_rt(_rel("backslash_escape_codec.rs"), '''
fn main() {
    let cases: Vec<Vec<u8>> = vec![vec![1,2,3], vec![], vec![0,255,10,13,92,34],
        b"hello world".to_vec(), (0u8..=255).collect(), vec![92,92,110]];
    let (mut h, mut t) = (0,0);
    for x in &cases { t+=1;
        let e = EscapeCodec::encode(x);
        if let Ok(back) = EscapeCodec::decode(&e) { if &back==x { h+=1; } } }
    println!("RT {} {}", h, t);
}''', "encode<->decode (all bytes)")

def rt_cobs(_m=None):
    return _rust_rt(_rel("cobs_framing.rs"), '''
fn main() {
    let cases: Vec<Vec<u8>> = vec![vec![1,2,3], vec![0], vec![0,0,0],
        b"frame".to_vec(), (1u8..=254).collect(), vec![0,1,0,1]];
    let (mut h, mut t) = (0,0);
    for x in &cases { t+=1;
        let e = Cobs::encode(x);
        if let Ok(back) = Cobs::decode(&e) { if &back==x { h+=1; } } }
    println!("RT {} {}", h, t);
}''', "encode<->decode (COBS framing)")


def rt_slip(_m=None):
    return _rust_rt(_rel("slip_escape_framer.rs"), '''
fn main() {
    let cases: Vec<Vec<u8>> = vec![vec![1,2,3], vec![], vec![0xC0,0xDB,0xDC,0xDD],
        b"frame data".to_vec(), (0u8..=255).collect(), vec![0xC0,0xC0]];
    let (mut h, mut t) = (0,0);
    for x in &cases { t+=1;
        let e = SlipCodec::encode(x);
        if let Ok(back) = SlipCodec::decode(&e) { if &back==x { h+=1; } } }
    println!("RT {} {}", h, t);
}''', "SLIP encode<->decode (all bytes)")

def rt_rle(_m=None):
    return _rust_rt(_rel("compressed_block_store.rs"), '''
fn main() {
    let cases: Vec<Vec<u8>> = vec![vec![1,1,1,2,3], vec![], vec![5,5,5,5,5,5],
        b"aaabbbccc".to_vec(), (0u8..=255).collect(), vec![9]];
    let (mut h, mut t) = (0,0);
    for x in &cases { t+=1;
        let back = rle_decode(&rle_encode(x));
        if &back==x { h+=1; } }
    println!("RT {} {}", h, t);
}''', "RLE encode<->decode")

def rt_cidr(_m=None):
    return _rust_rt(_rel("cidr_ip_math.rs"), '''
fn main() {
    let cases: Vec<u32> = vec![0, 1, 0xFFFFFFFF, 0xC0A80001, 0x7F000001, 0x08080808];
    let (mut h, mut t) = (0,0);
    for &x in &cases { t+=1;
        if IPv4::from_u32(x).to_u32()==x { h+=1; } }
    println!("RT {} {}", h, t);
}''', "IPv4 to_u32<->from_u32")

def rt_crc_packet(_m=None):
    return _rust_rt(_rel("crc_framed_packet.rs"), '''
fn main() {
    let cases: Vec<(Vec<u8>,Vec<u8>)> = vec![
        (vec![1,2], vec![3,4,5]), (vec![], vec![]), (b"hdr".to_vec(), b"payload".to_vec()),
        (vec![0], vec![255,255]), (vec![9;4], vec![7;20]), (vec![1], vec![])];
    let (mut h, mut t) = (0,0);
    for (hd,pl) in &cases { t+=1;
        let b = Packet::new(hd.clone(), pl.clone()).serialize();
        if let Ok(p2) = Packet::deserialize(&b) { if p2.serialize()==b { h+=1; } } }
    println!("RT {} {}", h, t);
}''', "Packet serialize-stability")

def rt_backup_state(_m=None):
    return _rust_rt(_rel("backup_snapshot_restore.rs"), '''
fn main() {
    let mut cases: Vec<HashMap<String,usize>> = Vec::new();
    cases.push(HashMap::new());
    let mut a=HashMap::new(); a.insert("x".to_string(),1); a.insert("y".to_string(),2); cases.push(a);
    let mut b=HashMap::new(); for i in 0..20 { b.insert(format!("k{}",i), i*7); } cases.push(b);
    let (mut h, mut t) = (0,0);
    for d in &cases { t+=1;
        let s = State{ data: d.clone() };
        // DATA equality, not byte-stability: State is HashMap-backed so serialize order
        // is non-deterministic; the round-trip contract is data preservation.
        if let Some(s2) = State::deserialize(&s.serialize()) { if &s2.data==d { h+=1; } } }
    println!("RT {} {}", h, t);
}''', "State serialize<->deserialize (data identity)")


def _rust_bytes_codec(name, enc, dec):
    """encode(&[u8])->String/Vec, decode(...)->Option<Vec<u8>>: decode(encode(x))==Some(x)."""
    def probe(_m=None):
        return _rust_rt(_rel(name), f'''
fn main() {{
    let cases: Vec<Vec<u8>> = vec![vec![1,2,3], vec![], vec![0,255,128],
        b"hello world".to_vec(), (0u8..=255).collect(), vec![42]];
    let (mut h, mut t) = (0,0);
    for x in &cases {{ t+=1;
        let e = {enc}(x);
        if let Some(back) = {dec}(&e) {{ if &back==x {{ h+=1; }} }} }}
    println!("RT {{}} {{}}", h, t);
}}''', f"{enc}<->{dec}")
    return probe

def rt_varint(_m=None):
    return _rust_rt(_rel("varint_leb128.rs"), '''
fn main() {
    let cases: Vec<u64> = vec![0, 1, 127, 128, 300, u64::MAX, 16384, 0xDEADBEEF];
    let (mut h, mut t) = (0,0);
    for &n in &cases { t+=1;
        if let Some((d,_)) = varint_decode(&varint_encode(n)) { if d==n { h+=1; } } }
    println!("RT {} {}", h, t);
}''', "varint_encode<->varint_decode")

def rt_zigzag(_m=None):
    return _rust_rt(_rel("zigzag_signed.rs"), '''
fn main() {
    let cases: Vec<i64> = vec![0, 1, -1, 63, -64, i64::MAX, i64::MIN, -12345, 12345];
    let (mut h, mut t) = (0,0);
    for &n in &cases { t+=1;
        if zigzag_decode(zigzag_encode(n))==n { h+=1; } }
    println!("RT {} {}", h, t);
}''', "zigzag_encode<->zigzag_decode")


def rt_delta_zigzag(_m=None):
    return _rust_rt(_rel("delta_zigzag_encode.rs"), '''
fn main() {
    let cases: Vec<Vec<i64>> = vec![vec![1,2,3], vec![], vec![100,-100,100],
        vec![0,0,0,0], vec![i64::MIN,0,i64::MAX], (0..50i64).collect()];
    let (mut h, mut t) = (0,0);
    for x in &cases { t+=1;
        if let Some(back) = delta_zigzag_decode(&delta_zigzag_encode(x)) { if &back==x { h+=1; } } }
    println!("RT {} {}", h, t);
}''', "delta_zigzag encode<->decode (i64 seq)")

def rt_length_prefixed(_m=None):
    return _rust_rt(_rel("length_prefixed_framing.rs"), '''
fn main() {
    let batches: Vec<Vec<Vec<u8>>> = vec![
        vec![b"one".to_vec(), b"two".to_vec()], vec![], vec![vec![]],
        vec![b"".to_vec(), b"x".to_vec(), b"".to_vec()],
        vec![(0u8..=255).collect()], vec![vec![1;100], vec![2;3]]];
    let (mut h, mut t) = (0,0);
    for msgs in &batches { t+=1;
        let mut buf = Vec::new();
        for m in msgs { buf.extend(encode_frame(m)); }
        if let Ok(back) = decode_frames(&buf) { if &back==msgs { h+=1; } } }
    println!("RT {} {}", h, t);
}''', "length_prefixed encode_frame<->decode_frames (multi-frame)")


# ── WAVE 1 (2026-07-23): extend the round-trip lane to the remaining invertible rust set.
# Only genuinely invertible patterns are wired — parse-only scanners and checksums are
# deliberately one-way and are NOT round-trip candidates (no fake oracle coverage).

def rt_gray(_m=None):
    return _rust_rt(_rel("gray_code.rs"), '''
fn main() {
    let mut cases: Vec<u32> = vec![0,1,2,3,7,8,255,256,65535,65536,4294967295];
    for i in 0..200u32 { cases.push(i.wrapping_mul(2654435761)); }
    let (mut h, mut t) = (0,0);
    for &n in &cases { t+=1; if gray_to_binary(binary_to_gray(n)) == n { h+=1; } }
    println!("RT {} {}", h, t);
}''', "binary_to_gray<->gray_to_binary")


def rt_roman(_m=None):
    return _rust_rt(_rel("roman_numeral.rs"), '''
fn main() {
    let (mut h, mut t) = (0,0);
    for n in 1u16..=3999 { t+=1;
        if let Some(s) = int_to_roman(n) {
            if roman_to_int(&s) == Some(n) { h+=1; } } }
    println!("RT {} {}", h, t);
}''', "int_to_roman<->roman_to_int (1..=3999)")


def rt_reverse_bits(_m=None):
    return _rust_rt(_rel("reverse_bits.rs"), '''
fn main() {
    let (mut h, mut t) = (0,0);
    for n in 0u16..=255 { let b = n as u8; t+=1; if reverse_bits_8(reverse_bits_8(b))==b { h+=1; } }
    for n in [0u16,1,2,255,256,4095,65535] { t+=1; if reverse_bits_16(reverse_bits_16(n))==n { h+=1; } }
    for n in [0u32,1,255,65536,4294967295] { t+=1; if reverse_bits_32(reverse_bits_32(n))==n { h+=1; } }
    for n in [0u64,1,255,4294967296,18446744073709551615] { t+=1; if reverse_bits_64(reverse_bits_64(n))==n { h+=1; } }
    println!("RT {} {}", h, t);
}''', "reverse_bits_N self-inverse (involution)")


def rt_bit_reader_writer(_m=None):
    return _rust_rt(_rel("bit_reader_writer.rs"), '''
fn main() {
    let seqs: Vec<Vec<(u64,usize)>> = vec![
        vec![(1,1),(0,1),(5,3),(255,8)],
        vec![(0,1),(1,1),(2,2),(3,2),(15,4)],
        vec![(1023,10),(7,3),(1,1)],
        vec![(0,8),(255,8),(170,8)],
        vec![(65535,16),(4095,12)],
    ];
    let (mut h, mut t) = (0,0);
    for seq in &seqs { t+=1;
        let mut w = BitWriter::new();
        for &(v,n) in seq { w.write_bits(v,n); }
        let bytes = w.finish();
        let mut r = BitReader::new(bytes);
        let mut ok = true;
        for &(v,n) in seq { if r.read_bits(n) != Some(v) { ok=false; break; } }
        if ok { h+=1; } }
    println!("RT {} {}", h, t);
}''', "BitWriter::write_bits<->BitReader::read_bits")


def rt_ini(_m=None):
    return _rust_rt(_rel("ini_config_parser.rs"), '''
fn main() {
    let cases = vec![
        "[a]\\nk=1\\n",
        "[srv]\\nhost=localhost\\nport=8080\\n[db]\\nname=test\\n",
        "[x]\\nempty=\\n",
        "[s1]\\na=1\\nb=2\\n[s2]\\nc=3\\n",
        "[only]\\nsingle=value\\n",
    ];
    let (mut h, mut t) = (0,0);
    for c in &cases { t+=1;
        let mut p1 = IniConfig::new(); p1.parse(c);
        let s1 = p1.serialize();
        let mut p2 = IniConfig::new(); p2.parse(&s1);
        let s2 = p2.serialize();
        if s1 == s2 { h+=1; } }
    println!("RT {} {}", h, t);
}''', "parse<->serialize (canonical fixed point)")


def rt_byte_unit(_m=None):
    # format_bytes is human-readable and lossy by design -> the honest identity is the
    # CANONICAL FIXED POINT: format(parse(format(x))) == format(x).
    return _rust_rt(_rel("byte_unit_parse.rs"), '''
fn main() {
    let cases: Vec<u64> = vec![0,1,512,1023,1024,1536,1048576,1073741824,5368709120,999,10240];
    let (mut h, mut t) = (0,0);
    for &n in &cases { t+=1;
        let s1 = format_bytes(n);
        if let Some(v) = parse_bytes(&s1) { if format_bytes(v) == s1 { h+=1; } } }
    println!("RT {} {}", h, t);
}''', "format_bytes<->parse_bytes (canonical fixed point)")


def rt_duration(_m=None):
    return _rust_rt(_rel("duration_parse.rs"), '''
fn main() {
    let cases: Vec<u64> = vec![0,1,999,1000,1500,60000,3600000,86400000,90000,5000];
    let (mut h, mut t) = (0,0);
    for &n in &cases { t+=1;
        let s1 = format_duration_ms(n);
        if let Some(v) = parse_duration_ms(&s1) { if format_duration_ms(v) == s1 { h+=1; } } }
    println!("RT {} {}", h, t);
}''', "format_duration_ms<->parse_duration_ms (canonical fixed point)")


REGISTRY = {
    "gray_code.rs": rt_gray,
    "roman_numeral.rs": rt_roman,
    "reverse_bits.rs": rt_reverse_bits,
    "bit_reader_writer.rs": rt_bit_reader_writer,
    "ini_config_parser.rs": rt_ini,
    "byte_unit_parse.rs": rt_byte_unit,
    "duration_parse.rs": rt_duration,
    "geohash_encode_decode.py": rt_geohash,
    "bpe_tokenizer_lite.py": rt_bpe,
    "message_encoder.py": rt_message_encoder,
    "model_persistence_roundtrip.py": rt_model_persistence,
    "backslash_escape_codec.rs": rt_backslash,
    "cobs_framing.rs": rt_cobs,
    "slip_escape_framer.rs": rt_slip,
    "compressed_block_store.rs": rt_rle,
    "cidr_ip_math.rs": rt_cidr,
    "crc_framed_packet.rs": rt_crc_packet,
    "backup_snapshot_restore.rs": rt_backup_state,
    "base32_codec.rs": _rust_bytes_codec("base32_codec.rs", "base32_encode", "base32_decode"),
    "base64_codec.rs": _rust_bytes_codec("base64_codec.rs", "base64_encode", "base64_decode"),
    "hex_codec.rs": _rust_bytes_codec("hex_codec.rs", "hex_encode", "hex_decode"),
    "base58_codec.rs": _rust_bytes_codec("base58_codec.rs", "base58_encode", "base58_decode"),
    "jwt_hs256_verify.rs": _rust_bytes_codec("jwt_hs256_verify.rs", "base64url_encode", "base64url_decode"),
    "run_length_encode.rs": _rust_bytes_codec("run_length_encode.rs", "rle_encode", "rle_decode"),
    "varint_leb128.rs": rt_varint,
    "zigzag_signed.rs": rt_zigzag,
    "delta_zigzag_encode.rs": rt_delta_zigzag,
    "length_prefixed_framing.rs": rt_length_prefixed,
}


def verify(name, fn):
    rel = _rel(name)
    if not rel:
        return {"status": "SKIP", "detail": "file not found"}
    try:
        m = None if rel.endswith(".rs") else _load(rel)   # rust probes self-harness, no py import
        held, total, label = fn(m)
    except RoundtripDefect as d:
        return {"status": "FLAG", "rel": rel, "reason": f"roundtrip_defect: {d}", "detail": str(d)}
    except Exception as e:
        return {"status": "ERROR", "detail": f"{type(e).__name__}: {e}"}
    if held < total or total < 3:
        return {"status": "FLAG", "rel": rel, "reason": f"roundtrip_incomplete {held}/{total} {label}",
                "detail": f"round-trip {held}/{total} {label}"}
    # language-aware self-test: python via subprocess; rust via compile+run its own main
    if rel.endswith(".rs"):
        import tempfile
        d = tempfile.mkdtemp(prefix="aura_st_")
        exe = os.path.join(d, "st")
        c = subprocess.run(["rustc", "-O", "--edition", "2021", "-A", "warnings",
                            "-o", exe, os.path.join(LIB, rel)], capture_output=True, text=True, timeout=180)
        if c.returncode != 0:
            return {"status": "REVIEW", "rel": rel, "detail": f"oracle {held}/{total} but self-test compile RED"}
        r1 = subprocess.run([exe], capture_output=True, text=True, timeout=60)
        r2 = subprocess.run([exe], capture_output=True, text=True, timeout=60)
    else:
        r1 = subprocess.run([sys.executable, os.path.join(LIB, rel)], capture_output=True, text=True, timeout=90)
        r2 = subprocess.run([sys.executable, os.path.join(LIB, rel)], capture_output=True, text=True, timeout=90)
    selftest = r1.returncode == 0
    det = r1.stdout == r2.stdout
    status = "PASS" if (selftest and det) else "REVIEW"
    return {"status": status, "rel": rel, "held": held, "total": total,
            "detail": f"oracle {held}/{total} [{label}] · selftest={'GREEN' if selftest else 'RED'} · det={det}"}


def main():
    print(f"ASSISTED ROUND-TRIP ORACLES — {len(REGISTRY)} wired")
    print("=" * 88)
    passes = []
    for name, fn in REGISTRY.items():
        r = verify(name, fn)
        if r["status"] == "PASS":
            passes.append(r["rel"])
        print(f"  [{r['status']:6}] {name:34} {r['detail']}")
    print("=" * 88)
    print(f"POSITIVE ORACLES EARNED (PASS): {len(passes)}/{len(REGISTRY)}  "
          f"— real semantic oracles, exam-PASS candidates (Illia's gate to freeze)")
    json.dump({"passes": passes}, open(os.path.join(HERE, "roundtrip_probes_report.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
