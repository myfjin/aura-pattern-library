"""
readiness_vs_liveness: liveness = the process is running; readiness = it can serve requests.
They are INDEPENDENT, and the point of the distinction is operational: a router must withhold
traffic from an instance that is alive-but-unready, and drop one that is dead — while a
liveness-only view would wrongly keep routing to a degraded instance.
Failure simulated: a live instance degrades (unready), then a ready instance dies.
Recovery asserted: the readiness-aware router sends ZERO requests to the unready-but-alive
instance (traffic withheld) and none to the dead one — proven by per-instance request counts.
A liveness-only router (ignoring readiness) would keep feeding the degraded instance → the
assert on its 0-count would fail.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys


class Instance:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        self.is_ready = False
        self.handled = 0

    def check_liveness(self):
        return self.is_alive

    def check_readiness(self):
        return self.is_ready and self.is_alive


class Router:
    """Round-robins requests over instances that pass BOTH probes."""
    def __init__(self, instances):
        self.instances = instances
        self._rr = 0

    def dispatch(self, n):
        for _ in range(n):
            servable = [i for i in self.instances if i.check_readiness()]
            if not servable:
                continue                       # no ready instance → request shed, not forced
            inst = servable[self._rr % len(servable)]
            inst.handled += 1
            self._rr += 1


if __name__ == "__main__":
    a, b = Instance("A"), Instance("B")
    router = Router([a, b])

    # Phase 1: both alive AND ready → traffic is shared.
    a.is_ready = b.is_ready = True
    router.dispatch(100)
    assert a.handled > 0 and b.handled > 0, "both ready instances should receive traffic"
    p1_a, p1_b = a.handled, b.handled

    # Phase 2: A degrades — alive but UNREADY. The defended outcome: A gets NO new traffic.
    a.is_ready = False
    assert a.check_liveness() is True and a.check_readiness() is False, \
        "A must be distinguishably alive-but-unready"
    router.dispatch(100)
    assert a.handled == p1_a, f"unready-but-alive A received traffic: {a.handled - p1_a} new requests"
    assert b.handled == p1_b + 100, f"B should absorb all 100 while A is unready: got {b.handled - p1_b}"

    # Phase 3: A recovers (ready again) → it takes traffic once more.
    a.is_ready = True
    router.dispatch(100)
    assert a.handled > p1_a, "recovered instance A should receive traffic again"

    # Phase 4: B dies (not alive). Liveness drops it entirely; all traffic goes to A.
    b.is_alive = False
    assert b.check_liveness() is False and b.check_readiness() is False, "dead B fails both probes"
    handled_b_before = b.handled
    router.dispatch(50)
    assert b.handled == handled_b_before, "dead instance B must receive no traffic"

    print(f"A handled={a.handled}, B handled={b.handled} (traffic correctly withheld/dropped)")
    print("readiness_vs_liveness PASS")
    sys.exit(0)
