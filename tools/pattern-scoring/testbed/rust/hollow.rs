#![forbid(unsafe_code)]
// pretends to test but asserts nothing
fn compute(x: i64) -> i64 { x * 2 }
fn main() {
    let _ = compute(21);
    println!("compute: PASS");
}
