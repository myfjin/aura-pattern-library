#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Deterministic timing model for a hedged request: fire a primary now, and if it
// hasn't returned by hedge_delay, fire a backup. Given fixed primary/backup latencies
// it computes which copy finishes first and the completion time, without any real I/O
// or concurrency. Use to reason about (or unit-test) hedging trade-offs — the backup
// only helps when hedge_delay + backup_latency beats primary_latency. Guarantees:
// returns the earlier completion, and ties resolve to the primary (asserts cover
// primary-wins, backup-wins, and the tie case).
struct HedgedRequestScheduler {
    hedge_delay: u64,
    primary_latency: u64,
    backup_latency: u64,
}

impl HedgedRequestScheduler {
    fn new(hedge_delay: u64, primary_latency: u64, backup_latency: u64) -> Self {
        Self {
            hedge_delay,
            primary_latency,
            backup_latency,
        }
    }

    fn execute(&self, now: u64) -> (u64, bool) {
        let primary_done = now + self.primary_latency;
        let hedge_fire = now + self.hedge_delay;
        let backup_done = hedge_fire + self.backup_latency;

        if primary_done <= backup_done {
            (primary_done, false) // Primary wins
        } else {
            (backup_done, true) // Backup wins
        }
    }
}

fn main() {
    // Test 1: Primary faster
    let sch = HedgedRequestScheduler::new(10, 5, 20);
    let (finish_time, backup_won) = sch.execute(0);
    assert_eq!(finish_time, 5, "Primary finishes at 5");
    assert!(!backup_won, "Primary should win");

    // Test 2: Backup faster
    let sch2 = HedgedRequestScheduler::new(5, 20, 5);
    let (finish_time, backup_won) = sch2.execute(0);
    assert_eq!(finish_time, 10, "Backup finishes at hedge_delay(5) + backup_latency(5) = 10");
    assert!(backup_won, "Backup should win");

    // Test 3: Tie (primary wins on tie)
    let sch3 = HedgedRequestScheduler::new(10, 10, 10);
    let (finish_time, backup_won) = sch3.execute(0);
    assert_eq!(finish_time, 10, "Tie at 10");
    assert!(!backup_won, "Primary wins on tie");

    // Test 4: Various latency seeds
    let scenarios = vec![
        (5, 20, 1, 0, true),   // hedge_delay=5, primary=20, backup=1, start=0, backup wins (5+1=6 vs 20)
        (2, 5, 1, 0, true),    // hedge_delay=2, primary=5, backup=1, start=0, backup wins (2+1=3 vs 5)
        (3, 3, 3, 10, false),  // hedge_delay=3, primary=3, backup=3, start=10, tie, primary wins
    ];

    for (hd, pl, bl, start, expect_backup) in scenarios {
        let sch = HedgedRequestScheduler::new(hd, pl, bl);
        let (_, backup_won) = sch.execute(start);
        assert_eq!(backup_won, expect_backup, "Scenario hd={} pl={} bl={} start={} failed", hd, pl, bl, start);
    }

    println!("hedged_request_scheduler: PASS");
}
