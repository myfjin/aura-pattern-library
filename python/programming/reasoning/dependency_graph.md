# dependency graph

**Language:** Python · **Sphere:** programming · **Category:** Reasoning

## What it does

Dependency Graph Resolver - Topological Sort Implementation

This module provides a dependency graph resolver that can:
- Detect circular dependencies
- Perform topological sorting
- Group tasks into parallel execution levels

## Guarantee

When it runs, dependency graph guarantees sum((len(l) for l in levels)) == 10; len(graph) == 10 and 'task_a' in graph and ('ghost' not in graph); sorted(order) == sorted((f'task_{n}' for n in 'abcdefghij')) (proven by run).

**Checkable constraints:**

- `len(graph) == 10 and 'task_a' in graph and ('ghost' not in graph)`
- `sorted(order) == sorted((f'task_{n}' for n in 'abcdefghij'))`
- `violations == []`
- `pos['task_a'] == 0`
- `[sorted(l) for l in levels] == [['task_a'], ['task_b', 'task_c', 'task_g', 'task_h'], ['task_e', 'task_f', 'task_i'], ['task_d'], ['task_j']]`
- `sum((len(l) for l in levels)) == 10`
- `graph.get_node_data('task_c') == 'work c'`
- `g2.topological_sort() == ['x', 'y', 'z']`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
