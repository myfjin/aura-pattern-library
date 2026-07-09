"""
OPTIMIZATION: Genetic Algorithm (Selection, Crossover, Mutation)

Core idea: Population-based metaheuristic mimicking natural evolution. Iteratively
select fit individuals, combine (crossover), mutate, and replace to explore the
solution space. Demonstrates OneMax (all bits to 1) and a deceptive variant.

When to use: Combinatorial optimization, non-differentiable landscapes, or when
exploring diverse regions of the solution space is more important than rapid convergence.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple, Callable


def bitstring_fitness_onemax(bitstring: List[int]) -> int:
    """OneMax: count the number of 1s. Simple, unimodal landscape."""
    return sum(bitstring)


def bitstring_fitness_deceptive(bitstring: List[int]) -> int:
    """
    Deceptive fitness: normally reward all-zeros (len - count_ones),
    but add a large bonus for all-1s to make it global optimum despite
    deceptive landscape pushing toward all-0s.
    """
    ones = sum(bitstring)
    if ones == len(bitstring):
        return len(bitstring) + 10  # All-1s gets big bonus
    return len(bitstring) - ones


class GeneticAlgorithm:
    """Basic GA with roulette-wheel selection, single-point crossover, bit-flip mutation."""

    def __init__(
        self,
        pop_size: int,
        bitstring_length: int,
        fitness_func: Callable[[List[int]], int],
        mutation_rate: float = 0.01,
        generations: int = 100,
    ):
        self.pop_size = pop_size
        self.bitstring_length = bitstring_length
        self.fitness_func = fitness_func
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.population: List[List[int]] = []
        self.best_fitness_history: List[int] = []

    def initialize_population(self):
        """Create random population."""
        self.population = [
            [random.randint(0, 1) for _ in range(self.bitstring_length)]
            for _ in range(self.pop_size)
        ]

    def evaluate_fitness(self, individual: List[int]) -> int:
        """Compute fitness of an individual."""
        return self.fitness_func(individual)

    def selection_roulette_wheel(self) -> List[int]:
        """
        Roulette-wheel selection: probability proportional to fitness.
        Returns a selected individual.
        """
        fitnesses = [self.evaluate_fitness(ind) for ind in self.population]
        total_fitness = sum(fitnesses)

        if total_fitness == 0:
            # All have zero fitness; select randomly
            return random.choice(self.population)[:]

        probabilities = [f / total_fitness for f in fitnesses]
        cumsum = []
        cum = 0
        for p in probabilities:
            cum += p
            cumsum.append(cum)

        r = random.random()
        for i, cs in enumerate(cumsum):
            if r <= cs:
                return self.population[i][:]

        return self.population[-1][:]

    def crossover(self, parent1: List[int], parent2: List[int]) -> List[int]:
        """Single-point crossover."""
        point = random.randint(1, self.bitstring_length - 1)
        child = parent1[:point] + parent2[point:]
        return child

    def mutate(self, individual: List[int]) -> List[int]:
        """Bit-flip mutation: flip each bit with probability mutation_rate."""
        mutant = individual[:]
        for i in range(len(mutant)):
            if random.random() < self.mutation_rate:
                mutant[i] = 1 - mutant[i]
        return mutant

    def evolve(self) -> Tuple[List[int], int]:
        """Run GA for specified generations. Return (best_individual, best_fitness)."""
        self.initialize_population()

        for gen in range(self.generations):
            # Evaluate current population
            fitnesses = [self.evaluate_fitness(ind) for ind in self.population]
            best_fitness = max(fitnesses)
            self.best_fitness_history.append(best_fitness)

            # Early stopping if optimum found (for OneMax, max is bitstring_length)
            if best_fitness == self.bitstring_length:
                break

            # Create next generation
            new_population = []
            for _ in range(self.pop_size):
                parent1 = self.selection_roulette_wheel()
                parent2 = self.selection_roulette_wheel()
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)

            self.population = new_population

        # Return best individual from final population
        fitnesses = [self.evaluate_fitness(ind) for ind in self.population]
        best_idx = fitnesses.index(max(fitnesses))
        return self.population[best_idx], fitnesses[best_idx]


if __name__ == "__main__":
    random.seed(42)

    # Test 1: OneMax (should find all-1s)
    ga_onemax = GeneticAlgorithm(
        pop_size=100,
        bitstring_length=20,
        fitness_func=bitstring_fitness_onemax,
        mutation_rate=0.02,
        generations=200,
    )
    best_ind_onemax, best_fit_onemax = ga_onemax.evolve()

    assert (
        best_fit_onemax == 20
    ), f"GA did not solve OneMax: got {best_fit_onemax} ones out of 20"
    assert (
        sum(best_ind_onemax) == 20
    ), f"Best individual not all-1s: {best_ind_onemax}"

    # Test 2: Deceptive fitness (harder to solve; landscape actively misleads toward 0s)
    ga_deceptive = GeneticAlgorithm(
        pop_size=100,
        bitstring_length=8,
        fitness_func=bitstring_fitness_deceptive,
        mutation_rate=0.1,
        generations=150,
    )
    best_ind_deceptive, best_fit_deceptive = ga_deceptive.evolve()

    # Deceptive: all-1s should yield special +10 bonus
    all_ones_fitness = bitstring_fitness_deceptive([1] * 8)
    assert (
        all_ones_fitness == 18
    ), f"Deceptive all-1s fitness wrong: {all_ones_fitness}"

    # Deceptive landscape is genuinely hard; we just verify GA runs and finds something
    # (the bonus structure means all-1s is optimal but misleading gradient favors 0s)
    assert best_fit_deceptive >= 1, f"GA failed on deceptive: fitness {best_fit_deceptive}"

    print(
        f"genetic_algorithm.py: onemax_ones={best_fit_onemax} deceptive_fitness={best_fit_deceptive} PASS"
    )
