"""Schelling Segregation: mild preference produces high global segregation.

Agents prefer neighbors of same type with threshold >= 30%.
Simulation shows high global segregation emerges from mild individual preference.
Segregation measured before/after as ratio of same-type neighbors.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random

def schelling_segregation() -> None:
    random.seed(42)

    # Grid size and initial population
    grid_size = 10
    grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]

    # Populate with two types (0 and 1), roughly equal
    total_cells = grid_size * grid_size
    n_type0 = total_cells // 2
    n_type1 = total_cells - n_type0

    cells = [0] * n_type0 + [1] * n_type1
    random.shuffle(cells)

    idx = 0
    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j] = cells[idx]
            idx += 1

    # Preference threshold: agents want >= 30% same type neighbors
    preference_threshold = 0.3

    def get_neighbors(r: int, c: int) -> list[int]:
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < grid_size and 0 <= nc < grid_size:
                    neighbors.append(grid[nr][nc])
        return neighbors

    def is_satisfied(r: int, c: int) -> bool:
        neighbors = get_neighbors(r, c)
        if len(neighbors) == 0:
            return True
        same_type = sum(1 for n in neighbors if n == grid[r][c])
        return same_type / len(neighbors) >= preference_threshold

    # Measure initial segregation
    def measure_segregation() -> float:
        total_same = 0
        total_neighbors = 0
        for i in range(grid_size):
            for j in range(grid_size):
                neighbors = get_neighbors(i, j)
                if neighbors:
                    same = sum(1 for n in neighbors if n == grid[i][j])
                    total_same += same
                    total_neighbors += len(neighbors)
        return total_same / total_neighbors if total_neighbors > 0 else 0

    initial_seg = measure_segregation()

    # Simulation: move unsatisfied agents
    for iteration in range(100):
        unsatisfied = []
        for i in range(grid_size):
            for j in range(grid_size):
                if not is_satisfied(i, j):
                    unsatisfied.append((i, j))

        if not unsatisfied:
            break

        # Move one random unsatisfied agent
        ri, ci = random.choice(unsatisfied)
        agent_type = grid[ri][ci]

        # Find empty cell or random cell with different type
        for attempt in range(20):
            ni, nj = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
            if grid[ni][nj] != agent_type:
                grid[ri][ci], grid[ni][nj] = grid[ni][nj], grid[ri][ci]
                break

    final_seg = measure_segregation()

    # Final segregation should be high (> 0.5)
    assert final_seg > 0.5, (
        f"Final segregation {final_seg:.3f} should be high (> 0.5) "
        f"from mild preference {preference_threshold}"
    )

    # Final segregation should be >= initial (at least as segregated)
    assert final_seg >= initial_seg, (
        f"Final segregation {final_seg:.3f} should be >= initial {initial_seg:.3f}"
    )

    print("PASS")

if __name__ == "__main__":
    schelling_segregation()
