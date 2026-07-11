# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import Any, Callable, List, Set, Optional, Generic, TypeVar
from collections import defaultdict
import weakref

T = TypeVar('T')

class Signal(Generic[T]):
    """A reactive signal that holds a value and notifies dependents of changes."""
    
    def __init__(self, initial_value: T) -> None:
        self._value: T = initial_value
        self._dependents: Set['Computed'] = set()
        self._effects: Set['Effect'] = set()
    
    @property
    def value(self) -> T:
        """Get the current value, tracking dependencies if in a reactive context."""
        # If we're in a computed or effect context, track this dependency
        current_context = _reactive_context.get()
        if current_context:
            if isinstance(current_context, Computed):
                current_context.add_dependency(self)
            elif isinstance(current_context, Effect):
                current_context.add_dependency(self)
        return self._value
    
    @value.setter
    def value(self, new_value: T) -> None:
        """Set a new value and notify dependents."""
        if self._value != new_value:
            self._value = new_value
            self._notify_dependents()
    
    def _notify_dependents(self) -> None:
        """Notify all dependents of a value change."""
        # Create copies to avoid modification during iteration
        dependents = self._dependents.copy()
        effects = self._effects.copy()
        
        # Notify computed values first
        for dependent in dependents:
            dependent._invalidate()
        
        # Then notify effects
        for effect in effects:
            effect._execute()


class Computed(Generic[T]):
    """A computed value that automatically updates when its dependencies change."""
    
    def __init__(self, computation: Callable[[], T]) -> None:
        self._computation: Callable[[], T] = computation
        self._value: Optional[T] = None
        self._dependencies: Set[Signal] = set()
        self._dependents: Set['Computed'] = set()
        self._effects: Set[Effect] = set()
        self._valid: bool = False
        self._disposed: bool = False
    
    @property
    def value(self) -> T:
        """Get the current computed value, computing it if necessary."""
        if not self._valid:
            self._compute_value()
        # Track dependencies if in a reactive context
        current_context = _reactive_context.get()
        if current_context:
            if isinstance(current_context, Computed):
                current_context.add_dependency(self)
            elif isinstance(current_context, Effect):
                current_context.add_dependency(self)
        return self._value  # type: ignore
    
    def add_dependency(self, signal: Signal) -> None:
        """Add a dependency to this computed value."""
        if self._disposed:
            return
        self._dependencies.add(signal)
        signal._dependents.add(self)
    
    def _compute_value(self) -> None:
        """Compute the value and track dependencies."""
        if self._disposed:
            return
            
        # Clear previous dependencies
        for dep in self._dependencies:
            dep._dependents.discard(self)
        self._dependencies.clear()
        
        # Compute new value with context tracking
        token = _reactive_context.set(self)
        try:
            self._value = self._computation()
            self._valid = True
        finally:
            _reactive_context.reset(token)
    
    def _invalidate(self) -> None:
        """Mark this computed value as invalid."""
        if self._valid:
            self._valid = False
            # Propagate invalidation to dependents
            for dependent in self._dependents.copy():
                dependent._invalidate()
            # Notify effects
            for effect in self._effects.copy():
                effect._execute()
    
    def dispose(self) -> None:
        """Dispose of this computed value and clean up dependencies."""
        if self._disposed:
            return
        self._disposed = True
        for dep in self._dependencies:
            dep._dependents.discard(self)
        self._dependencies.clear()
        self._dependents.clear()
        self._effects.clear()


class Effect:
    """An effect that runs side effects when its dependencies change."""
    
    def __init__(self, effect_fn: Callable[[], None]) -> None:
        self._effect_fn: Callable[[], None] = effect_fn
        self._dependencies: Set[Signal] = set()
        self._disposed: bool = False
        self._execute()
    
    def add_dependency(self, signal: Signal) -> None:
        """Add a dependency to this effect."""
        if self._disposed:
            return
        self._dependencies.add(signal)
        signal._effects.add(self)
    
    def _execute(self) -> None:
        """Execute the effect function and track dependencies."""
        if self._disposed:
            return
            
        # Clear previous dependencies
        for dep in self._dependencies:
            dep._effects.discard(self)
        self._dependencies.clear()
        
        # Execute effect with context tracking
        token = _reactive_context.set(self)
        try:
            self._effect_fn()
        finally:
            _reactive_context.reset(token)
    
    def dispose(self) -> None:
        """Dispose of this effect and clean up dependencies."""
        if self._disposed:
            return
        self._disposed = True
        for dep in self._dependencies:
            dep._effects.discard(self)
        self._dependencies.clear()


# Context management for tracking reactive dependencies
class _ReactiveContext:
    """Thread-local context for tracking reactive dependencies."""
    
    def __init__(self) -> None:
        self._context_stack: List[Any] = []
    
    def get(self) -> Any:
        """Get the current reactive context."""
        return self._context_stack[-1] if self._context_stack else None
    
    def set(self, context: Any) -> Any:
        """Set a new reactive context and return a token for resetting."""
        self._context_stack.append(context)
        return len(self._context_stack) - 1
    
    def reset(self, token: Any) -> None:
        """Reset the reactive context to a previous state."""
        if isinstance(token, int):
            # Remove all contexts added after the token
            while len(self._context_stack) > token:
                self._context_stack.pop()


_reactive_context = _ReactiveContext()


if __name__ == "__main__":
    # Self-test: computed values track their signals exactly, effects fire
    # per dependency change and stop after dispose, chains recompute.
    count = Signal(0)
    multiplier = Signal(2)
    doubled = Computed(lambda: count.value * 2)
    multiplied = Computed(lambda: count.value * multiplier.value)

    log = []
    effect1 = Effect(lambda: log.append(("doubled", doubled.value)))
    effect2 = Effect(lambda: log.append(("multiplied", multiplied.value)))

    # Initial: computed values exact; each effect ran once on creation.
    assert doubled.value == 0 and multiplied.value == 0
    assert log == [("doubled", 0), ("multiplied", 0)], f"initial effects wrong: {log}"

    # count=5: doubled 10, multiplied 10; BOTH effects re-fire with new values.
    count.value = 5
    assert doubled.value == 10, f"doubled must track count: {doubled.value}"
    assert multiplied.value == 10
    assert ("doubled", 10) in log and ("multiplied", 10) in log, f"effects stale: {log}"

    # multiplier=3 touches only `multiplied`: doubled's effect must NOT re-fire.
    n_doubled_before = sum(1 for k, _ in log if k == "doubled")
    multiplier.value = 3
    assert multiplied.value == 15, f"5*3 must be 15, got {multiplied.value}"
    assert doubled.value == 10
    n_doubled_after = sum(1 for k, _ in log if k == "doubled")
    assert n_doubled_after == n_doubled_before, \
        "doubled's effect fired for an unrelated signal"
    assert ("multiplied", 15) in log

    # A computed of computeds chains: (2c) + (3c) = 5c.
    total = Computed(lambda: doubled.value + multiplied.value)
    assert total.value == 25, f"10 + 15 must be 25, got {total.value}"
    count.value = 3
    assert total.value == 15, f"chain must recompute: 6 + 9 = 15, got {total.value}"
    assert doubled.value == 6 and multiplied.value == 9

    # DISPOSE: the effect stops observing; the other continues.
    n1 = len([1 for k, _ in log if k == "doubled"])
    effect1.dispose()
    count.value = 100
    assert doubled.value == 200, "computed itself must keep working after dispose"
    assert len([1 for k, _ in log if k == "doubled"]) == n1, \
        "disposed effect still fires"
    assert ("multiplied", 300) in log, "surviving effect missed the update"

    # Double-dispose is safe.
    effect1.dispose()
    effect2.dispose()
    count.value = 1
    n_total = len(log)
    count.value = 2
    assert len(log) == n_total, "all effects disposed but the log still grows"

    print("reactive_signals: computed exact (25→15 chain), unrelated signal "
          "didn't re-fire, dispose stops effects (200 vs silent) — PASS")