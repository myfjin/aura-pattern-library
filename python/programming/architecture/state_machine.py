"""
Simple State Machine Engine

This module provides a complete state machine implementation with support for
states, transitions, guards, actions, and entry/exit hooks.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, List, Optional, Callable, Any, Set
from dataclasses import dataclass


class StateMachineError(Exception):
    """Base exception for state machine errors."""
    pass


@dataclass
class Transition:
    """
    Represents a transition between states.
    
    Attributes:
        source: The source state name
        target: The target state name
        event: The event that triggers this transition
        guard: Optional guard condition (callable that returns bool)
        action: Optional action to execute during transition
    """
    source: str
    target: str
    event: str
    guard: Optional[Callable[[], bool]] = None
    action: Optional[Callable[[], None]] = None


class State:
    """
    Represents a state in the state machine.
    
    Attributes:
        name: Unique identifier for the state
        entry_action: Optional action executed when entering the state
        exit_action: Optional action executed when exiting the state
    """
    
    def __init__(self, name: str, 
                 entry_action: Optional[Callable[[], None]] = None,
                 exit_action: Optional[Callable[[], None]] = None):
        self.name = name
        self.entry_action = entry_action
        self.exit_action = exit_action


class StateMachine:
    """
    A finite state machine implementation.
    
    Supports states, transitions, guards, actions, and entry/exit hooks.
    """
    
    def __init__(self, initial_state: str):
        self.states: Dict[str, State] = {}
        self.transitions: List[Transition] = []
        self.current_state: Optional[str] = initial_state
        self._event_handlers: Dict[str, List[Callable[[str], None]]] = {}
    
    def add_state(self, state: State) -> None:
        """Add a state to the state machine."""
        if state.name in self.states:
            raise StateMachineError(f"State '{state.name}' already exists")
        self.states[state.name] = state
    
    def add_transition(self, transition: Transition) -> None:
        """Add a transition to the state machine."""
        if transition.source not in self.states:
            raise StateMachineError(f"Source state '{transition.source}' does not exist")
        if transition.target not in self.states:
            raise StateMachineError(f"Target state '{transition.target}' does not exist")
        self.transitions.append(transition)
    
    def on_event(self, event: str, handler: Callable[[str], None]) -> None:
        """Register an event handler that gets called after each event processing."""
        if event not in self._event_handlers:
            self._event_handlers[event] = []
        self._event_handlers[event].append(handler)
    
    def trigger(self, event: str) -> bool:
        """
        Trigger an event and attempt to transition.
        
        Returns:
            True if a transition occurred, False otherwise
        """
        if self.current_state is None:
            raise StateMachineError("State machine not initialized")
        
        # Find valid transitions
        valid_transitions = []
        for transition in self.transitions:
            if (transition.source == self.current_state and 
                transition.event == event):
                # Check guard condition if present
                if transition.guard is None or transition.guard():
                    valid_transitions.append(transition)
        
        if not valid_transitions:
            return False
        
        if len(valid_transitions) > 1:
            raise StateMachineError(f"Ambiguous transition for event '{event}' in state '{self.current_state}'")
        
        transition = valid_transitions[0]
        
        # Execute exit action of current state
        current_state_obj = self.states[self.current_state]
        if current_state_obj.exit_action:
            current_state_obj.exit_action()
        
        # Execute transition action
        if transition.action:
            transition.action()
        
        # Change state
        previous_state = self.current_state
        self.current_state = transition.target
        
        # Execute entry action of new state
        new_state_obj = self.states[self.current_state]
        if new_state_obj.entry_action:
            new_state_obj.entry_action()
        
        # Notify event handlers
        if event in self._event_handlers:
            for handler in self._event_handlers[event]:
                handler(previous_state)
        
        return True
    
    def get_current_state(self) -> str:
        """Get the current state name."""
        if self.current_state is None:
            raise StateMachineError("State machine not initialized")
        return self.current_state


def main():
    """Demo of the state machine with 4 states: off, on, error, and maintenance."""
    
    # Create state machine with initial state 'off'
    sm = StateMachine("off")
    
    # Define entry/exit actions
    def log_entry(state_name: str) -> Callable[[], None]:
        def action():
            print(f"Entering state: {state_name}")
        return action
    
    def log_exit(state_name: str) -> Callable[[], None]:
        def action():
            print(f"Exiting state: {state_name}")
        return action
    
    # Add states
    sm.add_state(State("off", entry_action=log_entry("off"), exit_action=log_exit("off")))
    sm.add_state(State("on", entry_action=log_entry("on"), exit_action=log_exit("on")))
    sm.add_state(State("error", entry_action=log_entry("error"), exit_action=log_exit("error")))
    sm.add_state(State("maintenance", entry_action=log_entry("maintenance"), exit_action=log_exit("maintenance")))
    
    # Define guards
    def is_safe_to_turn_on() -> bool:
        print("Checking if it's safe to turn on...")
        return True  # In a real system, this might check sensors
    
    def is_safe_to_turn_off() -> bool:
        print("Checking if it's safe to turn off...")
        return True  # In a real system, this might check state
    
    # Add transitions
    sm.add_transition(Transition("off", "on", "power_on", guard=is_safe_to_turn_on))
    sm.add_transition(Transition("on", "off", "power_off", guard=is_safe_to_turn_off))
    sm.add_transition(Transition("on", "error", "failure"))
    sm.add_transition(Transition("error", "maintenance", "repair"))
    sm.add_transition(Transition("maintenance", "off", "reset"))
    
    # Add event handlers
    def on_power_on(previous_state: str) -> None:
        print(f"Device powered on from {previous_state}")
    
    def on_power_off(previous_state: str) -> None:
        print(f"Device powered off from {previous_state}")
    
    sm.on_event("power_on", on_power_on)
    sm.on_event("power_off", on_power_off)
    
    # Run demo sequence
    print("=== State Machine Demo ===")
    print(f"Initial state: {sm.get_current_state()}")
    
    # Turn on
    print("\n1. Triggering 'power_on' event:")
    success = sm.trigger("power_on")
    print(f"Transition successful: {success}")
    print(f"Current state: {sm.get_current_state()}")
    
    # Simulate failure
    print("\n2. Triggering 'failure' event:")
    success = sm.trigger("failure")
    print(f"Transition successful: {success}")
    print(f"Current state: {sm.get_current_state()}")
    
    # Repair
    print("\n3. Triggering 'repair' event:")
    success = sm.trigger("repair")
    print(f"Transition successful: {success}")
    print(f"Current state: {sm.get_current_state()}")
    
    # Reset
    print("\n4. Triggering 'reset' event:")
    success = sm.trigger("reset")
    print(f"Transition successful: {success}")
    print(f"Current state: {sm.get_current_state()}")
    
    # Turn on again
    print("\n5. Triggering 'power_on' event again:")
    success = sm.trigger("power_on")
    print(f"Transition successful: {success}")
    print(f"Current state: {sm.get_current_state()}")
    
    # Turn off
    print("\n6. Triggering 'power_off' event:")
    success = sm.trigger("power_off")
    print(f"Transition successful: {success}")
    print(f"Current state: {sm.get_current_state()}")
    
    # Try invalid transition
    print("\n7. Trying invalid transition 'power_on' from 'off' with guard failure:")
    # Temporarily override guard to simulate failure
    original_guard = None
    for t in sm.transitions:
        if t.source == "off" and t.event == "power_on":
            original_guard = t.guard
            t.guard = lambda: False  # Always fail
            break
    
    success = sm.trigger("power_on")
    print(f"Transition successful: {success}")
    print(f"Current state: {sm.get_current_state()}")
    
    # Restore guard
    for t in sm.transitions:
        if t.source == "off" and t.event == "power_on":
            t.guard = original_guard
            break


if __name__ == "__main__":
    main()