#![forbid(unsafe_code)]
// tries to use unsafe despite the forbid → must fail to compile
fn deref_raw() -> i64 {
    let x = 42i64;
    let p = &x as *const i64;
    unsafe { *p }
}
fn main() { assert_eq!(deref_raw(), 42); println!("PASS"); }
