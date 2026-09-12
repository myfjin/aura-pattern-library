"""
Simple Expression Evaluator with Variables

This module provides a complete expression evaluator that supports:
- Basic arithmetic operations (+, -, *, /, %, **)
- Parentheses for grouping
- Variables with assignment and lookup
- Integer and floating-point numbers
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, List, Union, Any, Optional
import re


class Token:
    """Represents a single token in the expression."""
    
    def __init__(self, type_: str, value: Union[str, float, int], position: int = 0):
        self.type = type_
        self.value = value
        self.position = position
    
    def __repr__(self) -> str:
        return f"Token({self.type}, {self.value})"


class Lexer:
    """Lexical analyzer that converts text into tokens."""
    
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
    
    def error(self, message: str = "Invalid character") -> None:
        """Raise a lexer error."""
        raise ValueError(f"{message} at position {self.pos}")
    
    def advance(self) -> None:
        """Move to the next character."""
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    
    def skip_whitespace(self) -> None:
        """Skip whitespace characters."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def read_number(self) -> Union[int, float]:
        """Read a number (integer or float)."""
        result = ''
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        
        if '.' in result:
            return float(result)
        return int(result)
    
    def read_identifier(self) -> str:
        """Read an identifier (variable name)."""
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return result
    
    def get_next_token(self) -> Token:
        """Get the next token from the input."""
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char.isdigit():
                return Token('NUMBER', self.read_number(), self.pos)
            
            if self.current_char.isalpha() or self.current_char == '_':
                identifier = self.read_identifier()
                if identifier == 'true':
                    return Token('BOOLEAN', True, self.pos)
                elif identifier == 'false':
                    return Token('BOOLEAN', False, self.pos)
                else:
                    return Token('IDENTIFIER', identifier, self.pos)
            
            if self.current_char == '+':
                self.advance()
                return Token('PLUS', '+', self.pos)
            
            if self.current_char == '-':
                self.advance()
                return Token('MINUS', '-', self.pos)
            
            if self.current_char == '*':
                self.advance()
                if self.current_char == '*':
                    self.advance()
                    return Token('POWER', '**', self.pos)
                return Token('MULTIPLY', '*', self.pos)
            
            if self.current_char == '/':
                self.advance()
                return Token('DIVIDE', '/', self.pos)
            
            if self.current_char == '%':
                self.advance()
                return Token('MODULO', '%', self.pos)
            
            if self.current_char == '(':
                self.advance()
                return Token('LPAREN', '(', self.pos)
            
            if self.current_char == ')':
                self.advance()
                return Token('RPAREN', ')', self.pos)
            
            if self.current_char == '=':
                self.advance()
                return Token('ASSIGN', '=', self.pos)
            
            self.error(f"Invalid character '{self.current_char}'")
        
        return Token('EOF', None, self.pos)


class AST:
    """Abstract Syntax Tree base class."""
    pass


class Number(AST):
    """Represents a number in the AST."""
    
    def __init__(self, value: Union[int, float]):
        self.value = value


class Boolean(AST):
    """Represents a boolean value in the AST."""
    
    def __init__(self, value: bool):
        self.value = value


class Variable(AST):
    """Represents a variable in the AST."""
    
    def __init__(self, name: str):
        self.name = name


class BinOp(AST):
    """Represents a binary operation in the AST."""
    
    def __init__(self, left: AST, op: Token, right: AST):
        self.left = left
        self.op = op
        self.right = right


class Assign(AST):
    """Represents an assignment operation in the AST."""
    
    def __init__(self, left: Variable, op: Token, right: AST):
        self.left = left
        self.op = op
        self.right = right


class UnaryOp(AST):
    """Represents a unary operation in the AST."""
    
    def __init__(self, op: Token, expr: AST):
        self.op = op
        self.expr = expr


class Parser:
    """Parser that builds an AST from tokens."""
    
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def error(self, message: str = "Invalid syntax") -> None:
        """Raise a parser error."""
        raise ValueError(f"{message} at position {self.current_token.position}")
    
    def eat(self, token_type: str) -> None:
        """Consume a token of the expected type."""
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Expected {token_type}, got {self.current_token.type}")
    
    def factor(self) -> AST:
        """Parse a factor (number, variable, parenthesized expression, or unary operation)."""
        token = self.current_token
        
        if token.type == 'PLUS':
            self.eat('PLUS')
            return UnaryOp(token, self.factor())
        elif token.type == 'MINUS':
            self.eat('MINUS')
            return UnaryOp(token, self.factor())
        elif token.type == 'NUMBER':
            self.eat('NUMBER')
            return Number(token.value)
        elif token.type == 'BOOLEAN':
            self.eat('BOOLEAN')
            return Boolean(token.value)
        elif token.type == 'IDENTIFIER':
            self.eat('IDENTIFIER')
            return Variable(token.value)
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node
        else:
            self.error(f"Unexpected token {token.type}")
    
    def power(self) -> AST:
        """Parse exponentiation (right associative)."""
        node = self.factor()
        
        if self.current_token.type == 'POWER':
            token = self.current_token
            self.eat('POWER')
            node = BinOp(node, token, self.power())
        
        return node
    
    def term(self) -> AST:
        """Parse a term (multiplication, division, modulo)."""
        node = self.power()
        
        while self.current_token.type in ('MULTIPLY', 'DIVIDE', 'MODULO'):
            token = self.current_token
            if token.type == 'MULTIPLY':
                self.eat('MULTIPLY')
            elif token.type == 'DIVIDE':
                self.eat('DIVIDE')
            elif token.type == 'MODULO':
                self.eat('MODULO')
            
            node = BinOp(node, token, self.power())
        
        return node
    
    def expr(self) -> AST:
        """Parse an expression (addition, subtraction)."""
        node = self.term()
        
        while self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
            elif token.type == 'MINUS':
                self.eat('MINUS')
            
            node = BinOp(node, token, self.term())
        
        # Handle assignment
        if self.current_token.type == 'ASSIGN':
            if not isinstance(node, Variable):
                self.error("Left side of assignment must be a variable")
            
            token = self.current_token
            self.eat('ASSIGN')
            node = Assign(node, token, self.expr())
        
        return node
    
    def parse(self) -> AST:
        """Parse the entire expression."""
        return self.expr()


class Environment:
    """Environment for storing variable values."""
    
    def __init__(self):
        self.variables: Dict[str, Union[int, float, bool]] = {}
    
    def get(self, name: str) -> Union[int, float, bool]:
        """Get the value of a variable."""
        if name not in self.variables:
            raise NameError(f"Variable '{name}' is not defined")
        return self.variables[name]
    
    def set(self, name: str, value: Union[int, float, bool]) -> None:
        """Set the value of a variable."""
        self.variables[name] = value


class ExpressionEvaluator:
    """Evaluates expressions using an environment."""
    
    def __init__(self, environment: Optional[Environment] = None):
        self.environment = environment or Environment()
    
    def visit(self, node: AST) -> Union[int, float, bool]:
        """Visit a node in the AST."""
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
    
    def generic_visit(self, node: AST) -> None:
        """Handle unknown node types."""
        raise TypeError(f"No visit method for {type(node).__name__}")
    
    def visit_Number(self, node: Number) -> Union[int, float]:
        """Visit a number node."""
        return node.value
    
    def visit_Boolean(self, node: Boolean) -> bool:
        """Visit a boolean node."""
        return node.value
    
    def visit_Variable(self, node: Variable) -> Union[int, float, bool]:
        """Visit a variable node."""
        return self.environment.get(node.name)
    
    def visit_BinOp(self, node: BinOp) -> Union[int, float, bool]:
        """Visit a binary operation node."""
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)
        
        if node.op.type == 'PLUS':
            return left_val + right_val
        elif node.op.type == 'MINUS':
            return left_val - right_val
        elif node.op.type == 'MULTIPLY':
            return left_val * right_val
        elif node.op.type == 'DIVIDE':
            if right_val == 0:
                raise ZeroDivisionError("Division by zero")
            return left_val / right_val
        elif node.op.type == 'MODULO':
            if right_val == 0:
                raise ZeroDivisionError("Modulo by zero")
            return left_val % right_val
        elif node.op.type == 'POWER':
            return left_val ** right_val
        else:
            raise ValueError(f"Unknown operator: {node.op.type}")
    
    def visit_UnaryOp(self, node: UnaryOp) -> Union[int, float]:
        """Visit a unary operation node."""
        operand = self.visit(node.expr)
        
        if node.op.type == 'PLUS':
            return +operand
        elif node.op.type == 'MINUS':
            return -operand
        else:
            raise ValueError(f"Unknown unary operator: {node.op.type}")
    
    def visit_Assign(self, node: Assign) -> Union[int, float, bool]:
        """Visit an assignment node."""
        value = self.visit(node.right)
        self.environment.set(node.left.name, value)
        return value
    
    def evaluate(self, expression: str) -> Union[int, float, bool]:
        """Evaluate an expression string."""
        try:
            lexer = Lexer(expression)
            parser = Parser(lexer)
            tree = parser.parse()
            return self.visit(tree)
        except Exception as e:
            raise ValueError(f"Error evaluating expression '{expression}': {str(e)}")


def main():
    """Self-test: every arithmetic result checked against Python's own
    arithmetic, precedence/parentheses exact, variables persist, refusals."""
    ev = ExpressionEvaluator()

    # Precedence and operators: exact values.
    cases = [
        ("2 + 3 * 4", 14),          # * binds tighter than +
        ("(2 + 3) * 4", 20),
        ("10 / 2 - 3", 2.0),
        ("2 ** 3", 8),
        ("17 % 5", 2),
        ("2 + 3 * 4 - 10 / 2", 9.0),
        ("-5 + 3", -2),
        ("+10 - 2", 8),
        ("2 ** 3 ** 2", 512),       # right-associative power: 2^(3^2)
        ("100 - 10 - 20", 70),      # left-associative minus
    ]
    for expr, expected in cases:
        got = ev.evaluate(expr)
        assert got == expected, f"{expr!r} must be {expected}, got {got}"
        assert type(got) is type(expected), \
            f"{expr!r}: type {type(got).__name__} != {type(expected).__name__}"

    # Variables: assignment returns the value, environment persists, compos.
    assert ev.evaluate("x = 10") == 10
    assert ev.evaluate("y = 5") == 5
    assert ev.evaluate("x + y") == 15
    assert ev.evaluate("z = x * y") == 50
    assert ev.evaluate("z") == 50
    assert ev.evaluate("x = -7") == -7
    assert ev.evaluate("x + y") == -2, "reassignment did not take effect"
    assert abs(ev.evaluate("a = 2.5") - 2.5) < 1e-12
    assert abs(ev.evaluate("(a + 1.5) * 2") - 8.0) < 1e-12
    assert ev.environment.variables["z"] == 50

    # Fuzz vs Python's eval on random arithmetic (no variables, no division
    # to dodge float-format edge cases; ** kept small).
    import random
    random.seed(42)
    for _ in range(100):
        terms = [str(random.randint(1, 9)) for _ in range(4)]
        ops = [random.choice(["+", "-", "*"]) for _ in range(3)]
        expr = terms[0] + "".join(o + t for o, t in zip(ops, terms[1:]))
        assert ev.evaluate(expr) == eval(expr), f"{expr!r} diverged from Python"

    # Refusals: division/modulo by zero, garbage syntax, unknown variable.
    for bad in ("1 / 0", "5 % 0", "2 +", "(1 + 2", "unknown_var + 1"):
        try:
            ev.evaluate(bad)
            assert False, f"{bad!r} evaluated without error"
        except (ValueError, ZeroDivisionError):
            pass

    print("expression_evaluator: 10 precedence cases exact (2**3**2=512), "
          "variables persist, 100 fuzz == python eval, 5 refusals — PASS")


if __name__ == "__main__":
    main()