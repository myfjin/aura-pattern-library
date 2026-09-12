#![forbid(unsafe_code)]
// claims addition but the self-test is wrong / code is wrong
fn add(a: i64, b: i64) -> i64 { a + b }
fn main() {
    assert_eq!(add(2, 2), 5, "this WILL fail: 2+2 != 5");
    println!("add: PASS");
}
