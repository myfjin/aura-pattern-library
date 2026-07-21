#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Priority-ordered failover selector: nodes are held in fixed preference order and
// select() returns the id of the first one still marked healthy. mark_healthy /
// mark_unhealthy toggle a node's state, so recovery restores its original priority.
// Use to pick a primary endpoint and fall through to lower-priority backups. Guarantees:
// selection always honors declared order (never a lower-priority node while a higher
// healthy one exists), returns None only when all are down, and a recovered node
// resumes its slot — asserts pin the full failover-then-recover sequence.
struct FailoverNode {
    id: usize,
    healthy: bool,
}

struct FailoverPriorityList {
    nodes: Vec<FailoverNode>,
}

impl FailoverPriorityList {
    fn new(node_ids: Vec<usize>) -> Self {
        let nodes = node_ids
            .into_iter()
            .map(|id| FailoverNode {
                id,
                healthy: true,
            })
            .collect();
        Self { nodes }
    }

    fn select(&self) -> Option<usize> {
        self.nodes
            .iter()
            .find(|n| n.healthy)
            .map(|n| n.id)
    }

    fn mark_healthy(&mut self, node_id: usize) {
        if let Some(node) = self.nodes.iter_mut().find(|n| n.id == node_id) {
            node.healthy = true;
        }
    }

    fn mark_unhealthy(&mut self, node_id: usize) {
        if let Some(node) = self.nodes.iter_mut().find(|n| n.id == node_id) {
            node.healthy = false;
        }
    }
}

fn main() {
    // Test 1: Select healthy node in priority order
    let mut list = FailoverPriorityList::new(vec![0, 1, 2]);
    assert_eq!(list.select(), Some(0), "First node should be selected");

    // Test 2: Skip unhealthy, select next healthy
    list.mark_unhealthy(0);
    assert_eq!(list.select(), Some(1), "Second node should be selected when first is unhealthy");

    // Test 3: Skip multiple unhealthy
    list.mark_unhealthy(1);
    assert_eq!(list.select(), Some(2), "Third node should be selected");

    // Test 4: All unhealthy returns None
    list.mark_unhealthy(2);
    assert_eq!(list.select(), None, "No healthy node returns None");

    // Test 5: Recovery (mark healthy again)
    list.mark_healthy(1);
    assert_eq!(list.select(), Some(1), "First healthy in priority order");

    // Test 6: Exact failover sequence
    let mut list2 = FailoverPriorityList::new(vec![10, 20, 30, 40]);
    let mut sequence = Vec::new();

    sequence.push(list2.select());
    list2.mark_unhealthy(10);

    sequence.push(list2.select());
    list2.mark_unhealthy(20);

    sequence.push(list2.select());
    list2.mark_unhealthy(30);

    sequence.push(list2.select());
    list2.mark_unhealthy(40);

    sequence.push(list2.select());
    list2.mark_healthy(20);

    sequence.push(list2.select());

    let expected = vec![Some(10), Some(20), Some(30), Some(40), None, Some(20)];
    assert_eq!(sequence, expected, "Failover sequence must match");

    println!("failover_priority_list: PASS");
}
