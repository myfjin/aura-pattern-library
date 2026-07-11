#![forbid(unsafe_code)]
//! quorum_write — N replicas, majority-ack required; minority partition refuses write.
//!
//! Core idea: a write succeeds only if a majority of N replicas acknowledge. A minority
//! partition cannot succeed a write. THE LAW: split into majority and minority, attempt
//! a write on the minority, and assert it fails; majority succeeds.
//! When to use: quorum-based consensus, distributed databases, CRDT syncing.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashMap;

struct Replica {
    #[allow(dead_code)]
    id: usize,
    data: HashMap<String, String>,
}

impl Replica {
    fn new(id: usize) -> Self {
        Replica {
            id,
            data: HashMap::new(),
        }
    }

    fn write(&mut self, key: String, value: String) {
        self.data.insert(key, value);
    }

    fn get(&self, key: &str) -> Option<String> {
        self.data.get(key).cloned()
    }
}

struct QuorumWrite {
    replicas: Vec<Replica>,
    quorum_size: usize,
}

impl QuorumWrite {
    fn new(n: usize) -> Self {
        let mut replicas = Vec::new();
        for i in 0..n {
            replicas.push(Replica::new(i));
        }
        let quorum_size = n / 2 + 1; // Majority
        QuorumWrite { replicas, quorum_size }
    }

    fn write(&mut self, key: String, value: String, replica_ids: &[usize]) -> Result<(), String> {
        if replica_ids.len() < self.quorum_size {
            return Err("quorum not reached".to_string());
        }

        for &id in replica_ids {
            if id < self.replicas.len() {
                self.replicas[id].write(key.clone(), value.clone());
            }
        }
        Ok(())
    }

    fn read(&self, key: &str, replica_ids: &[usize]) -> Option<String> {
        for &id in replica_ids {
            if id < self.replicas.len() {
                if let Some(v) = self.replicas[id].get(key) {
                    return Some(v);
                }
            }
        }
        None
    }
}

fn main() {
    let mut store = QuorumWrite::new(5); // 5 replicas, quorum = 3

    // Test 1: majority write succeeds.
    let majority = vec![0, 1, 2]; // 3 replicas (majority)
    assert!(
        store.write("key1".to_string(), "value1".to_string(), &majority).is_ok(),
        "majority write succeeds"
    );

    // Test 2: minority write fails.
    let minority = vec![3, 4]; // 2 replicas (minority)
    assert!(
        store.write("key2".to_string(), "value2".to_string(), &minority).is_err(),
        "minority write fails"
    );

    // Test 3: read from majority.
    let result = store.read("key1", &majority);
    assert_eq!(result, Some("value1".to_string()));

    // Test 4: read "key2" not in majority (was rejected).
    let result2 = store.read("key2", &majority);
    assert_eq!(result2, None, "key2 not in majority");

    // Test 5: boundary: exact quorum.
    let quorum = vec![0, 1, 2]; // Exactly 3
    assert!(
        store.write("key3".to_string(), "value3".to_string(), &quorum).is_ok(),
        "exact quorum write succeeds"
    );

    println!("quorum_write: majority required; minority refused — PASS");
}
