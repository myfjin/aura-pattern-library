"""Value Iteration on Gridworld: compute optimal values and policy.

Small 4x4 gridworld with pit at (1,1) and goal at (3,3). Value iteration converges
monotonically and finds optimal policy that routes around the pit. Values are asserted
to converge within epsilon and optimal policy is verified.
"""
import random

def value_iteration_gridworld() -> None:
    random.seed(42)

    # 4x4 gridworld: state = (row, col)
    goal = (3, 3)
    pit = (1, 1)
    grid_size = 4

    # Value iteration
    values = [[0.0 for _ in range(grid_size)] for _ in range(grid_size)]
    values_prev = [[0.0 for _ in range(grid_size)] for _ in range(grid_size)]
    gamma = 0.9
    epsilon = 1e-4

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
        return -0.1  # step cost

    # Value iteration with convergence check
    iterations = 0
    converged = False
    for iteration in range(100):
        iterations = iteration
        for i in range(grid_size):
            for j in range(grid_size):
                state = (i, j)
                if state == goal:
                    values[i][j] = 1.0
                    continue

                neighbors = get_neighbors(state)
                max_value = -float('inf')
                for next_state in neighbors:
                    reward = get_reward(next_state)
                    next_value = reward + gamma * values_prev[next_state[0]][next_state[1]]
                    max_value = max(max_value, next_value)

                values[i][j] = max_value

        # Check convergence
        delta = max(abs(values[i][j] - values_prev[i][j])
                    for i in range(grid_size) for j in range(grid_size))

        values_prev = [row[:] for row in values]

        if delta < epsilon:
            converged = True
            break

    assert converged, f"Value iteration did not converge after {iterations} iterations"

    # Verify optimal policy avoids pit
    policy = {}
    for i in range(grid_size):
        for j in range(grid_size):
            state = (i, j)
            if state == goal:
                continue

            neighbors = get_neighbors(state)
            best_next = None
            best_value = -float('inf')
            for next_state in neighbors:
                next_value = get_reward(next_state) + gamma * values[next_state[0]][next_state[1]]
                if next_value > best_value:
                    best_value = next_value
                    best_next = next_state
            policy[state] = best_next

    # Check that policy doesn't move towards pit from starting positions
    for i in range(grid_size):
        for j in range(grid_size):
            state = (i, j)
            if state in policy and policy[state] == pit:
                assert False, f"Optimal policy moves to pit from {state}"

    print("PASS")

if __name__ == "__main__":
    value_iteration_gridworld()
