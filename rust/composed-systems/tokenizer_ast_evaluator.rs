#![forbid(unsafe_code)]
// composes: tokenize-arithmetic + parse-to-ast-with-precedence + evaluate

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#[derive(Clone, Debug, PartialEq)]
enum Token {
    Num(i32),
    Plus,
    Minus,
    Mult,
    Div,
    LParen,
    RParen,
}

#[derive(Clone, Debug)]
enum Expr {
    Num(i32),
    BinOp(Box<Expr>, Token, Box<Expr>),
}

fn tokenize(s: &str) -> Vec<Token> {
    let mut tokens = Vec::new();
    let mut i = 0;
    let bytes = s.as_bytes();
    while i < bytes.len() {
        match bytes[i] {
            b' ' => { i += 1; }
            b'(' => { tokens.push(Token::LParen); i += 1; }
            b')' => { tokens.push(Token::RParen); i += 1; }
            b'+' => { tokens.push(Token::Plus); i += 1; }
            b'-' => { tokens.push(Token::Minus); i += 1; }
            b'*' => { tokens.push(Token::Mult); i += 1; }
            b'/' => { tokens.push(Token::Div); i += 1; }
            b'0'..=b'9' => {
                let mut num = 0;
                while i < bytes.len() && bytes[i].is_ascii_digit() {
                    num = num * 10 + (bytes[i] - b'0') as i32;
                    i += 1;
                }
                tokens.push(Token::Num(num));
            }
            _ => { i += 1; }
        }
    }
    tokens
}

fn parse_expr(tokens: &[Token], pos: &mut usize) -> Option<Expr> {
    parse_add_sub(tokens, pos)
}

fn parse_add_sub(tokens: &[Token], pos: &mut usize) -> Option<Expr> {
    let mut left = parse_mul_div(tokens, pos)?;
    while *pos < tokens.len() {
        match &tokens[*pos] {
            Token::Plus | Token::Minus => {
                let op = tokens[*pos].clone();
                *pos += 1;
                let right = parse_mul_div(tokens, pos)?;
                left = Expr::BinOp(Box::new(left), op, Box::new(right));
            }
            _ => break,
        }
    }
    Some(left)
}

fn parse_mul_div(tokens: &[Token], pos: &mut usize) -> Option<Expr> {
    let mut left = parse_primary(tokens, pos)?;
    while *pos < tokens.len() {
        match &tokens[*pos] {
            Token::Mult | Token::Div => {
                let op = tokens[*pos].clone();
                *pos += 1;
                let right = parse_primary(tokens, pos)?;
                left = Expr::BinOp(Box::new(left), op, Box::new(right));
            }
            _ => break,
        }
    }
    Some(left)
}

fn parse_primary(tokens: &[Token], pos: &mut usize) -> Option<Expr> {
    if *pos >= tokens.len() { return None; }
    match &tokens[*pos] {
        Token::Num(n) => {
            let n = *n;
            *pos += 1;
            Some(Expr::Num(n))
        }
        Token::LParen => {
            *pos += 1;
            let expr = parse_expr(tokens, pos)?;
            if *pos < tokens.len() && tokens[*pos] == Token::RParen {
                *pos += 1;
                Some(expr)
            } else {
                None
            }
        }
        _ => None,
    }
}

fn eval(expr: &Expr) -> i32 {
    match expr {
        Expr::Num(n) => *n,
        Expr::BinOp(left, op, right) => {
            let lv = eval(left);
            let rv = eval(right);
            match op {
                Token::Plus => lv + rv,
                Token::Minus => lv - rv,
                Token::Mult => lv * rv,
                Token::Div => lv / rv,
                _ => 0,
            }
        }
    }
}

fn main() {
    // Stage 1: Tokenize
    let expr_str = "2 + 3 * 4";
    let tokens = tokenize(expr_str);
    // tokens: [Num(2), Plus, Num(3), Mult, Num(4)]

    // Stage 2: Parse with precedence (mult binds tighter than plus)
    let mut pos = 0;
    let ast = parse_expr(&tokens, &mut pos).expect("parse failed");

    // Stage 3: Evaluate
    let result = eval(&ast);
    // Expected: 2 + (3 * 4) = 2 + 12 = 14
    // Wrong (no precedence): (2 + 3) * 4 = 5 * 4 = 20

    assert_eq!(result, 14, "Correct precedence: 2 + 3*4 = 14");

    // Corruption test: what if we evaluated left-to-right without precedence?
    // We'd get 20, which our assertion catches
    println!("tokenizer_ast_evaluator: PASS");
}
