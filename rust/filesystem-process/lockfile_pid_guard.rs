#![forbid(unsafe_code)]
//! lockfile_pid_guard — pidfile stale-lock detection LOGIC on fixtures; stale reclaimed, live respected.
//!
//! Core idea: a pidfile guards mutual exclusion. Acquisition must RECLAIM a lock that is stale
//! (too old) or whose owner PID is dead, but RESPECT a lock that is young AND whose owner is
//! alive. THE ONE LAW: drive the guard against a planted liveness fixture (which PIDs are alive)
//! and planted ages, asserting each of the four cases resolves correctly — a guard that ignored
//! staleness OR liveness would mis-handle one. When to use: daemon guarding, mutual exclusion.
//! (Liveness is a planted set here, standing in for the real `/proc/<pid>` check, which lives in
//! an uncalled `apply()` per the SAFETY law — no real process is inspected in the gated demo.)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashSet;
use std::time::Duration;

struct PidLock {
    pid: u32,
    age: Duration, // how long the lock has been held (planted, not wall-clock)
}

/// The real check would read /proc/<pid>; NEVER called by main (SAFETY law — logic on fixtures).
#[allow(dead_code)]
fn apply_is_process_alive(_pid: u32) -> bool {
    unimplemented!("real impl reads /proc/<pid>; the gated demo uses a planted liveness set")
}

fn acquire(
    existing: Option<&PidLock>,
    stale_after: Duration,
    live_pids: &HashSet<u32>,
) -> Result<(), String> {
    match existing {
        None => Ok(()), // no lock → free
        Some(lock) => {
            if lock.age > stale_after {
                Ok(()) // stale → reclaim regardless of owner
            } else if !live_pids.contains(&lock.pid) {
                Ok(()) // young but owner is DEAD → reclaim
            } else {
                Err(format!("lock held by live pid {}", lock.pid)) // young + alive → respect
            }
        }
    }
}

fn main() {
    let stale_after = Duration::from_secs(60);
    // Planted liveness fixture: exactly these PIDs are alive.
    let live: HashSet<u32> = [42u32, 100, 5000].into_iter().collect();

    // Case 1: no existing lock → acquire.
    assert!(acquire(None, stale_after, &live).is_ok(), "free lock must be acquirable");

    // Case 2: young (10s) + owner ALIVE (42) → respected (rejected).
    let held = PidLock { pid: 42, age: Duration::from_secs(10) };
    let r = acquire(Some(&held), stale_after, &live);
    assert!(r.is_err(), "a young, live lock must be respected");
    assert!(r.unwrap_err().contains("42"), "error should name the holding pid");

    // Case 3: young (10s) but owner DEAD (999 ∉ live) → reclaimed.
    let dead_owner = PidLock { pid: 999, age: Duration::from_secs(10) };
    assert!(acquire(Some(&dead_owner), stale_after, &live).is_ok(), "dead owner → reclaim");

    // Case 4: STALE (120s) even though owner is alive (42) → reclaimed (staleness wins).
    let stale = PidLock { pid: 42, age: Duration::from_secs(120) };
    assert!(acquire(Some(&stale), stale_after, &live).is_ok(), "stale lock → reclaim even if owner alive");

    // Boundary: exactly at the threshold (60s) is NOT yet stale → live owner respected.
    let boundary = PidLock { pid: 100, age: Duration::from_secs(60) };
    assert!(
        acquire(Some(&boundary), stale_after, &live).is_err(),
        "age == threshold is not yet stale; live owner respected"
    );

    // A guard that ignored liveness would wrongly reject case 3; one that ignored age would
    // wrongly reject case 4. Both pass here only because BOTH conditions are checked.
    println!("lockfile_pid_guard: stale reclaimed, dead-owner reclaimed, young+live respected — PASS");
}
