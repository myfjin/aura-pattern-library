#![forbid(unsafe_code)]
//! ewma_gauge — exponentially weighted moving average with hysteresis alert.
//!
//! Core idea: EWMA smooths noisy samples; hysteresis prevents alert flapping when
//! the signal hovers near the threshold. THE ONE LAW: plant a known sequence with
//! drift, compute EWMA by hand, verify it matches, inject a drifting event sequence,
//! and assert alerts fire only when crossing the threshold with hysteresis deadband —
//! a broken EWMA or missing hysteresis would trigger spurious alerts or miss real ones.
//! When to use: anomaly detection, threshold alerts, smoothing noisy metrics.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct EwmaGauge {
    alpha: f64,
    value: f64,
    initialized: bool,
    threshold: f64,
    hysteresis: f64,
    alert_state: bool,
}

impl EwmaGauge {
    fn new(alpha: f64, threshold: f64, hysteresis: f64) -> Self {
        EwmaGauge {
            alpha,
            value: 0.0,
            initialized: false,
            threshold,
            hysteresis,
            alert_state: false,
        }
    }

    fn update(&mut self, sample: f64) -> bool {
        if !self.initialized {
            self.value = sample;
            self.initialized = true;
        } else {
            self.value = self.alpha * sample + (1.0 - self.alpha) * self.value;
        }

        // Hysteresis: alert if crossing threshold+hysteresis from below,
        // or crossing threshold-hysteresis from above.
        let newly_alert = if !self.alert_state {
            self.value >= self.threshold + self.hysteresis
        } else {
            self.value >= self.threshold - self.hysteresis
        };

        let alert_fired = newly_alert && !self.alert_state;
        self.alert_state = newly_alert;
        alert_fired
    }

    fn current(&self) -> f64 {
        self.value
    }
}

fn manual_ewma(samples: &[f64], alpha: f64) -> Vec<f64> {
    let mut result = Vec::new();
    let mut value = 0.0;
    for (i, &sample) in samples.iter().enumerate() {
        if i == 0 {
            value = sample;
        } else {
            value = alpha * sample + (1.0 - alpha) * value;
        }
        result.push(value);
    }
    result
}

fn main() {
    // Planted case 1: stable sequence, then drifting upward.
    let samples = vec![
        10.0, 10.5, 9.8, 10.2, 10.1, // stable ~10
        25.0, 30.0, 35.0, 40.0, // drift upward (strong enough to breach threshold+hyst)
    ];

    let alpha = 0.3;
    let threshold = 20.0;
    let hysteresis = 2.0;

    let mut gauge = EwmaGauge::new(alpha, threshold, hysteresis);
    let manual = manual_ewma(&samples, alpha);

    let mut alert_count = 0;
    for (i, &sample) in samples.iter().enumerate() {
        let alert = gauge.update(sample);
        if alert {
            alert_count += 1;
        }

        // THE ONE LAW: the gauge's EWMA must match the hand-computed sequence.
        assert!(
            (gauge.current() - manual[i]).abs() < 1e-9,
            "EWMA mismatch at step {}: gauge={}, manual={}",
            i,
            gauge.current(),
            manual[i]
        );
    }

    // Verify hysteresis behavior: alert should fire exactly once as we drift above threshold.
    // The drift is strong enough (15→30) that one alert is expected; more than one would
    // indicate missing hysteresis (flapping).
    assert_eq!(
        alert_count, 1,
        "exactly one alert should fire when drifting above threshold with hysteresis"
    );

    // Planted case 2: reversal — alarm stays on despite dipping below threshold+hyst.
    let mut gauge2 = EwmaGauge::new(alpha, threshold, hysteresis);
    gauge2.update(10.0); // init
    gauge2.update(35.0); // spike → should alert
    let spike_alert = gauge2.update(35.0);
    assert!(spike_alert, "spike should trigger alert");

    // Now slowly decay toward threshold; the alert should persist (no de-alert) until
    // we drop below threshold - hysteresis.
    gauge2.update(20.0); // still above threshold (20)
    let still_alert = gauge2.alert_state;
    assert!(still_alert, "alert should remain active when above threshold");

    // Decay strongly to drop below threshold-hysteresis (< 18)
    gauge2.update(10.0);
    gauge2.update(10.0);
    let de_alert = gauge2.alert_state;
    assert!(
        !de_alert,
        "alert should clear when dropping below threshold-hysteresis"
    );

    println!("ewma_gauge: EWMA exact, hysteresis suppresses flapping, drift alert fires once — PASS");
}
