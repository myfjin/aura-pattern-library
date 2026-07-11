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
    """Self-test: every rendering feature asserted against its exact output —
    substitution, defaults, nested paths, loops, loop-scoped contexts."""
    engine = TemplateEngine()

    # Basic substitution is exact (round-trip a number through the template).
    assert engine.render("Hello {{ name }}!", Context({"name": "World"})) == "Hello World!"
    assert int(engine.render("{{ n }}", Context({"n": 42}))) == 42

    # Defaults fire only when the variable is missing.
    assert engine.render("Hello {{ name | Guest }}!", Context({})) == "Hello Guest!"
    assert engine.render("Hello {{ name | Guest }}!", Context({"name": "Zed"})) == "Hello Zed!", \
        "default overrode a present variable"

    # Nested dotted paths resolve.
    out = engine.render("User: {{ user.name }}, Age: {{ user.age }}",
                        Context({"user": {"name": "Alice", "age": 30}}))
    assert out == "User: Alice, Age: 30", f"nested paths wrong: {out!r}"

    # Loops render each element in order.
    out = engine.render("Items: {% for item in items %}{{ item }}, {% endfor %}",
                        Context({"items": ["apple", "banana", "cherry"]}))
    assert out == "Items: apple, banana, cherry, ", f"loop output wrong: {out!r}"

    # Loop over dicts: the loop variable scopes nested access per iteration.
    out = engine.render("{% for p in people %}{{ p.name }}={{ p.age }};{% endfor %}",
                        Context({"people": [{"name": "Alice", "age": 30},
                                            {"name": "Bob", "age": 25}]}))
    assert out == "Alice=30;Bob=25;", f"loop-scoped nesting wrong: {out!r}"

    # Empty list → loop body vanishes; non-list loop target renders nothing.
    assert engine.render("A{% for x in xs %}X{% endfor %}B", Context({"xs": []})) == "AB"
    assert engine.render("A{% for x in xs %}X{% endfor %}B", Context({"xs": 42})) == "AB", \
        "non-iterable loop target must render empty"

    # Defaults inside loop bodies (missing price falls back to 0).
    out = engine.render("{% for i in items %}{{ i.name }}:{{ i.price | 0 }} {% endfor %}",
                        Context({"items": [{"name": "Staff", "price": 100},
                                           {"name": "Ring"}]}))
    assert out == "Staff:100 Ring:0 ", f"loop defaults wrong: {out!r}"

    # The loop variable does not leak into the outer scope.
    ctx = Context({"items": ["x"]})
    engine.render("{% for item in items %}{{ item }}{% endfor %}", ctx)
    assert ctx.get("item") is None if hasattr(ctx, "get") else True

    # Type refusals.
    for bad_call in (lambda: engine.render(42, Context({})),
                     lambda: engine.render("x", {"not": "a context"})):
        try:
            bad_call()
            assert False, "invalid render arguments accepted"
        except TypeError:
            pass

    print("template_engine: substitution/defaults/nesting/loops all exact "
          "(Alice=30;Bob=25;), empty+non-list loops safe — PASS")


if __name__ == "__main__":
    main()