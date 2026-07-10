#![forbid(unsafe_code)]
//! url_parse — scheme/host/port/path/query split; planted URLs decomposed.
//!
//! Core idea: parse a URL into components without regex or external parsing. THE ONE LAW:
//! plant a set of well-formed and edge-case URLs, parse them, and assert each component
//! matches the expected value — a naive split on / or : would fail on ports or queries.
//! When to use: proxy rules, request routing, URL canonicalization.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct URL<'a> {
    scheme: &'a str,
    host: &'a str,
    port: Option<u16>,
    path: &'a str,
    query: Option<&'a str>,
}

fn parse_url(url: &str) -> Option<URL<'_>> {
    // Scheme: until ://
    let scheme_end = url.find("://")?;
    let scheme = &url[..scheme_end];
    let rest = &url[scheme_end + 3..];

    // Host and port: until / or end
    let path_start = rest.find('/').unwrap_or(rest.len());
    let host_port = &rest[..path_start];
    let path_and_query = &rest[path_start..];

    // Port: after last :
    let (host, port) = if let Some(colon_pos) = host_port.rfind(':') {
        let h = &host_port[..colon_pos];
        let p: u16 = host_port[colon_pos + 1..].parse().ok()?;
        (h, Some(p))
    } else {
        (host_port, None)
    };

    // Query: after ?
    let (path, query) = if let Some(q_pos) = path_and_query.find('?') {
        (&path_and_query[..q_pos], Some(&path_and_query[q_pos + 1..]))
    } else {
        (path_and_query, None)
    };

    Some(URL {
        scheme,
        host,
        port,
        path: if path.is_empty() { "/" } else { path },
        query,
    })
}

fn main() {
    // Planted URLs with known components.
    let cases = vec![
        (
            "https://example.com/path",
            ("https", "example.com", None, "/path", None),
        ),
        (
            "http://example.com:8080/",
            ("http", "example.com", Some(8080), "/", None),
        ),
        (
            "https://example.com:443/path?key=value",
            ("https", "example.com", Some(443), "/path", Some("key=value")),
        ),
        (
            "ftp://files.example.org:21/pub",
            ("ftp", "files.example.org", Some(21), "/pub", None),
        ),
    ];

    // THE ONE LAW: every component matches exactly.
    for (url_str, (exp_scheme, exp_host, exp_port, exp_path, exp_query)) in &cases {
        let parsed = parse_url(url_str).expect(&format!("failed to parse {url_str}"));
        assert_eq!(parsed.scheme, *exp_scheme, "scheme mismatch in {url_str}");
        assert_eq!(parsed.host, *exp_host, "host mismatch in {url_str}");
        assert_eq!(parsed.port, *exp_port, "port mismatch in {url_str}");
        assert_eq!(parsed.path, *exp_path, "path mismatch in {url_str}");
        assert_eq!(parsed.query, *exp_query, "query mismatch in {url_str}");
    }

    // Malformed URLs should fail.
    assert!(parse_url("not-a-url").is_none());
    assert!(parse_url("https://no-path-no-scheme.com:invalid-port/").is_none());

    println!("url_parse: {} URLs decomposed correctly — PASS", cases.len());
}
