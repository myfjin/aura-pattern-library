#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn main() {
    // Two-phase commit as a real coordinator + participant FSM, not a boolean reduction.
    // THE ONE LAW: a participant that voted YES is PREPARED and BLOCKED — it may not commit on
    // its own. It commits only if the coordinator's global decision is COMMIT (which requires
    // EVERY participant to have voted YES); if any voted NO, the global decision is ABORT and
    // even the YES-voters must abort. The decision is atomic: all participants end in the same
    // outcome state.

    #[derive(Clone, Copy, Debug, PartialEq, Eq)]
    enum Vote {
        Yes,
        No,
    }

    #[derive(Clone, Copy, Debug, PartialEq, Eq)]
    enum Decision {
        Commit,
        Abort,
    }

    #[derive(Clone, Copy, Debug, PartialEq, Eq)]
    enum PState {
        Working,   // initial
        Prepared,  // voted YES, durably prepared, awaiting decision (BLOCKED)
        Committed, // applied the global COMMIT
        Aborted,   // voted NO, or applied the global ABORT
    }

    struct Participant {
        vote: Vote,
        state: PState,
    }

    impl Participant {
        fn new(vote: Vote) -> Self {
            Participant { vote, state: PState::Working }
        }
        // Phase 1: on PREPARE, a YES-voter durably prepares (and is now blocked); a NO-voter aborts.
        fn prepare(&mut self) -> Vote {
            self.state = match self.vote {
                Vote::Yes => PState::Prepared,
                Vote::No => PState::Aborted,
            };
            self.vote
        }
        // Phase 2: apply the coordinator's global decision. A prepared participant obeys it.
        fn apply(&mut self, d: Decision) {
            self.state = match d {
                Decision::Commit => PState::Committed,
                Decision::Abort => PState::Aborted,
            };
        }
    }

    // Coordinator runs both phases and returns the global decision.
    fn run_2pc(participants: &mut [Participant]) -> Decision {
        // Phase 1: collect votes. Global COMMIT requires unanimity.
        let mut all_yes = true;
        for p in participants.iter_mut() {
            if p.prepare() == Vote::No {
                all_yes = false;
            }
        }
        let decision = if all_yes { Decision::Commit } else { Decision::Abort };
        // Phase 2: broadcast the decision; every participant applies the SAME outcome.
        for p in participants.iter_mut() {
            p.apply(decision);
        }
        decision
    }

    // Scenario 1: unanimous YES → COMMIT, and every participant ends Committed.
    let mut ps = vec![Participant::new(Vote::Yes), Participant::new(Vote::Yes), Participant::new(Vote::Yes)];
    assert_eq!(run_2pc(&mut ps), Decision::Commit);
    assert!(ps.iter().all(|p| p.state == PState::Committed), "all commit on unanimous yes");

    // Scenario 2: one NO → ABORT, and even the YES-voters end Aborted (they cannot commit alone).
    let mut ps = vec![Participant::new(Vote::Yes), Participant::new(Vote::No), Participant::new(Vote::Yes)];
    assert_eq!(run_2pc(&mut ps), Decision::Abort);
    assert!(ps.iter().all(|p| p.state == PState::Aborted), "all abort when any votes no");
    // The yes-voter specifically did NOT unilaterally commit:
    assert_eq!(ps[0].vote, Vote::Yes);
    assert_eq!(ps[0].state, PState::Aborted, "a yes-voter must abort under a global abort");

    // Scenario 3: the blocking property — after PREPARE but BEFORE the decision, a yes-voter is
    // Prepared (durable + blocked), not yet Committed.
    let mut solo = Participant::new(Vote::Yes);
    assert_eq!(solo.prepare(), Vote::Yes);
    assert_eq!(solo.state, PState::Prepared, "prepared participant is blocked awaiting the decision");
    solo.apply(Decision::Commit);
    assert_eq!(solo.state, PState::Committed);

    // Scenario 4: a NO-voter is Aborted the moment it votes, independent of others.
    let mut no = Participant::new(Vote::No);
    assert_eq!(no.prepare(), Vote::No);
    assert_eq!(no.state, PState::Aborted, "a no-voter aborts immediately in phase 1");

    println!("two_phase_commit_coordinator: PASS");
}
