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
    """Self-test: the full lifecycle walked with every state asserted,
    entry/exit/handler hooks counted, guards veto, invalid events refused."""
    events = []
    sm = StateMachine("off")
    for name in ("off", "on", "error", "maintenance"):
        sm.add_state(State(name,
                           entry_action=(lambda n: lambda: events.append(f"enter:{n}"))(name),
                           exit_action=(lambda n: lambda: events.append(f"exit:{n}"))(name)))

    guard_calls = {"n": 0, "allow": True}
    def guard() -> bool:
        guard_calls["n"] += 1
        return guard_calls["allow"]

    sm.add_transition(Transition("off", "on", "power_on", guard=guard))
    sm.add_transition(Transition("on", "off", "power_off"))
    sm.add_transition(Transition("on", "error", "failure"))
    sm.add_transition(Transition("error", "maintenance", "repair"))
    sm.add_transition(Transition("maintenance", "off", "reset"))
    sm.on_event("power_on", lambda prev: events.append(f"handler:power_on:{prev}"))

    assert sm.get_current_state() == "off"

    # Walk the whole lifecycle; each step lands in the exact state.
    walk = [("power_on", "on"), ("failure", "error"), ("repair", "maintenance"),
            ("reset", "off"), ("power_on", "on"), ("power_off", "off")]
    for event, expected in walk:
        assert sm.trigger(event) is True, f"{event} refused"
        assert sm.get_current_state() == expected, \
            f"after {event} expected {expected}, in {sm.get_current_state()}"

    # Hooks fired in order for the first transition: exit old, enter new, handler.
    assert events[0] == "exit:off" and events[1] == "enter:on", \
        f"entry/exit order wrong: {events[:2]}"
    assert "handler:power_on:off" in events, "event handler missing or wrong prev state"
    assert events.count("enter:on") == 2 and events.count("exit:off") == 2
    assert guard_calls["n"] == 2, f"guard must run once per power_on, ran {guard_calls['n']}"

    # GUARD VETO: with the guard failing, the transition is refused and the
    # state does NOT move (and no phantom hooks fire).
    guard_calls["allow"] = False
    n_events = len(events)
    assert sm.trigger("power_on") is False, "guarded transition passed a failing guard"
    assert sm.get_current_state() == "off", "state moved despite guard veto"
    assert len(events) == n_events, "hooks fired for a vetoed transition"
    guard_calls["allow"] = True

    # Invalid events (no transition from the current state) are refused in place.
    assert sm.trigger("repair") is False, "event with no transition accepted"
    assert sm.get_current_state() == "off"
    assert sm.trigger("no_such_event") is False

    # Exactly 14 hook events: 6 transitions x 2 hooks + 2 power_on handlers.
    assert len(events) == 14, f"expected 14 hook events, got {len(events)}: {events}"

    print("state_machine: 6-step lifecycle exact, exit→enter→handler order, "
          "guard veto froze state, invalid events refused, 14 hooks — PASS")


if __name__ == "__main__":
    main()
