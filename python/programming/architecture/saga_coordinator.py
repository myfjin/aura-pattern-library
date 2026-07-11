"""
Saga Pattern Coordinator Module

This module implements the Saga pattern for distributed transactions,
providing forward execution and backward compensation on failure.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Callable, Any, Optional, Dict
from dataclasses import dataclass
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SagaStatus(Enum):
    """Enumeration of possible saga statuses."""
    PENDING = "pending"
    EXECUTING = "executing"
    COMPLETED = "completed"
    COMPENSATING = "compensating"
    FAILED = "failed"


@dataclass
class SagaContext:
    """Context object that carries data between saga steps."""
    data: Dict[str, Any]
    
    def __init__(self):
        self.data = {}
    
    def set(self, key: str, value: Any) -> None:
        """Set a value in the context."""
        self.data[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from the context."""
        return self.data.get(key, default)


class SagaStep:
    """
    Represents a single step in a saga transaction.
    
    Each step has a forward action and an optional compensating action
    for rollback scenarios.
    """
    
    def __init__(
        self,
        name: str,
        forward_action: Callable[[SagaContext], Any],
        compensating_action: Optional[Callable[[SagaContext], Any]] = None
    ):
        """
        Initialize a saga step.
        
        Args:
            name: Name of the step for logging and identification
            forward_action: Function to execute during forward processing
            compensating_action: Function to execute during compensation
        """
        self.name = name
        self.forward_action = forward_action
        self.compensating_action = compensating_action
    
    def execute(self, context: SagaContext) -> Any:
        """
        Execute the forward action of this step.
        
        Args:
            context: The saga context
            
        Returns:
            Result of the forward action
            
        Raises:
            Exception: If the forward action fails
        """
        logger.info(f"Executing step: {self.name}")
        try:
            result = self.forward_action(context)
            logger.info(f"Step {self.name} completed successfully")
            return result
        except Exception as e:
            logger.error(f"Step {self.name} failed: {str(e)}")
            raise
    
    def compensate(self, context: SagaContext) -> None:
        """
        Execute the compensating action of this step.
        
        Args:
            context: The saga context
            
        Raises:
            Exception: If the compensating action fails
        """
        if self.compensating_action is None:
            logger.warning(f"Step {self.name} has no compensating action")
            return
            
        logger.info(f"Compensating step: {self.name}")
        try:
            self.compensating_action(context)
            logger.info(f"Step {self.name} compensated successfully")
        except Exception as e:
            logger.error(f"Compensation for step {self.name} failed: {str(e)}")
            raise


class Saga:
    """
    Saga coordinator that manages execution and compensation of steps.
    
    Implements the Saga pattern for distributed transactions with
    automatic rollback on failure.
    """
    
    def __init__(self, name: str):
        """
        Initialize a saga coordinator.
        
        Args:
            name: Name of the saga for logging and identification
        """
        self.name = name
        self.steps: List[SagaStep] = []
        self.executed_steps: List[SagaStep] = []
        self.status = SagaStatus.PENDING
        self.context = SagaContext()
    
    def add_step(self, step: SagaStep) -> None:
        """
        Add a step to the saga.
        
        Args:
            step: The saga step to add
        """
        self.steps.append(step)
    
    def execute(self) -> bool:
        """
        Execute the saga by running all steps in order.
        
        If any step fails, compensation is automatically triggered
        for all previously executed steps.
        
        Returns:
            True if saga completed successfully, False otherwise
        """
        logger.info(f"Starting saga: {self.name}")
        self.status = SagaStatus.EXECUTING
        
        try:
            for step in self.steps:
                # Execute the step
                step.execute(self.context)
                self.executed_steps.append(step)
            
            self.status = SagaStatus.COMPLETED
            logger.info(f"Saga {self.name} completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Saga {self.name} failed: {str(e)}")
            self.status = SagaStatus.FAILED
            self._compensate()
            return False
    
    def _compensate(self) -> None:
        """
        Execute compensation for all successfully executed steps.
        
        Compensation is performed in reverse order of execution.
        """
        logger.info(f"Starting compensation for saga: {self.name}")
        self.status = SagaStatus.COMPENSATING
        
        # Compensate in reverse order
        for step in reversed(self.executed_steps):
            try:
                step.compensate(self.context)
            except Exception as e:
                logger.error(f"Compensation failed for step {step.name}: {str(e)}")
                # Continue with other compensations even if one fails
        
        self.status = SagaStatus.FAILED
        logger.info(f"Compensation completed for saga: {self.name}")


class CompensatingAction:
    """
    Helper class for creating compensating actions.
    
    Provides utility methods for common compensation scenarios.
    """
    
    @staticmethod
    def create_simple_compensation(
        action_name: str,
        compensation_func: Callable[[SagaContext], None]
    ) -> Callable[[SagaContext], None]:
        """
        Create a simple compensating action.
        
        Args:
            action_name: Name for logging
            compensation_func: Function to execute for compensation
            
        Returns:
            Compensation function
        """
        def compensator(context: SagaContext) -> None:
            logger.info(f"Performing compensation: {action_name}")
            compensation_func(context)
        return compensator
    
    @staticmethod
    def create_noop_compensation() -> Callable[[SagaContext], None]:
        """
        Create a no-op compensating action.
        
        Returns:
            No-op compensation function
        """
        def compensator(context: SagaContext) -> None:
            logger.info("No compensation needed")
        return compensator


def main():
    """Self-test: a failing saga compensates every EXECUTED step in exact
    reverse order and reports FAILED; a clean saga completes with no
    compensation and exact context state."""
    trace = []

    def mk_step(name, fail=False):
        def action(context):
            if fail:
                raise RuntimeError(f"{name} exploded")
            trace.append(f"do:{name}")
            context.set(name, True)
            return name
        def compensate(context):
            trace.append(f"undo:{name}")
            context.set(f"{name}_compensated", True)
        return SagaStep(name, action, compensate)

    # FAILING SAGA: steps A, B succeed; C fails; D never runs.
    saga = Saga("failing")
    for step in (mk_step("A"), mk_step("B"), mk_step("C", fail=True), mk_step("D")):
        saga.add_step(step)
    ok = saga.execute()
    assert ok is False, "failing saga reported success"
    assert saga.status == SagaStatus.FAILED

    # Execution stopped at the failure; D never ran; nothing after C did.
    assert trace == ["do:A", "do:B", "undo:B", "undo:A"], \
        f"compensation must undo executed steps in REVERSE order: {trace}"
    assert saga.context.get("A_compensated") is True
    assert saga.context.get("B_compensated") is True
    assert saga.context.get("C_compensated") is None, \
        "the FAILING step (never executed) was compensated"
    assert saga.context.get("D") is None, "step after the failure executed"

    # SUCCESSFUL SAGA: all steps run, zero compensations, exact context.
    trace.clear()
    good = Saga("good")
    for name in ("V", "P", "I"):
        good.add_step(mk_step(name))
    ok = good.execute()
    assert ok is True and good.status == SagaStatus.COMPLETED
    assert trace == ["do:V", "do:P", "do:I"], f"clean run trace wrong: {trace}"
    assert not any(t.startswith("undo") for t in trace), \
        "a successful saga ran compensations"
    assert all(good.context.get(n) is True for n in ("V", "P", "I"))
    n_executed = len(good.executed_steps)
    assert n_executed == 3, f"3 steps must be recorded as executed, got {n_executed}"

    # A failing COMPENSATION must not abort the remaining compensations.
    trace.clear()
    tough = Saga("tough-compensation")
    def bad_undo(context):
        raise RuntimeError("compensation itself failed")
    tough.add_step(SagaStep("first", lambda c: trace.append("do:first"), bad_undo))
    tough.add_step(mk_step("second"))
    tough.add_step(mk_step("boom", fail=True))
    assert tough.execute() is False
    assert "undo:second" in trace, "good compensation skipped"
    assert tough.context.get("second_compensated") is True, \
        "a crashing compensation aborted the rest of the rollback"

    print("saga_coordinator: failure → undo B,A in reverse (C/D untouched), "
          "clean run 3/3 no undo, crashing compensation contained — PASS")


if __name__ == "__main__":
    main()
