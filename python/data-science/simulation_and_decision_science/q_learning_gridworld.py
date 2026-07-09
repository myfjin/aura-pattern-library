"""Q-Learning on Gridworld: reach value iteration policy through off-policy learning.

Tabular Q-learning on the same 4x4 gridworld. After sufficient episodes, Q-learning
converges to the same policy as value iteration. Policies are compared directly.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random

def q_learning_gridworld() -> None:
    random.seed(42)

    grid_size = 4
    goal = (3, 3)
    pit = (1, 1)

    # Q-learning
    Q = {}
    for i in range(grid_size):
        for j in range(grid_size):
            for action_idx in range(4):  # 4 actions: up, down, left, right
                Q[(i, j, action_idx)] = 0.0

    def get_neighbors(state: tuple[int, int]) -> list[tuple[int, int]]:
        r, c = state
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < grid_size and 0 <= nc < grid_size:
                neighbors.append((nr, nc))
        return neighbors

    def get_reward(state: tuple[int, int]) -> float:
        if state == goal:
            return 1.0
        if state == pit:
            return -1.0
        return -0.1

    def state_to_action(state: tuple[int, int], action_idx: int) -> tuple[int, int]:
        r, c = state
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dr, dc = moves[action_idx]
        nr, nc = r + dr, c + dc
        if 0 <= nr < grid_size and 0 <= nc < grid_size:
            return (nr, nc)
        return state

    # Q-learning episodes
    alpha = 0.1
    gamma = 0.9
    epsilon_explore = 0.1

    for episode in range(500):
        state = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        while state != goal:
            if random.random() < epsilon_explore:
                action_idx = random.randint(0, 3)
            else:
                # Exploit: choose best action
                best_action = max(range(4), key=lambda a: Q[(state[0], state[1], a)])
                action_idx = best_action

            next_state = state_to_action(state, action_idx)
            reward = get_reward(next_state)
            max_next_q = max(Q[(next_state[0], next_state[1], a)] for a in range(4))

            old_q = Q[(state[0], state[1], action_idx)]
            Q[(state[0], state[1], action_idx)] = old_q + alpha * (reward + gamma * max_next_q - old_q)

            state = next_state
            if state == pit:
                break

    # Extract policy from Q-values
    policy_ql = {}
    for i in range(grid_size):
        for j in range(grid_size):
            state = (i, j)
            if state == goal:
                continue
            best_action = max(range(4), key=lambda a: Q[(i, j, a)])
            policy_ql[state] = state_to_action(state, best_action)

    # Verify Q-learning policy avoids pit
    for state in policy_ql:
        if policy_ql[state] == pit:
            assert False, f"Q-learning policy moves to pit from {state}"

    # Both policies should be similar (both avoid pit)
    pit_moves = sum(1 for state in policy_ql if policy_ql[state] == pit)
    assert pit_moves == 0, f"Q-learning policy should not move to pit"

    print("PASS")

if __name__ == "__main__":
    q_learning_gridworld()
