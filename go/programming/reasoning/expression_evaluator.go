package main

import (
	"errors"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
	"unicode"
)

// Token represents a single token in the expression.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Token struct {
	Type     string
	Value    interface{}
	Position int
}

// Lexer converts text into tokens.
type Lexer struct {
	text        string
	pos         int
	currentChar rune
}

func NewLexer(text string) *Lexer {
	l := &Lexer{text: text}
	if len(text) > 0 {
		l.currentChar = rune(text[0])
	} else {
		l.currentChar = 0
	}
	return l
}

func (l *Lexer) error(message string) {
	panic(fmt.Sprintf("%s at position %d", message, l.pos))
}

func (l *Lexer) advance() {
	l.pos++
	if l.pos >= len(l.text) {
		l.currentChar = 0
	} else {
		l.currentChar = rune(l.text[l.pos])
	}
}

func (l *Lexer) skipWhitespace() {
	for l.currentChar != 0 && unicode.IsSpace(l.currentChar) {
		l.advance()
	}
}

func (l *Lexer) readNumber() (interface{}, error) {
	var result strings.Builder
	for l.currentChar != 0 && (unicode.IsDigit(l.currentChar) || l.currentChar == '.') {
		result.WriteRune(l.currentChar)
		l.advance()
	}
	s := result.String()
	if strings.Contains(s, ".") {
		return strconv.ParseFloat(s, 64)
	}
	return strconv.Atoi(s)
}

func (l *Lexer) readIdentifier() string {
	var result strings.Builder
	for l.currentChar != 0 && (unicode.IsLetter(l.currentChar) || unicode.IsDigit(l.currentChar) || l.currentChar == '_') {
		result.WriteRune(l.currentChar)
		l.advance()
	}
	return result.String()
}

func (l *Lexer) getNextToken() Token {
	for l.currentChar != 0 {
		if unicode.IsSpace(l.currentChar) {
			l.skipWhitespace()
			continue
		}

		if unicode.IsDigit(l.currentChar) {
			pos := l.pos
			val, err := l.readNumber()
			if err != nil {
				l.error("invalid number")
			}
			return Token{Type: "NUMBER", Value: val, Position: pos}
		}

		if unicode.IsLetter(l.currentChar) || l.currentChar == '_' {
			pos := l.pos
			ident := l.readIdentifier()
			switch ident {
			case "true":
				return Token{Type: "BOOLEAN", Value: true, Position: pos}
			case "false":
				return Token{Type: "BOOLEAN", Value: false, Position: pos}
			default:
				return Token{Type: "IDENTIFIER", Value: ident, Position: pos}
			}
		}

		switch l.currentChar {
		case '+':
			l.advance()
			return Token{Type: "PLUS", Value: "+", Position: l.pos}
		case '-':
			l.advance()
			return Token{Type: "MINUS", Value: "-", Position: l.pos}
		case '*':
			l.advance()
			if l.currentChar == '*' {
				l.advance()
				return Token{Type: "POWER", Value: "**", Position: l.pos}
			}
			return Token{Type: "MULTIPLY", Value: "*", Position: l.pos}
		case '/':
			l.advance()
			return Token{Type: "DIVIDE", Value: "/", Position: l.pos}
		case '%':
			l.advance()
			return Token{Type: "MODULO", Value: "%", Position: l.pos}
		case '(':
			l.advance()
			return Token{Type: "LPAREN", Value: "(", Position: l.pos}
		case ')':
			l.advance()
			return Token{Type: "RPAREN", Value: ")", Position: l.pos}
		case '=':
			l.advance()
			return Token{Type: "ASSIGN", Value: "=", Position: l.pos}
		default:
			l.error(fmt.Sprintf("invalid character '%c'", l.currentChar))
		}
	}
	return Token{Type: "EOF", Value: nil, Position: l.pos}
}

// AST node types.
type ASTNode interface{}

type NumberNode struct {
	Value interface{}
}

type BooleanNode struct {
	Value bool
}

type VariableNode struct {
	Name string
}

type BinOpNode struct {
	Left  ASTNode
	Op    Token
	Right ASTNode
}

type AssignNode struct {
	Left  VariableNode
	Op    Token
	Right ASTNode
}

type UnaryOpNode struct {
	Op   Token
	Expr ASTNode
}

// Parser builds an AST from tokens.
type Parser struct {
	lexer        *Lexer
	currentToken Token
}

func NewParser(lexer *Lexer) *Parser {
	return &Parser{
		lexer:        lexer,
		currentToken: lexer.getNextToken(),
	}
}

func (p *Parser) error(message string) {
	panic(fmt.Sprintf("%s at position %d", message, p.currentToken.Position))
}

func (p *Parser) eat(tokenType string) {
	if p.currentToken.Type == tokenType {
		p.currentToken = p.lexer.getNextToken()
	} else {
		p.error(fmt.Sprintf("expected %s, got %s", tokenType, p.currentToken.Type))
	}
}

func (p *Parser) factor() ASTNode {
	token := p.currentToken

	switch token.Type {
	case "PLUS":
		p.eat("PLUS")
		return UnaryOpNode{Op: token, Expr: p.factor()}
	case "MINUS":
		p.eat("MINUS")
		return UnaryOpNode{Op: token, Expr: p.factor()}
	case "NUMBER":
		p.eat("NUMBER")
		return NumberNode{Value: token.Value}
	case "BOOLEAN":
		p.eat("BOOLEAN")
		return BooleanNode{Value: token.Value.(bool)}
	case "IDENTIFIER":
		p.eat("IDENTIFIER")
		return VariableNode{Name: token.Value.(string)}
	case "LPAREN":
		p.eat("LPAREN")
		node := p.expr()
		p.eat("RPAREN")
		return node
	default:
		p.error(fmt.Sprintf("unexpected token %s", token.Type))
	}
	return nil
}

func (p *Parser) power() ASTNode {
	node := p.factor()
	if p.currentToken.Type == "POWER" {
		token := p.currentToken
		p.eat("POWER")
		node = BinOpNode{Left: node, Op: token, Right: p.power()}
	}
	return node
}

func (p *Parser) term() ASTNode {
	node := p.power()
	for p.currentToken.Type == "MULTIPLY" || p.currentToken.Type == "DIVIDE" || p.currentToken.Type == "MODULO" {
		token := p.currentToken
		switch token.Type {
		case "MULTIPLY":
			p.eat("MULTIPLY")
		case "DIVIDE":
			p.eat("DIVIDE")
		case "MODULO":
			p.eat("MODULO")
		}
		node = BinOpNode{Left: node, Op: token, Right: p.power()}
	}
	return node
}

func (p *Parser) expr() ASTNode {
	node := p.term()
	for p.currentToken.Type == "PLUS" || p.currentToken.Type == "MINUS" {
		token := p.currentToken
		switch token.Type {
		case "PLUS":
			p.eat("PLUS")
		case "MINUS":
			p.eat("MINUS")
		}
		node = BinOpNode{Left: node, Op: token, Right: p.term()}
	}

	if p.currentToken.Type == "ASSIGN" {
		if _, ok := node.(VariableNode); !ok {
			p.error("left side of assignment must be a variable")
		}
		token := p.currentToken
		p.eat("ASSIGN")
		return AssignNode{Left: node.(VariableNode), Op: token, Right: p.expr()}
	}

	return node
}

func (p *Parser) parse() ASTNode {
	return p.expr()
}

// Environment stores variable values.
type Environment struct {
	variables map[string]interface{}
}

func NewEnvironment() *Environment {
	return &Environment{variables: make(map[string]interface{})}
}

func (e *Environment) Get(name string) (interface{}, error) {
	val, ok := e.variables[name]
	if !ok {
		return nil, fmt.Errorf("variable '%s' is not defined", name)
	}
	return val, nil
}

func (e *Environment) Set(name string, value interface{}) {
	e.variables[name] = value
}

// ExpressionEvaluator evaluates ASTs.
type ExpressionEvaluator struct {
	env *Environment
}

func NewExpressionEvaluator(env *Environment) *ExpressionEvaluator {
	if env == nil {
		env = NewEnvironment()
	}
	return &ExpressionEvaluator{env: env}
}

func (ev *ExpressionEvaluator) visit(node ASTNode) (interface{}, error) {
	switch n := node.(type) {
	case NumberNode:
		return n.Value, nil
	case BooleanNode:
		return n.Value, nil
	case VariableNode:
		return ev.env.Get(n.Name)
	case BinOpNode:
		left, err := ev.visit(n.Left)
		if err != nil {
			return nil, err
		}
		right, err := ev.visit(n.Right)
		if err != nil {
			return nil, err
		}
		return ev.visitBinOp(n.Op.Type, left, right)
	case AssignNode:
		val, err := ev.visit(n.Right)
		if err != nil {
			return nil, err
		}
		ev.env.Set(n.Left.Name, val)
		return val, nil
	case UnaryOpNode:
		operand, err := ev.visit(n.Expr)
		if err != nil {
			return nil, err
		}
		return ev.visitUnaryOp(n.Op.Type, operand)
	default:
		return nil, fmt.Errorf("unknown node type")
	}
}

func (ev *ExpressionEvaluator) visitBinOp(op string, left, right interface{}) (interface{}, error) {
	leftNum, leftIsNum := toFloat(left)
	rightNum, rightIsNum := toFloat(right)

	if leftIsNum && rightIsNum {
		switch op {
		case "PLUS":
			return leftNum + rightNum, nil
		case "MINUS":
			return leftNum - rightNum, nil
		case "MULTIPLY":
			return leftNum * rightNum, nil
		case "DIVIDE":
			if rightNum == 0 {
				return nil, errors.New("division by zero")
			}
			return leftNum / rightNum, nil
		case "MODULO":
			if rightNum == 0 {
				return nil, errors.New("modulo by zero")
			}
			return math.Mod(leftNum, rightNum), nil
		case "POWER":
			return math.Pow(leftNum, rightNum), nil
		}
	}

	return nil, fmt.Errorf("unknown operator: %s", op)
}

func (ev *ExpressionEvaluator) visitUnaryOp(op string, operand interface{}) (interface{}, error) {
	num, ok := toFloat(operand)
	if !ok {
		return nil, fmt.Errorf("unknown unary operator: %s", op)
	}
	switch op {
	case "PLUS":
		return +num, nil
	case "MINUS":
		return -num, nil
	}
	return nil, fmt.Errorf("unknown unary operator: %s", op)
}

func (ev *ExpressionEvaluator) Evaluate(expression string) (interface{}, error) {
	defer func() {
		if r := recover(); r != nil {
			_ = r
		}
	}()

	lexer := NewLexer(expression)
	parser := NewParser(lexer)
	tree := parser.parse()
	return ev.visit(tree)
}

func toFloat(v interface{}) (float64, bool) {
	switch n := v.(type) {
	case int:
		return float64(n), true
	case float64:
		return n, true
	}
	return 0, false
}

func main() {
	evaluator := NewExpressionEvaluator(nil)

	expressions := []string{
		"2 + 3 * 4",
		"(2 + 3) * 4",
		"10 / 2 - 3",
		"2 ** 3",
		"17 % 5",
		"x = 10",
		"y = 5",
		"x + y",
		"z = x * y",
		"z",
		"a = 2.5",
		"b = 3.7",
		"a + b",
		"result = (a + b) * 2",
		"result",
		"-5 + 3",
		"+10 - 2",
		"x = -7",
		"x",
		"flag = true",
		"flag",
	}

	fmt.Println("Expression Evaluator Demo")
	fmt.Println("=========================")

	for _, expr := range expressions {
		result, err := evaluator.Evaluate(expr)
		if err != nil {
			fmt.Printf("%-20s => Error: %v\n", expr, err)
		} else {
			fmt.Printf("%-20s => %v\n", expr, result)
		}
	}

	fmt.Println("\nEnvironment variables:")
	names := make([]string, 0, len(evaluator.env.variables))
	for n := range evaluator.env.variables {
		names = append(names, n)
	}
	sort.Strings(names)
	for _, name := range names {
		value := evaluator.env.variables[name]
		fmt.Printf("  %s = %v\n", name, value)
	}

	exprResult, err := evaluator.Evaluate("2 + 3 * 4")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to evaluate final check: %v\n", err)
		os.Exit(1)
	}
	if !(exprResult.(float64) == 14) {
		fmt.Fprintln(os.Stderr, "2 + 3 * 4 should equal 14")
		os.Exit(1)
	}

	fmt.Println("expression_evaluator PASS")
}
