#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#[derive(Debug, Clone, Copy, PartialEq)]
enum RetryClass {
    Ok,
    Retry,
    RetryAfter,
    Fatal,
}

fn classify_http_status(status: u16) -> RetryClass {
    match status {
        // 2xx: OK
        200..=299 => RetryClass::Ok,
        // 3xx: OK (not retried)
        300..=399 => RetryClass::Ok,
        // 408: Request Timeout
        408 => RetryClass::Retry,
        // 429: Too Many Requests
        429 => RetryClass::RetryAfter,
        // 500: Internal Server Error
        500 => RetryClass::Retry,
        // 502, 503, 504: Bad Gateway, Service Unavailable, Gateway Timeout
        502 | 503 | 504 => RetryClass::RetryAfter,
        // 4xx: Fatal (except 408, 429)
        400..=499 => RetryClass::Fatal,
        // 5xx: Retry (except 502, 503, 504)
        500..=599 => RetryClass::Retry,
        // Other
        _ => RetryClass::Retry,
    }
}

fn main() {
    // Test 1: Success statuses
    assert_eq!(classify_http_status(200), RetryClass::Ok, "200 OK");
    assert_eq!(classify_http_status(201), RetryClass::Ok, "201 Created");
    assert_eq!(classify_http_status(204), RetryClass::Ok, "204 No Content");

    // Test 2: Redirect (treated as OK, not retried)
    assert_eq!(classify_http_status(301), RetryClass::Ok, "301 Moved Permanently");
    assert_eq!(classify_http_status(302), RetryClass::Ok, "302 Found");

    // Test 3: Retriable client errors
    assert_eq!(classify_http_status(408), RetryClass::Retry, "408 Request Timeout");

    // Test 4: Retry-After needed
    assert_eq!(classify_http_status(429), RetryClass::RetryAfter, "429 Too Many Requests");
    assert_eq!(classify_http_status(503), RetryClass::RetryAfter, "503 Service Unavailable");

    // Test 5: Fatal client errors
    assert_eq!(classify_http_status(400), RetryClass::Fatal, "400 Bad Request");
    assert_eq!(classify_http_status(401), RetryClass::Fatal, "401 Unauthorized");
    assert_eq!(classify_http_status(403), RetryClass::Fatal, "403 Forbidden");
    assert_eq!(classify_http_status(404), RetryClass::Fatal, "404 Not Found");

    // Test 6: Server errors
    assert_eq!(classify_http_status(500), RetryClass::Retry, "500 Internal Server Error");
    assert_eq!(classify_http_status(502), RetryClass::RetryAfter, "502 Bad Gateway");
    assert_eq!(classify_http_status(504), RetryClass::RetryAfter, "504 Gateway Timeout");

    // Test 7: Exact planted table
    let table = vec![
        (200, RetryClass::Ok),
        (429, RetryClass::RetryAfter),
        (503, RetryClass::RetryAfter),
        (500, RetryClass::Retry),
        (404, RetryClass::Fatal),
        (408, RetryClass::Retry),
    ];
    for (status, expected_class) in table {
        assert_eq!(classify_http_status(status), expected_class, "Status {} should be {:?}", status, expected_class);
    }

    println!("http_status_retry_classifier: PASS");
}
