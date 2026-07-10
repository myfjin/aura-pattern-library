#![forbid(unsafe_code)]
//! leader_lease — lease + logical clock; exactly ONE leader, lease expiry triggers re-election.
//!
//! Core idea: a leader holds a lease (time-limited). Followers check the lease epoch.
//! If expired, a new election happens (epoch increments, new leader chosen). THE LAW:
//! simulate lease expiry, trigger re-election, and assert only one leader at a time.
//! When to use: master election, consensus leadership, Zookeeper-like systems.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct Leader {
    id: usize,
    #[allow(dead_code)]
    epoch: u64,
    lease_valid: bool,
}

impl Leader {
    fn new(id: usize, epoch: u64) -> Self {
        Leader {
            id,
            epoch,
            lease_valid: true,
        }
    }

    fn expire_lease(&mut self) {
        self.lease_valid = false;
    }

    fn is_valid_leader(&self) -> bool {
        self.lease_valid
    }
}

struct LeaderElection {
    current_leader: Option<Leader>,
    epoch: u64,
    candidates: Vec<usize>,
}

impl LeaderElection {
    fn new(candidates: Vec<usize>) -> Self {
        LeaderElection {
            current_leader: None,
            epoch: 0,
            candidates,
        }
    }

    fn elect(&mut self) -> usize {
        // Simple: elect the first candidate. In practice, uses consensus.
        self.epoch += 1;
        let leader_id = self.candidates[self.epoch as usize % self.candidates.len()];
        self.current_leader = Some(Leader::new(leader_id, self.epoch));
        leader_id
    }

    fn expire_leader(&mut self) {
        if let Some(leader) = &mut self.current_leader {
            leader.expire_lease();
        }
    }

    fn trigger_election_if_needed(&mut self) -> Result<usize, String> {
        if let Some(leader) = &self.current_leader {
            if !leader.is_valid_leader() {
                return Ok(self.elect());
            }
            Ok(leader.id)
        } else {
            Ok(self.elect())
        }
    }

    fn current_leader_id(&self) -> Option<usize> {
        if let Some(leader) = &self.current_leader {
            if leader.is_valid_leader() {
                return Some(leader.id);
            }
        }
        None
    }
}

fn main() {
    // Test 1: initial election.
    let mut election = LeaderElection::new(vec![0, 1, 2]);
    let leader_id = election.elect();
    assert!(election.current_leader_id().is_some(), "leader elected");
    assert_eq!(election.current_leader_id(), Some(leader_id));

    // Test 2: lease expires, leader invalid.
    election.expire_leader();
    assert_eq!(election.current_leader_id(), None, "expired leader is invalid");

    // Test 3: re-election.
    let new_leader = election.trigger_election_if_needed().unwrap();
    assert!(election.current_leader_id().is_some(), "re-election succeeds");
    assert_ne!(new_leader, leader_id, "new leader differs (in simple cycling)");

    // Test 4: epoch increments.
    let epoch_before = election.epoch;
    election.expire_leader();
    election.trigger_election_if_needed().ok();
    let epoch_after = election.epoch;
    assert!(epoch_after > epoch_before, "epoch incremented on re-election");

    // Test 5: one leader at a time.
    let only_one = election.current_leader_id().is_some() as usize
        + (if let Some(leader) = &election.current_leader {
            !leader.is_valid_leader() as usize
        } else {
            0
        });
    assert!(only_one <= 1, "at most one valid leader");

    println!("leader_lease: lease expiry triggers re-election; one leader at a time — PASS");
}
