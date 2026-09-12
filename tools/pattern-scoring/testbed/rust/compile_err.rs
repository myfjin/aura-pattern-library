#![forbid(unsafe_code)]
// broken on purpose
fn add(a: i64, b: i64) -> i64 { a + b   // missing brace
fn main() { assert_eq!(add(2,2), 4); println!("PASS"); }
