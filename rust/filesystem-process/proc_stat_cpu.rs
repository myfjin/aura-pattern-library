#![forbid(unsafe_code)]
//! proc_stat_cpu — parse two /proc/stat fixtures → CPU% delta; matches hand math.
//!
//! Core idea: parse /proc/stat lines to extract CPU ticks (user, system, etc.), compute
//! the delta between two snapshots, and calculate the percentage. THE ONE LAW: plant
//! two known /proc/stat snapshots, parse both, compute CPU% from hand math, assert
//! the parser produces the same result.
//! When to use: system monitoring, CPU usage tracking, performance analysis.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct CpuStat {
    user: u64,
    system: u64,
    idle: u64,
    iowait: u64,
}

impl CpuStat {
    fn from_line(line: &str) -> Option<Self> {
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.is_empty() || !parts[0].starts_with("cpu") {
            return None;
        }
        if parts.len() < 5 {
            return None;
        }

        let user = parts[1].parse().ok()?;
        let _nice = parts[2].parse::<u64>().ok()?;
        let system = parts[3].parse().ok()?;
        let idle = parts[4].parse().ok()?;
        let iowait = if parts.len() > 5 {
            parts[5].parse().ok()?
        } else {
            0
        };

        Some(CpuStat {
            user,
            system,
            idle,
            iowait,
        })
    }

    fn total_ticks(&self) -> u64 {
        self.user + self.system + self.idle + self.iowait
    }

    fn busy_ticks(&self) -> u64 {
        self.user + self.system
    }
}

fn cpu_percentage(start: &CpuStat, end: &CpuStat) -> f64 {
    let total_delta = end.total_ticks() - start.total_ticks();
    if total_delta == 0 {
        return 0.0;
    }
    let busy_delta = end.busy_ticks() - start.busy_ticks();
    (busy_delta as f64 / total_delta as f64) * 100.0
}

fn main() {
    // Planted case 1: typical /proc/stat snapshot.
    let stat1 = "cpu 10 0 20 100 5 0 0 0 0 0";
    let snap1 = CpuStat::from_line(stat1).expect("parse stat1");
    assert_eq!(snap1.user, 10);
    assert_eq!(snap1.system, 20);
    assert_eq!(snap1.idle, 100);
    assert_eq!(snap1.iowait, 5);
    assert_eq!(snap1.total_ticks(), 135);
    assert_eq!(snap1.busy_ticks(), 30);

    // Planted case 2: second snapshot after time passes.
    let stat2 = "cpu 50 0 70 200 5 0 0 0 0 0";
    let snap2 = CpuStat::from_line(stat2).expect("parse stat2");
    assert_eq!(snap2.user, 50);
    assert_eq!(snap2.system, 70);
    assert_eq!(snap2.total_ticks(), 325);
    assert_eq!(snap2.busy_ticks(), 120);

    // THE ONE LAW: CPU% matches hand computation.
    // Delta: total = 325 - 135 = 190, busy = 120 - 30 = 90
    // CPU% = 90 / 190 * 100 ≈ 47.37%
    let cpu_pct = cpu_percentage(&snap1, &snap2);
    let expected = (90.0 / 190.0) * 100.0;
    assert!((cpu_pct - expected).abs() < 0.01, "CPU% should match hand math");
    assert!(cpu_pct > 45.0 && cpu_pct < 50.0, "CPU% should be ~47%");

    // Planted case 3: high CPU (mostly busy).
    let stat3 = "cpu 100 0 50 10 0 0 0 0 0 0";
    let snap3 = CpuStat::from_line(stat3).expect("parse stat3");

    let stat4 = "cpu 200 0 100 20 0 0 0 0 0 0";
    let snap4 = CpuStat::from_line(stat4).expect("parse stat4");

    let high_cpu = cpu_percentage(&snap3, &snap4);
    // Delta: total = (200+100+20) - (100+50+10) = 320 - 160 = 160
    // busy = (200+100) - (100+50) = 300 - 150 = 150
    // CPU% = 150 / 160 * 100 = 93.75%
    assert!(high_cpu > 90.0 && high_cpu < 95.0, "high CPU should be ~93%");

    // Planted case 4: idle system (low CPU).
    let stat5 = "cpu 10 0 5 1000 0 0 0 0 0 0";
    let snap5 = CpuStat::from_line(stat5).expect("parse stat5");

    let stat6 = "cpu 20 0 10 2000 0 0 0 0 0 0";
    let snap6 = CpuStat::from_line(stat6).expect("parse stat6");

    let low_cpu = cpu_percentage(&snap5, &snap6);
    // Delta: total = (20+10+2000) - (10+5+1000) = 2030 - 1015 = 1015
    // busy = (20+10) - (10+5) = 30 - 15 = 15
    // CPU% = 15 / 1015 * 100 ≈ 1.48%
    assert!(low_cpu < 2.0, "idle system should have low CPU%");

    println!("proc_stat_cpu: CPU% delta parsing matches hand math — PASS");
}
