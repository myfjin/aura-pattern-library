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
    """Demo: Order processing saga with payment and inventory management."""
    
    # Create a saga for order processing
    order_saga = Saga("Order Processing Saga")
    
    # Step 1: Validate order
    def validate_order(context: SagaContext) -> bool:
        order_data = context.get("order")
        if not order_data:
            raise ValueError("No order data provided")
        
        if order_data.get("amount", 0) <= 0:
            raise ValueError("Invalid order amount")
        
        context.set("order_validated", True)
        logger.info(f"Order {order_data.get('id')} validated")
        return True
    
    def compensate_validate_order(context: SagaContext) -> None:
        order_data = context.get("order")
        logger.info(f"Compensating order validation for order {order_data.get('id')}")
        context.set("order_validated", False)
    
    validate_step = SagaStep(
        "Validate Order",
        validate_order,
        compensate_validate_order
    )
    order_saga.add_step(validate_step)
    
    # Step 2: Process payment
    def process_payment(context: SagaContext) -> str:
        order_data = context.get("order")
        if not context.get("order_validated"):
            raise RuntimeError("Order not validated")
        
        # Simulate payment processing
        payment_id = f"payment_{order_data.get('id')}"
        context.set("payment_id", payment_id)
        logger.info(f"Payment processed: {payment_id}")
        return payment_id
    
    def compensate_payment(context: SagaContext) -> None:
        payment_id = context.get("payment_id")
        logger.info(f"Refunding payment: {payment_id}")
        context.set("payment_refunded", True)
    
    payment_step = SagaStep(
        "Process Payment",
        process_payment,
        compensate_payment
    )
    order_saga.add_step(payment_step)
    
    # Step 3: Reserve inventory
    def reserve_inventory(context: SagaContext) -> List[str]:
        order_data = context.get("order")
        items = order_data.get("items", [])
        
        if not items:
            raise ValueError("No items in order")
        
        # Simulate inventory reservation
        reserved_items = [f"reserved_{item}" for item in items]
        context.set("reserved_items", reserved_items)
        logger.info(f"Inventory reserved: {reserved_items}")
        return reserved_items
    
    def compensate_inventory(context: SagaContext) -> None:
        reserved_items = context.get("reserved_items", [])
        logger.info(f"Releasing reserved inventory: {reserved_items}")
        context.set("inventory_released", True)
    
    inventory_step = SagaStep(
        "Reserve Inventory",
        reserve_inventory,
        compensate_inventory
    )
    order_saga.add_step(inventory_step)
    
    # Step 4: Confirm order (this step will fail to demonstrate compensation)
    def confirm_order(context: SagaContext) -> str:
        # Simulate a failure in the final step
        raise RuntimeError("Warehouse system unavailable")
        
        # This code would normally execute:
        # order_id = context.get("order", {}).get("id")
        # confirmation_id = f"confirm_{order_id}"
        # context.set("confirmation_id", confirmation_id)
        # logger.info(f"Order confirmed: {confirmation_id}")
        # return confirmation_id
    
    def compensate_confirm(context: SagaContext) -> None:
        confirmation_id = context.get("confirmation_id")
        if confirmation_id:
            logger.info(f"Canceling order confirmation: {confirmation_id}")
            context.set("confirmation_canceled", True)
    
    confirm_step = SagaStep(
        "Confirm Order",
        confirm_order,
        compensate_confirm
    )
    order_saga.add_step(confirm_step)
    
    # Set up order data in context
    order_saga.context.set("order", {
        "id": "order_12345",
        "amount": 99.99,
        "items": ["item_A", "item_B"]
    })
    
    # Execute the saga
    success = order_saga.execute()
    
    # Print results
    print(f"\nSaga Execution Result: {'SUCCESS' if success else 'FAILED'}")
    print(f"Final Saga Status: {order_saga.status.value}")
    print(f"Context Data: {order_saga.context.data}")
    
    # Demonstrate a successful saga
    print("\n" + "="*50)
    print("DEMONSTRATING SUCCESSFUL SAGA")
    print("="*50)
    
    # Create a successful saga
    successful_saga = Saga("Successful Order Processing")
    
    # Add the same steps but with a working confirmation
    def working_confirm_order(context: SagaContext) -> str:
        order_id = context.get("order", {}).get("id")
        confirmation_id = f"confirm_{order_id}"
        context.set("confirmation_id", confirmation_id)
        logger.info(f"Order confirmed: {confirmation_id}")
        return confirmation_id
    
    # Add all steps to the successful saga
    successful_saga.add_step(validate_step)
    successful_saga.add_step(payment_step)
    successful_saga.add_step(inventory_step)
    
    # Add working confirmation step
    working_confirm_step = SagaStep(
        "Confirm Order",
        working_confirm_order,
        compensate_confirm
    )
    successful_saga.add_step(working_confirm_step)
    
    # Set up order data
    successful_saga.context.set("order", {
        "id": "order_67890",
        "amount": 149.99,
        "items": ["item_C", "item_D"]
    })
    
    # Execute the successful saga
    success2 = successful_saga.execute()
    
    print(f"\nSaga Execution Result: {'SUCCESS' if success2 else 'FAILED'}")
    print(f"Final Saga Status: {successful_saga.status.value}")
    print(f"Context Data: {successful_saga.context.data}")


if __name__ == "__main__":
    main()