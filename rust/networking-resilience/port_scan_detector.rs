#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashMap;

struct PortScanDetector {
    threshold: usize,
    window_seconds: u64,
    sources: HashMap<u32, Vec<(u16, u64)>>, // IP -> [(port, timestamp)]
}

impl PortScanDetector {
    fn new(threshold: usize, window_seconds: u64) -> Self {
        Self {
            threshold,
            window_seconds,
            sources: HashMap::new(),
        }
    }

    fn detect(&mut self, src_ip: u32, dst_port: u16, now: u64) -> bool {
        let entry = self.sources.entry(src_ip).or_insert_with(Vec::new);

        // Remove old events outside window (keep events within window_seconds)
        entry.retain(|(_, ts)| now - ts < self.window_seconds);

        // Add new event
        entry.push((dst_port, now));

        // Count distinct ports
        let distinct_ports: std::collections::HashSet<u16> =
            entry.iter().map(|(p, _)| *p).collect();

        distinct_ports.len() >= self.threshold
    }
}

fn main() {
    // Test 1: Below threshold
    let mut detector = PortScanDetector::new(5, 60);
    let src = 0x7F000001u32; // 127.0.0.1

    assert!(!detector.detect(src, 80, 0), "1 port, threshold 5");
    assert!(!detector.detect(src, 443, 0), "2 ports, threshold 5");
    assert!(!detector.detect(src, 8080, 0), "3 ports, threshold 5");

    // Test 2: Reach threshold
    assert!(!detector.detect(src, 22, 0), "4 ports, threshold 5");
    assert!(detector.detect(src, 3306, 0), "5 ports, threshold 5 → FLAGGED");

    // Test 3: Repeat port doesn't increase count
    assert!(detector.detect(src, 80, 0), "5 distinct ports (80 repeated) → FLAGGED");

    // Test 4: Window expiration
    let mut detector2 = PortScanDetector::new(3, 10);
    assert!(!detector2.detect(0xC0A80001, 80, 0), "1 port at t=0");
    assert!(!detector2.detect(0xC0A80001, 443, 0), "2 ports at t=0");
    assert!(detector2.detect(0xC0A80001, 22, 0), "3 ports at t=0 → FLAGGED");

    // Advance time past window
    assert!(!detector2.detect(0xC0A80001, 8080, 15), "t=15, old events expire, 1 new port → NOT FLAGGED");

    // Test 5: Multiple sources independent
    let mut detector3 = PortScanDetector::new(2, 60);
    assert!(!detector3.detect(10, 80, 0), "Source 10, port 80");
    assert!(detector3.detect(10, 443, 0), "Source 10, port 443 → FLAGGED");
    assert!(!detector3.detect(20, 80, 0), "Source 20, port 80 (different source, count 1)");
    assert!(detector3.detect(20, 443, 0), "Source 20, port 443 → FLAGGED");
    assert!(detector3.detect(10, 22, 0), "Source 10, port 22 (3 distinct) → FLAGGED");

    // Test 6: Exact planted sequence
    let mut detector4 = PortScanDetector::new(4, 100);
    let src = 192u32;
    let mut flagged_count = 0;

    let events = vec![
        (80, 0, false),   // 1 port
        (443, 0, false),  // 2 ports
        (22, 0, false),   // 3 ports
        (3306, 0, true),  // 4 ports → FLAGGED
        (8080, 0, true),  // 5 ports → FLAGGED
        (21, 0, true),    // 6 ports → FLAGGED
    ];

    for (port, time, expect_flag) in events {
        let flag = detector4.detect(src, port, time);
        assert_eq!(flag, expect_flag, "Port {} should flag={}", port, expect_flag);
        if flag {
            flagged_count += 1;
        }
    }
    assert_eq!(flagged_count, 3, "3 events should trigger flag");

    println!("port_scan_detector: PASS");
}
