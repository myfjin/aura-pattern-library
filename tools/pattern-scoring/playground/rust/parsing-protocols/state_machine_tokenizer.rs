#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// A single-pass character-class tokenizer that scans source text into a Token stream:
// runs of digits become Number, an alpha/underscore start followed by alnum/underscore
// becomes Ident, listed operator and punctuation chars become Op(char), each whitespace
// char becomes one Space, and anything else becomes an Error token (it does not abort).
// Use as a lexer skeleton for a simple expression or config grammar.
// Guarantees maximal-munch boundaries: adjacent classes do not merge ("123abc" splits into
// Number then Ident), and the emitted stream is exactly determined including Space tokens.
#[derive(Debug, PartialEq, Clone)]
enum Token {
    Number(String),
    Ident(String),
    Op(char),
    Space,
    Error(String),
}

struct Tokenizer;

impl Tokenizer {
    fn tokenize(input: &str) -> Vec<Token> {
        let mut tokens = Vec::new();
        let bytes = input.as_bytes();
        let mut i = 0;

        while i < bytes.len() {
            let ch = bytes[i] as char;

            if ch.is_whitespace() {
                tokens.push(Token::Space);
                i += 1;
            } else if ch.is_ascii_digit() {
                let start = i;
                while i < bytes.len() && (bytes[i] as char).is_ascii_digit() {
                    i += 1;
                }
                tokens.push(Token::Number(
                    input[start..i].to_string(),
                ));
            } else if ch.is_ascii_alphabetic() || ch == '_' {
                let start = i;
                while i < bytes.len() {
                    let c = bytes[i] as char;
                    if c.is_ascii_alphanumeric() || c == '_' {
                        i += 1;
                    } else {
                        break;
                    }
                }
                tokens.push(Token::Ident(
                    input[start..i].to_string(),
                ));
            } else if "+-*/%=<>!&|^".contains(ch) {
                tokens.push(Token::Op(ch));
                i += 1;
            } else if ch == '(' || ch == ')' || ch == '{' || ch == '}' || ch == '[' || ch == ']' || ch == ',' || ch == ';' || ch == ':' {
                tokens.push(Token::Op(ch));
                i += 1;
            } else {
                let bad_ch = ch.to_string();
                tokens.push(Token::Error(format!("illegal char '{}'", bad_ch)));
                i += 1;
            }
        }

        tokens
    }
}

fn main() {
    // Ground truth test: the FULL token stream is exactly determined (Space tokens included).
    let input1 = "fn main() { let x = 42; }";
    let tokens = Tokenizer::tokenize(input1);
    let expected1 = vec![
        Token::Ident("fn".to_string()),
        Token::Space,
        Token::Ident("main".to_string()),
        Token::Op('('),
        Token::Op(')'),
        Token::Space,
        Token::Op('{'),
        Token::Space,
        Token::Ident("let".to_string()),
        Token::Space,
        Token::Ident("x".to_string()),
        Token::Space,
        Token::Op('='),
        Token::Space,
        Token::Number("42".to_string()),
        Token::Op(';'),
        Token::Space,
        Token::Op('}'),
    ];
    assert_eq!(tokens, expected1, "token stream mismatch");

    // Ground truth test: number parsing
    let input2 = "let x123 = 9876 + 1;";
    let tokens2 = Tokenizer::tokenize(input2);
    let nums: Vec<_> = tokens2.iter()
        .filter_map(|t| match t {
            Token::Number(n) => Some(n.clone()),
            _ => None,
        })
        .collect();
    assert_eq!(nums, vec!["9876", "1"]);

    // Adversarial test: input with illegal character must produce an Error token
    let input3 = "x = @ y";
    let tokens3 = Tokenizer::tokenize(input3);
    let has_error = tokens3.iter().any(|t| matches!(t, Token::Error(_)));
    assert!(has_error, "should detect illegal char '@'");

    // Adversarial test: malformed operator sequence (not real state machine, but mixed)
    let input4 = "123abc";
    let tokens4 = Tokenizer::tokenize(input4);
    // Should tokenize as Number(123) then Ident(abc), not merge them
    assert_eq!(tokens4[0], Token::Number("123".to_string()));
    assert_eq!(tokens4[1], Token::Ident("abc".to_string()));

    // Adversarial test: underscore in identifier
    let input5 = "_private_var_123";
    let tokens5 = Tokenizer::tokenize(input5);
    assert_eq!(tokens5[0], Token::Ident("_private_var_123".to_string()));

    println!("state_machine_tokenizer: PASS");
}
