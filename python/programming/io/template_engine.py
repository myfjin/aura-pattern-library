#!/usr/bin/env python3
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import re
from typing import Any, Dict, List, Union, Optional


class Context:
    """A context object that holds variables for template rendering."""
    
    def __init__(self, variables: Optional[Dict[str, Any]] = None):
        """Initialize the context with optional variables.
        
        Args:
            variables: A dictionary of variable names and values.
        """
        self.variables = variables or {}
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a variable value by key with optional default.
        
        Args:
            key: The variable name to look up.
            default: The default value if key is not found.
            
        Returns:
            The variable value or default.
        """
        return self.variables.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set a variable in the context.
        
        Args:
            key: The variable name.
            value: The variable value.
        """
        self.variables[key] = value


class TemplateEngine:
    """A simple template engine supporting variable substitution and loops."""
    
    def __init__(self):
        """Initialize the template engine."""
        # Pattern for variable substitution: {{ variable }}
        self.var_pattern = re.compile(r'\{\{\s*([a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*)\s*\}\}')
        # Pattern for variable with default: {{ variable | default }}
        self.default_pattern = re.compile(r'\{\{\s*([a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*)\s*\|\s*([^}]+)\s*\}\}')
        # Pattern for loops: {% for item in list %}...{% endfor %}
        self.loop_pattern = re.compile(r'\{%\s*for\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+in\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*%\}(.*?){%\s*endfor\s*%\}', re.DOTALL)
    
    def _get_nested_value(self, context: Context, key: str) -> Any:
        """Get a nested value from context using dot notation.
        
        Args:
            context: The context to look up values in.
            key: The key with possible dot notation (e.g., 'user.name').
            
        Returns:
            The resolved value or None if not found.
        """
        parts = key.split('.')
        value = context.get(parts[0])
        
        if value is None:
            return None
            
        for part in parts[1:]:
            if isinstance(value, dict) and part in value:
                value = value[part]
            else:
                return None
                
        return value
    
    def _render_variables(self, template: str, context: Context) -> str:
        """Render variable substitutions in template.
        
        Args:
            template: The template string.
            context: The context with variables.
            
        Returns:
            The template with variables substituted.
        """
        # Handle defaults first
        def default_replacer(match):
            key = match.group(1)
            default_val = match.group(2).strip()
            value = self._get_nested_value(context, key)
            if value is None:
                return default_val
            return str(value)
        
        result = self.default_pattern.sub(default_replacer, template)
        
        # Handle regular variables
        def var_replacer(match):
            key = match.group(1)
            value = self._get_nested_value(context, key)
            if value is None:
                return ''
            return str(value)
        
        result = self.var_pattern.sub(var_replacer, result)
        return result
    
    def _render_loops(self, template: str, context: Context) -> str:
        """Render loop constructs in template.
        
        Args:
            template: The template string.
            context: The context with variables.
            
        Returns:
            The template with loops rendered.
        """
        def loop_replacer(match):
            loop_var = match.group(1)
            list_var = match.group(2)
            inner_template = match.group(3)
            
            list_value = self._get_nested_value(context, list_var)
            if not isinstance(list_value, (list, tuple)):
                return ''
            
            result = ''
            for item in list_value:
                # Create a new context for each iteration
                loop_context = Context(context.variables.copy())
                loop_context.set(loop_var, item)
                # Render the inner template with the loop context
                rendered = self._render_variables(inner_template, loop_context)
                result += rendered
                
            return result
        
        # Keep processing loops until none are left (handle nested loops)
        while self.loop_pattern.search(template):
            template = self.loop_pattern.sub(loop_replacer, template)
            
        return template
    
    def render(self, template: str, context: Context) -> str:
        """Render a template with the given context.
        
        Args:
            template: The template string to render.
            context: The context with variables.
            
        Returns:
            The rendered template string.
            
        Raises:
            TypeError: If template is not a string or context is not a Context.
        """
        if not isinstance(template, str):
            raise TypeError("Template must be a string")
        
        if not isinstance(context, Context):
            raise TypeError("Context must be a Context instance")
        
        # First process loops, then variables
        result = self._render_loops(template, context)
        result = self._render_variables(result, context)
        
        return result


def main():
    """Demo the template engine functionality."""
    engine = TemplateEngine()
    
    # Test 1: Basic variable substitution
    template1 = "Hello {{ name }}!"
    context1 = Context({"name": "World"})
    result1 = engine.render(template1, context1)
    print(f"Test 1: {result1}")
    
    # Test 2: Variable with default
    template2 = "Hello {{ name | Guest }}!"
    context2 = Context({})
    result2 = engine.render(template2, context2)
    print(f"Test 2: {result2}")
    
    # Test 3: Nested variables
    template3 = "User: {{ user.name }}, Age: {{ user.age }}"
    context3 = Context({"user": {"name": "Alice", "age": 30}})
    result3 = engine.render(template3, context3)
    print(f"Test 3: {result3}")
    
    # Test 4: Simple loop
    template4 = "Items: {% for item in items %}{{ item }}, {% endfor %}"
    context4 = Context({"items": ["apple", "banana", "cherry"]})
    result4 = engine.render(template4, context4)
    print(f"Test 4: {result4}")
    
    # Test 5: Loop with nested variables
    template5 = "{% for person in people %}Name: {{ person.name }}, Age: {{ person.age }}\n{% endfor %}"
    context5 = Context({
        "people": [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25}
        ]
    })
    result5 = engine.render(template5, context5)
    print(f"Test 5:\n{result5}")
    
    # Test 6: Complex template with loops and defaults
    template6 = """
Greetings {{ user.name | Friend }}!

Your items:
{% for item in items %}
- {{ item.name }} ({{ item.price | 0 }} gold)
{% endfor %}
"""
    context6 = Context({
        "user": {"name": "Gandalf"},
        "items": [
            {"name": "Staff", "price": 100},
            {"name": "Hat", "price": 50},
            {"name": "Ring"}  # No price
        ]
    })
    result6 = engine.render(template6, context6)
    print(f"Test 6:{result6}")


if __name__ == "__main__":
    main()