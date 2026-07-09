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
    """Demonstrate the timer functionality."""
    print("Starting timer demo...")
    
    # Basic timer usage
    timer = Timer("test")
    timer.start()
    time.sleep(0.01)  # 10ms
    timer.stop()
    print(f"Basic timer result: {timer.elapsed():.6f} seconds")
    
    # Timer stack usage
    with TimerStack() as stack:
        stack.start("main")
        
        # Simulate some work
        stack.start("setup")
        time.sleep(0.005)  # 5ms
        stack.stop()
        
        # Nested timers
        stack.start("processing")
        stack.start("phase1")
        time.sleep(0.01)  # 10ms
        stack.stop()
        
        stack.start("phase2")
        time.sleep(0.015)  # 15ms
        stack.stop()
        stack.stop()  # processing
        
        stack.start("teardown")
        time.sleep(0.002)  # 2ms
        stack.stop()
        
        stack.stop()  # main
    
    # Generate and print report
    report = stack.report()
    print("\n" + str(report))
    
    # Demonstrate multiple calls to same timer
    with TimerStack() as stack:
        for i in range(3):
            stack.start("loop_task")
            time.sleep(0.001 * (i + 1))  # 1ms, 2ms, 3ms
            stack.stop()
        
        stack.start("final_task")
        time.sleep(0.005)  # 5ms
        stack.stop()
        
        report = stack.report()
        print("\n" + str(report))


if __name__ == "__main__":
    demo()