#![forbid(unsafe_code)]
// Clamp a value into [lo, hi]. Rejects nothing; total function.
fn clamp(x: i64, lo: i64, hi: i64) -> i64 { if x < lo { lo } else if x > hi { hi } else { x } }
fn main() {
    assert_eq!(clamp(5, 0, 10), 5, "inside stays");
    assert_eq!(clamp(-3, 0, 10), 0, "below clamps to lo");
    assert_eq!(clamp(99, 0, 10), 10, "above clamps to hi");
    println!("clamp: PASS");
}
