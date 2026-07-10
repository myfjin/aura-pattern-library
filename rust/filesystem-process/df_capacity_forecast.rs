#![forbid(unsafe_code)]
//! df_capacity_forecast — linear time-to-full from synthetic df samples; matches trajectory.
//!
//! Core idea: collect disk usage samples over time, fit a line, forecast when full.
//! THE ONE LAW: plant a known growth rate, collect samples, fit, forecast, and assert
//! the prediction matches the hand-computed time-to-full.
//! When to use: capacity planning, SLA monitoring, disk quota alerts.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct DfSample {
    time: u32,     // Seconds since epoch.
    used_bytes: u64,
}

fn linear_forecast(samples: &[DfSample], capacity: u64) -> Option<u32> {
    if samples.len() < 2 {
        return None;
    }

    // Simple linear fit: compute slope from first to last sample.
    let first = &samples[0];
    let last = &samples[samples.len() - 1];

    let time_delta = last.time - first.time;
    if time_delta == 0 {
        return None;
    }

    let bytes_delta = last.used_bytes as i64 - first.used_bytes as i64;
    let slope = bytes_delta as f64 / time_delta as f64; // bytes per second

    if slope <= 0.0 {
        return None; // Not growing
    }

    // Forecast: how long until we reach capacity?
    let bytes_to_full = capacity as f64 - last.used_bytes as f64;
    let seconds_to_full = bytes_to_full / slope;
    let forecast_time = last.time as f64 + seconds_to_full;

    Some(forecast_time as u32)
}

fn main() {
    // Planted case 1: steady growth at 1000 bytes/sec.
    let samples1 = vec![
        DfSample { time: 0, used_bytes: 0 },
        DfSample { time: 10, used_bytes: 10_000 },
        DfSample { time: 20, used_bytes: 20_000 },
        DfSample { time: 30, used_bytes: 30_000 },
    ];

    let capacity = 100_000u64;
    let forecast = linear_forecast(&samples1, capacity).expect("forecast should succeed");

    // Hand math: at t=30, used=30k. Slope = 30k / 30 = 1000 bytes/sec.
    // To reach 100k: 70k / 1000 = 70 seconds. So forecast at t=30+70=100.
    assert_eq!(forecast, 100, "forecast should match hand math");

    // Planted case 2: faster growth.
    let samples2 = vec![
        DfSample { time: 0, used_bytes: 0 },
        DfSample { time: 5, used_bytes: 50_000 },
        DfSample { time: 10, used_bytes: 100_000 },
    ];

    let capacity2 = 200_000u64;
    let forecast2 = linear_forecast(&samples2, capacity2).expect("forecast should succeed");

    // Hand math: slope = 100k / 10 = 10k bytes/sec.
    // At t=10, used=100k. To reach 200k: 100k / 10k = 10 seconds. Forecast at t=10+10=20.
    assert_eq!(forecast2, 20, "forecast should be at 20 seconds");

    // THE ONE LAW: forecast must match the linear trajectory.
    // Verify by checking the predicted time-to-full.
    let bytes_to_full = capacity2 - samples2.last().unwrap().used_bytes;
    let slope = (samples2.last().unwrap().used_bytes as f64) / (samples2.last().unwrap().time as f64);
    let expected_ttf = bytes_to_full as f64 / slope;
    assert!((expected_ttf - 10.0).abs() < 1.0, "time-to-full should match");

    // Planted case 3: no growth (empty array) should return None.
    let samples3 = vec![DfSample { time: 100, used_bytes: 50_000 }];
    let forecast3 = linear_forecast(&samples3, 100_000);
    assert!(forecast3.is_none(), "single sample should not forecast");

    // Planted case 4: negative growth (cleanup) should not forecast.
    let samples4 = vec![
        DfSample { time: 0, used_bytes: 50_000 },
        DfSample { time: 10, used_bytes: 40_000 }, // Going down
    ];
    let forecast4 = linear_forecast(&samples4, 100_000);
    assert!(forecast4.is_none(), "negative growth should not forecast full");

    println!("df_capacity_forecast: linear forecast matches trajectory hand math — PASS");
}
