# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
from typing import Dict, List, Optional, Tuple
from collections import defaultdict


class Timer:
    """A simple timer that can be started and stopped to measure elapsed time."""
    
    def __init__(self, name: str) -> None:
        self.name = name
        self._start_time: Optional[float] = None
        self._elapsed: float = 0.0
        self._running: bool = False
    
    def start(self) -> None:
        """Start the timer."""
        if self._running:
            raise RuntimeError(f"Timer '{self.name}' is already running")
        self._start_time = time.perf_counter()
        self._running = True
    
    def stop(self) -> None:
        """Stop the timer and accumulate elapsed time."""
        if not self._running:
            raise RuntimeError(f"Timer '{self.name}' is not running")
        if self._start_time is None:
            raise RuntimeError(f"Timer '{self.name}' has no start time")
        self._elapsed += time.perf_counter() - self._start_time
        self._start_time = None
        self._running = False
    
    def elapsed(self) -> float:
        """Return the total elapsed time in seconds."""
        if self._running and self._start_time is not None:
            return self._elapsed + (time.perf_counter() - self._start_time)
        return self._elapsed
    
    def reset(self) -> None:
        """Reset the timer to zero."""
        self._elapsed = 0.0
        self._start_time = None
        self._running = False
    
    @property
    def running(self) -> bool:
        """Return whether the timer is currently running."""
        return self._running


class TimerStack:
    """A stack-based hierarchical timer manager."""
    
    def __init__(self) -> None:
        self._timers: Dict[str, Timer] = {}
        self._stack: List[str] = []
        self._call_counts: Dict[str, int] = defaultdict(int)
    
    def start(self, name: str) -> None:
        """Start a timer with the given name."""
        if name not in self._timers:
            self._timers[name] = Timer(name)
        self._timers[name].start()
        self._stack.append(name)
        self._call_counts[name] += 1
    
    def stop(self) -> str:
        """Stop the most recently started timer."""
        if not self._stack:
            raise RuntimeError("No active timers to stop")
        name = self._stack.pop()
        self._timers[name].stop()
        return name
    
    def __enter__(self) -> 'TimerStack':
        """Enter context manager."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit context manager, stopping all remaining timers."""
        while self._stack:
            self.stop()
    
    def get_timer(self, name: str) -> Optional[Timer]:
        """Get a timer by name."""
        return self._timers.get(name)
    
    def get_elapsed(self, name: str) -> float:
        """Get elapsed time for a timer by name."""
        timer = self._timers.get(name)
        return timer.elapsed() if timer else 0.0
    
    def get_call_count(self, name: str) -> int:
        """Get the number of times a timer was started."""
        return self._call_counts.get(name, 0)
    
    def get_all_timers(self) -> Dict[str, Timer]:
        """Get all timers."""
        return self._timers.copy()
    
    def report(self) -> 'Report':
        """Generate a report of all timer data."""
        return Report(
            timers=self._timers.copy(),
            call_counts=dict(self._call_counts),
            stack_depth=len(self._stack)
        )


class Report:
    """A report containing timer statistics."""
    
    def __init__(self, timers: Dict[str, Timer], call_counts: Dict[str, int], stack_depth: int) -> None:
        self.timers = timers
        self.call_counts = call_counts
        self.stack_depth = stack_depth
        self.timestamp = time.time()
    
    def format_report(self) -> str:
        """Format the report as a string."""
        if not self.timers:
            return "No timers recorded."
        
        lines = ["Timer Report:"]
        lines.append("-" * 50)
        lines.append(f"{'Name':<20} {'Time (s)':<12} {'Calls':<8} {'Avg Time (s)':<12}")
        lines.append("-" * 50)
        
        # Sort timers by elapsed time (descending)
        sorted_timers = sorted(self.timers.items(), key=lambda x: x[1].elapsed(), reverse=True)
        
        for name, timer in sorted_timers:
            elapsed = timer.elapsed()
            calls = self.call_counts.get(name, 0)
            avg_time = elapsed / calls if calls > 0 else 0
            lines.append(f"{name:<20} {elapsed:<12.6f} {calls:<8} {avg_time:<12.6f}")
        
        lines.append("-" * 50)
        lines.append(f"Active timers: {self.stack_depth}")
        lines.append(f"Report generated: {time.ctime(self.timestamp)}")
        
        return "\n".join(lines)
    
    def __str__(self) -> str:
        return self.format_report()


def demo() -> None:
    """Self-test on a FAKE clock: exact elapsed arithmetic, accumulation
    across restarts, LIFO stack discipline, misuse refused."""
    _now = [1000.0]
    _real = time.perf_counter
    time.perf_counter = lambda: _now[0]
    try:
        # Exact elapsed: start, advance 2.5s, stop.
        t = Timer("t")
        t.start()
        _now[0] += 2.5
        t.stop()
        assert t.elapsed() == 2.5, f"2.5s on the fake clock must read 2.5, got {t.elapsed()}"

        # Accumulation across restarts: +1.5 more = 4.0 total.
        t.start()
        _now[0] += 1.5
        t.stop()
        assert t.elapsed() == 4.0, f"accumulated elapsed must be 4.0, got {t.elapsed()}"

        # A running timer reads live time without stopping.
        t.start()
        _now[0] += 0.5
        assert t.elapsed() == 4.5 and t.running
        t.stop()
        t.reset()
        assert t.elapsed() == 0.0 and not t.running, "reset left state behind"

        # Misuse is refused: double start, stop without start.
        t.start()
        try:
            t.start()
            assert False, "double start accepted"
        except RuntimeError:
            pass
        t.stop()
        try:
            t.stop()
            assert False, "stop on stopped timer accepted"
        except RuntimeError:
            pass

        # Stack discipline: stop() always pops the INNERMOST timer (LIFO),
        # and nested times nest arithmetically.
        stack = TimerStack()
        stack.start("outer")
        _now[0] += 1.0
        stack.start("inner")
        _now[0] += 2.0
        assert stack.stop() == "inner", "stop must pop the innermost timer"
        _now[0] += 1.0
        assert stack.stop() == "outer"
        assert stack.get_elapsed("inner") == 2.0, f"inner: {stack.get_elapsed('inner')}"
        assert stack.get_elapsed("outer") == 4.0, f"outer must span 1+2+1=4: {stack.get_elapsed('outer')}"
        assert stack.get_elapsed("ghost") == 0.0

        # Call counts and re-entry: 3 starts of the same name accumulate.
        with TimerStack() as s2:
            for dt in (1.0, 2.0, 3.0):
                s2.start("loop")
                _now[0] += dt
                s2.stop()
        assert s2.get_call_count("loop") == 3
        assert s2.get_elapsed("loop") == 6.0, f"1+2+3 must be 6, got {s2.get_elapsed('loop')}"

        # Context-manager exit force-stops whatever is still running.
        with TimerStack() as s3:
            s3.start("abandoned")
            _now[0] += 7.0
        assert s3.get_elapsed("abandoned") == 7.0, "unstopped timer not closed by __exit__"
        assert not s3.get_timer("abandoned").running

        # Stopping an empty stack is refused.
        try:
            TimerStack().stop()
            assert False, "stop on empty stack accepted"
        except RuntimeError:
            pass

        # Report contains the exact numbers.
        rep = s2.report()
        assert "loop" in rep.format_report() and rep.call_counts["loop"] == 3
    finally:
        time.perf_counter = _real

    print("timer_stack: fake-clock elapsed exact (2.5→4.0→4.5), LIFO pops, "
          "loop 3 calls == 6.0s, __exit__ closed 7.0s — PASS")


if __name__ == "__main__":
    demo()