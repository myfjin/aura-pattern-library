"""
Queue Capacity Planner — simulate your queue's future before you deploy it.

WHAT IT DOES: Discrete-event simulation of a FIFO queue with Poisson arrivals,
exponential service, and parallel workers. Validated against exact M/M/1 theory
first (trust earned), then finds the minimal worker count meeting an SLA.

WHEN TO USE: Capacity planning for worker pools, sizing before launch.

GUARANTEES: Simulator matches M/M/1 theory within 5%. Chosen pool meets the SLA.
One fewer worker violates the SLA (minimality). Mean wait is non-increasing in
worker count.

NOT: A production queue simulator. Assumes Poisson arrivals and exponential service
times. Does not model timeouts, retries, or priority queues.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"