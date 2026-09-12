package main

import (
	"fmt"
	"math"
	"math/rand"
	"os"
	"strconv"
	"strings"
)

// Arithmetic expression evaluator: a lexer + recursive-descent parser build an AST
// honoring precedence and right-associative '**', which an interpreter evaluates over
// a variable environment (assignment persists across calls). Use to safely evaluate
// integer/float expressions without host eval(). Guarantees (self-test): 10 precedence
// cases exact (2**3**2=512), variables persist, 100 random exprs match a reference
// evaluator, and division/modulo-by-zero, bad syntax, and unknown vars are refused.
// Token represents a single token.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Token struct {
	Type     string
	Value    interface{}
	Position int
}

// Lexer turns text into tokens.
type Lexer struct {
	text        string
	pos         int
	currentChar byte
	hasChar     bool
}

func newLexer(text string) *Lexer {
	l := &Lexer{text: text}
	if len(text) > 0 {
		l.currentChar = text[0]
		l.hasChar = true
	}
	return l
}

func (l *Lexer) advance() {
	l.pos++
	if l.pos >= len(l.text) {
		l.hasChar = false
	} else {
		l.currentChar = l.text[l.pos]
	}
}

func (l *Lexer) skipWhitespace() {
	for l.hasChar && (l.currentChar == ' ' || l.currentChar == '\t' || l.currentChar == '\n' || l.currentChar == '\r') {
		l.advance()
	}
}

func (l *Lexer) readNumber() (interface{}, error) {
	start := l.pos
	for l.hasChar && ((l.currentChar >= '0' && l.currentChar <= '9') || l.currentChar == '.') {
		l.advance()
	}
	result := l.text[start:l.pos]
	if strings.Contains(result, ".") {
		v, err := strconv.ParseFloat(result, 64)
		if err != nil {
			return nil, fmt.Errorf("invalid number %q at position %d", result, l.pos)
		}
		return v, nil
	}
	v, err := strconv.Atoi(result)
	if err != nil {
		return nil, fmt.Errorf("invalid integer %q at position %d", result, l.pos)
	}
	return v, nil
}

func (l *Lexer) readIdentifier() string {
	start := l.pos
	for l.hasChar && ((l.currentChar >= 'a' && l.currentChar <= 'z') || (l.currentChar >= 'A' && l.currentChar <= 'Z') || (l.currentChar >= '0' && l.currentChar <= '9') || l.currentChar == '_') {
		l.advance()
	}
	return l.text[start:l.pos]
}

func (l *Lexer) getNextToken() (Token, error) {
	for l.hasChar {
		if l.currentChar == ' ' || l.currentChar == '\t' || l.currentChar == '\n' || l.currentChar == '\r' {
			l.skipWhitespace()
			continue
		}
		if l.currentChar >= '0' && l.currentChar <= '9' {
			v, err := l.readNumber()
			if err != nil {
				return Token{}, err
			}
			return Token{"NUMBER", v, l.pos}, nil
		}
		if (l.currentChar >= 'a' && l.currentChar <= 'z') || (l.currentChar >= 'A' && l.currentChar <= 'Z') || l.currentChar == '_' {
			identifier := l.readIdentifier()
			if identifier == "true" {
				return Token{"BOOLEAN", true, l.pos}, nil
			}
			if identifier == "false" {
				return Token{"BOOLEAN", false, l.pos}, nil
			}
			return Token{"IDENTIFIER", identifier, l.pos}, nil
		}
		pos := l.pos
		switch l.currentChar {
		case '+':
			l.advance()
			return Token{"PLUS", "+", pos}, nil
		case '-':
			l.advance()
			return Token{"MINUS", "-", pos}, nil
		case '*':
			l.advance()
			if l.hasChar && l.currentChar == '*' {
				l.advance()
				return Token{"POWER", "**", pos}, nil
			}
			return Token{"MULTIPLY", "*", pos}, nil
		case '/':
			l.advance()
			return Token{"DIVIDE", "/", pos}, nil
		case '%':
			l.advance()
			return Token{"MODULO", "%", pos}, nil
		case '(':
			l.advance()
			return Token{"LPAREN", "(", pos}, nil
		case ')':
			l.advance()
			return Token{"RPAREN", ")", pos}, nil
		case '=':
			l.advance()
			return Token{"ASSIGN", "=", pos}, nil
		default:
			return Token{}, fmt.Errorf("invalid character '%c' at position %d", l.currentChar, l.pos)
		}
	}
	return Token{"EOF", nil, l.pos}, nil
}

// AST node interface.
type AST interface {
	astNode()
}

type Number struct{ Value interface{} }
type Boolean struct{ Value bool }
type Variable struct{ Name string }
type BinOp struct {
	Left, Right AST
	Op          Token
}
type Assign struct {
	Left  *Variable
	Right AST
	Op    Token
}
type UnaryOp struct {
	Expr AST
	Op   Token
}

func (Number) astNode()   {}
func (Boolean) astNode()  {}
func (Variable) astNode() {}
func (BinOp) astNode()    {}
func (Assign) astNode()   {}
func (UnaryOp) astNode()  {}

// Parser builds an AST from tokens.
type Parser struct {
	lexer        *Lexer
	currentToken Token
}

func newParser(lexer *Lexer) (*Parser, error) {
	t, err := lexer.getNextToken()
	if err != nil {
		return nil, err
	}
	return &Parser{lexer: lexer, currentToken: t}, nil
}

func (p *Parser) eat(tokenType string) error {
	if p.currentToken.Type == tokenType {
		t, err := p.lexer.getNextToken()
		if err != nil {
			return err
		}
		p.currentToken = t
		return nil
	}
	return fmt.Errorf("expected %s, got %s at position %d", tokenType, p.currentToken.Type, p.currentToken.Position)
}

func (p *Parser) factor() (AST, error) {
	token := p.currentToken
	switch token.Type {
	case "PLUS":
		if err := p.eat("PLUS"); err != nil {
			return nil, err
		}
		e, err := p.factor()
		if err != nil {
			return nil, err
		}
		return &UnaryOp{Op: token, Expr: e}, nil
	case "MINUS":
		if err := p.eat("MINUS"); err != nil {
			return nil, err
		}
		e, err := p.factor()
		if err != nil {
			return nil, err
		}
		return &UnaryOp{Op: token, Expr: e}, nil
	case "NUMBER":
		if err := p.eat("NUMBER"); err != nil {
			return nil, err
		}
		return &Number{Value: token.Value}, nil
	case "BOOLEAN":
		if err := p.eat("BOOLEAN"); err != nil {
			return nil, err
		}
		return &Boolean{Value: token.Value.(bool)}, nil
	case "IDENTIFIER":
		if err := p.eat("IDENTIFIER"); err != nil {
			return nil, err
		}
		return &Variable{Name: token.Value.(string)}, nil
	case "LPAREN":
		if err := p.eat("LPAREN"); err != nil {
			return nil, err
		}
		node, err := p.expr()
		if err != nil {
			return nil, err
		}
		if err := p.eat("RPAREN"); err != nil {
			return nil, err
		}
		return node, nil
	default:
		return nil, fmt.Errorf("unexpected token %s at position %d", token.Type, token.Position)
	}
}

func (p *Parser) power() (AST, error) {
	node, err := p.factor()
	if err != nil {
		return nil, err
	}
	if p.currentToken.Type == "POWER" {
		token := p.currentToken
		if err := p.eat("POWER"); err != nil {
			return nil, err
		}
		right, err := p.power()
		if err != nil {
			return nil, err
		}
		node = &BinOp{Left: node, Op: token, Right: right}
	}
	return node, nil
}

func (p *Parser) term() (AST, error) {
	node, err := p.power()
	if err != nil {
		return nil, err
	}
	for p.currentToken.Type == "MULTIPLY" || p.currentToken.Type == "DIVIDE" || p.currentToken.Type == "MODULO" {
		token := p.currentToken
		if err := p.eat(token.Type); err != nil {
			return nil, err
		}
		right, err := p.power()
		if err != nil {
			return nil, err
		}
		node = &BinOp{Left: node, Op: token, Right: right}
	}
	return node, nil
}

func (p *Parser) expr() (AST, error) {
	node, err := p.term()
	if err != nil {
		return nil, err
	}
	for p.currentToken.Type == "PLUS" || p.currentToken.Type == "MINUS" {
		token := p.currentToken
		if err := p.eat(token.Type); err != nil {
			return nil, err
		}
		right, err := p.term()
		if err != nil {
			return nil, err
		}
		node = &BinOp{Left: node, Op: token, Right: right}
	}
	if p.currentToken.Type == "ASSIGN" {
		variable, ok := node.(*Variable)
		if !ok {
			return nil, fmt.Errorf("left side of assignment must be a variable at position %d", p.currentToken.Position)
		}
		token := p.currentToken
		if err := p.eat("ASSIGN"); err != nil {
			return nil, err
		}
		right, err := p.expr()
		if err != nil {
			return nil, err
		}
		node = &Assign{Left: variable, Op: token, Right: right}
	}
	return node, nil
}

func (p *Parser) parse() (AST, error) {
	return p.expr()
}

// Environment stores variable values.
type Environment struct {
	variables map[string]interface{}
}

func newEnvironment() *Environment {
	return &Environment{variables: map[string]interface{}{}}
}

func (e *Environment) get(name string) (interface{}, error) {
	value, ok := e.variables[name]
	if !ok {
		return nil, fmt.Errorf("variable '%s' is not defined", name)
	}
	return value, nil
}

func (e *Environment) set(name string, value interface{}) {
	e.variables[name] = value
}

// ExpressionEvaluator evaluates expressions.
type ExpressionEvaluator struct {
	environment *Environment
}

func newExpressionEvaluator(environment *Environment) *ExpressionEvaluator {
	return &ExpressionEvaluator{environment: environment}
}

func (ev *ExpressionEvaluator) visit(node AST) (interface{}, error) {
	switch n := node.(type) {
	case *Number:
		return n.Value, nil
	case *Boolean:
		return n.Value, nil
	case *Variable:
		return ev.environment.get(n.Name)
	case *BinOp:
		leftVal, err := ev.visit(n.Left)
		if err != nil {
			return nil, err
		}
		rightVal, err := ev.visit(n.Right)
		if err != nil {
			return nil, err
		}
		return ev.applyBinOp(n.Op.Type, leftVal, rightVal)
	case *UnaryOp:
		operand, err := ev.visit(n.Expr)
		if err != nil {
			return nil, err
		}
		return ev.applyUnaryOp(n.Op.Type, operand)
	case *Assign:
		value, err := ev.visit(n.Right)
		if err != nil {
			return nil, err
		}
		ev.environment.set(n.Left.Name, value)
		return value, nil
	default:
		return nil, fmt.Errorf("no visit method for node")
	}
}

func toFloat(v interface{}) float64 {
	switch x := v.(type) {
	case int:
		return float64(x)
	case float64:
		return x
	case bool:
		if x {
			return 1.0
		}
		return 0.0
	}
	return 0.0
}

func isInt(v interface{}) bool {
	_, ok := v.(int)
	return ok
}

func (ev *ExpressionEvaluator) applyBinOp(op string, leftVal, rightVal interface{}) (interface{}, error) {
	leftIsInt := isInt(leftVal)
	rightIsInt := isInt(rightVal)
	if op == "PLUS" {
		if leftIsInt && rightIsInt {
			return leftVal.(int) + rightVal.(int), nil
		}
		return toFloat(leftVal) + toFloat(rightVal), nil
	}
	if op == "MINUS" {
		if leftIsInt && rightIsInt {
			return leftVal.(int) - rightVal.(int), nil
		}
		return toFloat(leftVal) - toFloat(rightVal), nil
	}
	if op == "MULTIPLY" {
		if leftIsInt && rightIsInt {
			return leftVal.(int) * rightVal.(int), nil
		}
		return toFloat(leftVal) * toFloat(rightVal), nil
	}
	if op == "DIVIDE" {
		right := toFloat(rightVal)
		if math.Abs(right) < 1e-15 {
			return nil, fmt.Errorf("division by zero")
		}
		return toFloat(leftVal) / right, nil
	}
	if op == "MODULO" {
		if rightIsInt && leftIsInt {
			right := rightVal.(int)
			if right == 0 {
				return nil, fmt.Errorf("modulo by zero")
			}
			return leftVal.(int) % right, nil
		}
		return nil, fmt.Errorf("modulo not supported for non-integer")
	}
	if op == "POWER" {
		left := toFloat(leftVal)
		right := toFloat(rightVal)
		result := math.Pow(left, right)
		if leftIsInt && rightIsInt && result == float64(int(result)) {
			return int(result), nil
		}
		return result, nil
	}
	return nil, fmt.Errorf("unknown operator: %s", op)
}

func (ev *ExpressionEvaluator) applyUnaryOp(op string, operand interface{}) (interface{}, error) {
	if op == "PLUS" {
		return operand, nil
	}
	if op == "MINUS" {
		if v, ok := operand.(int); ok {
			return -v, nil
		}
		return -toFloat(operand), nil
	}
	return nil, fmt.Errorf("unknown unary operator: %s", op)
}

func (ev *ExpressionEvaluator) evaluate(expression string) (interface{}, error) {
	lexer := newLexer(expression)
	parser, err := newParser(lexer)
	if err != nil {
		return nil, fmt.Errorf("error evaluating expression %q: %v", expression, err)
	}
	tree, err := parser.parse()
	if err != nil {
		return nil, fmt.Errorf("error evaluating expression %q: %v", expression, err)
	}
	v, err := ev.visit(tree)
	if err != nil {
		return nil, fmt.Errorf("error evaluating expression %q: %v", expression, err)
	}
	return v, nil
}

func pythonEval(expr string) float64 {
	// eval simple integer expressions with + - * only, left-to-right with precedence not needed because terms are 1-9 and ops chosen.
	// Actually terms are 4 single-digit numbers with 3 ops; precedence matters for *.
	// We use a tiny shunting-yard evaluator.
	var values []float64
	var ops []rune
	pushVal := func(v float64) { values = append(values, v) }
	pushOp := func(o rune) { ops = append(ops, o) }
	applyOp := func(o rune) {
		n := len(values)
		a, b := values[n-2], values[n-1]
		values = values[:n-1]
		switch o {
		case '+':
			values[n-2] = a + b
		case '-':
			values[n-2] = a - b
		case '*':
			values[n-2] = a * b
		}
	}
	precedence := func(o rune) int {
		if o == '*' {
			return 2
		}
		return 1
	}
	for _, ch := range expr {
		switch ch {
		case ' ':
			continue
		case '+', '-', '*':
			for len(ops) > 0 && precedence(ops[len(ops)-1]) >= precedence(ch) {
				applyOp(ops[len(ops)-1])
				ops = ops[:len(ops)-1]
			}
			pushOp(ch)
		default:
			pushVal(float64(int(ch - '0')))
		}
	}
	for len(ops) > 0 {
		applyOp(ops[len(ops)-1])
		ops = ops[:len(ops)-1]
	}
	return values[0]
}

func main() {
	ev := newExpressionEvaluator(newEnvironment())

	cases := []struct {
		expr     string
		expected interface{}
	}{
		{"2 + 3 * 4", 14},
		{"(2 + 3) * 4", 20},
		{"10 / 2 - 3", 2.0},
		{"2 ** 3", 8},
		{"17 % 5", 2},
		{"2 + 3 * 4 - 10 / 2", 9.0},
		{"-5 + 3", -2},
		{"+10 - 2", 8},
		{"2 ** 3 ** 2", 512},
		{"100 - 10 - 20", 70},
	}

	for _, c := range cases {
		got, err := ev.evaluate(c.expr)
		if err != nil {
			fmt.Fprintf(os.Stderr, "error evaluating %q: %v\n", c.expr, err)
			os.Exit(1)
		}
		if !(got == c.expected) {
			fmt.Fprintf(os.Stderr, "%q must be %v (%T), got %v (%T)\n", c.expr, c.expected, c.expected, got, got)
			os.Exit(1)
		}
		if fmt.Sprintf("%T", got) != fmt.Sprintf("%T", c.expected) {
			fmt.Fprintf(os.Stderr, "%q: type %T != %T\n", c.expr, got, c.expected)
			os.Exit(1)
		}
	}

	// Explicit 2**3 == 8 recovery site preserves the literal 8 from the oracle.
	got8, err := ev.evaluate("2 ** 3")
	if err != nil || !(got8 == 8) {
		fmt.Fprintf(os.Stderr, "2 ** 3 must be 8, got %v err %v\n", got8, err)
		os.Exit(1)
	}

	got, err := ev.evaluate("x = 10")
	if err != nil || !(got == 10) {
		fmt.Fprintf(os.Stderr, "x = 10 must be 10, got %v err %v\n", got, err)
		os.Exit(1)
	}
	got, err = ev.evaluate("y = 5")
	if err != nil || !(got == 5) {
		fmt.Fprintf(os.Stderr, "y = 5 must be 5, got %v err %v\n", got, err)
		os.Exit(1)
	}
	v15, err := ev.evaluate("x + y")
	if err != nil || !(v15 == 15) {
		fmt.Fprintf(os.Stderr, "x + y mismatch\n")
		os.Exit(1)
	}
	v50, err := ev.evaluate("z = x * y")
	if err != nil || !(v50 == 50) {
		fmt.Fprintf(os.Stderr, "z = x * y mismatch\n")
		os.Exit(1)
	}
	vZ, err := ev.evaluate("z")
	if err != nil || !(vZ == 50) {
		fmt.Fprintf(os.Stderr, "z mismatch\n")
		os.Exit(1)
	}
	got, err = ev.evaluate("x = -7")
	if err != nil || !(got == -7) {
		fmt.Fprintf(os.Stderr, "x = -7 mismatch\n")
		os.Exit(1)
	}
	vNeg2, err := ev.evaluate("x + y")
	if err != nil || !(vNeg2 == -2) {
		fmt.Fprintf(os.Stderr, "reassignment did not take effect\n")
		os.Exit(1)
	}
	va, err := ev.evaluate("a = 2.5")
	if err != nil || !(math.Abs(toFloat(va)-2.5) < 1e-12) {
		fmt.Fprintf(os.Stderr, "a = 2.5 tolerance mismatch\n")
		os.Exit(1)
	}
	v8, err := ev.evaluate("(a + 1.5) * 2")
	if err != nil || !(math.Abs(toFloat(v8)-8.0) < 1e-12) {
		fmt.Fprintf(os.Stderr, "(a + 1.5) * 2 tolerance mismatch\n")
		os.Exit(1)
	}
	if !(ev.environment.variables["z"] == 50) {
		fmt.Fprintf(os.Stderr, "environment z mismatch\n")
		os.Exit(1)
	}

	rand.Seed(42)
	for i := 0; i < 100; i++ {
		terms := make([]string, 4)
		for j := range terms {
			terms[j] = strconv.Itoa(rand.Intn(9) + 1)
		}
		ops := []string{"+", "-", "*"}
		chosen := make([]string, 3)
		for j := range chosen {
			chosen[j] = ops[rand.Intn(len(ops))]
		}
		expr := terms[0]
		for j, op := range chosen {
			expr += op + terms[j+1]
		}
		got, err := ev.evaluate(expr)
		if err != nil {
			fmt.Fprintf(os.Stderr, "error evaluating %q: %v\n", expr, err)
			os.Exit(1)
		}
		want := pythonEval(expr)
		if toFloat(got) != want {
			fmt.Fprintf(os.Stderr, "%q diverged from python: got %v want %v\n", expr, got, want)
			os.Exit(1)
		}
	}

	// Refusals: division/modulo by zero, garbage syntax, unknown variable.
	badCases := []string{"1 / 0", "5 % 0", "2 +", "(1 + 2", "unknown_var + 1"}
	for _, bad := range badCases {
		_, err := ev.evaluate(bad)
		if err == nil {
			fmt.Fprintf(os.Stderr, "%q evaluated without error\n", bad)
			os.Exit(1)
		}
	}

	fmt.Println("expression_evaluator: 10 precedence cases exact (2**3**2=512), variables persist, 100 fuzz == python eval, 5 refusals -- PASS")
}
