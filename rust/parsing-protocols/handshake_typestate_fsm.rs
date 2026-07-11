#![forbid(unsafe_code)]

// Typestate markers
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct Init;
struct Hello;
struct Auth;
struct Ready;

struct Handshake<State> {
    state: std::marker::PhantomData<State>,
    data: String,
}

impl Handshake<Init> {
    fn new() -> Self {
        Handshake {
            state: std::marker::PhantomData,
            data: String::from("INIT"),
        }
    }

    fn send_hello(self, msg: &str) -> Result<Handshake<Hello>, String> {
        if msg.is_empty() {
            return Err("hello message empty".to_string());
        }
        Ok(Handshake {
            state: std::marker::PhantomData,
            data: self.data + " -> HELLO:" + msg,
        })
    }
}

impl Handshake<Hello> {
    fn send_auth(self, token: &str) -> Result<Handshake<Auth>, String> {
        if token.is_empty() {
            return Err("auth token empty".to_string());
        }
        Ok(Handshake {
            state: std::marker::PhantomData,
            data: self.data + " -> AUTH:" + token,
        })
    }
}

impl Handshake<Auth> {
    fn send_ready(self) -> Result<Handshake<Ready>, String> {
        Ok(Handshake {
            state: std::marker::PhantomData,
            data: self.data + " -> READY",
        })
    }
}

impl Handshake<Ready> {
    fn get_data(&self) -> &str {
        &self.data
    }
}

fn main() {
    // Ground truth: happy path
    let hs = Handshake::new();
    let hs = hs.send_hello("greetings").unwrap();
    let hs = hs.send_auth("secret_token").unwrap();
    let hs = hs.send_ready().unwrap();
    assert!(hs.get_data().contains("READY"));

    // Ground truth: state machine forces order
    let hs2 = Handshake::new();
    // Cannot call send_auth on Init — compiler would reject this
    // (Handshake<Init> does not have send_auth method)
    let hs2 = hs2.send_hello("hi").unwrap();
    // Cannot call send_ready on Hello
    // (Handshake<Hello> does not have send_ready method)
    let hs2 = hs2.send_auth("token").unwrap();
    let hs2 = hs2.send_ready().unwrap();
    assert!(hs2.get_data().contains("READY"));

    // Adversarial: empty hello message rejected
    let hs3 = Handshake::new();
    assert!(hs3.send_hello("").is_err());

    // Adversarial: empty auth token rejected
    let hs4 = Handshake::new();
    let hs4 = hs4.send_hello("msg").unwrap();
    assert!(hs4.send_auth("").is_err());

    // Adversarial: data integrity through chain
    let hs5 = Handshake::new();
    let hs5 = hs5.send_hello("msg1").unwrap();
    let hs5 = hs5.send_auth("auth1").unwrap();
    let hs5 = hs5.send_ready().unwrap();
    let full_trace = hs5.get_data();
    assert!(full_trace.contains("INIT"));
    assert!(full_trace.contains("HELLO:msg1"));
    assert!(full_trace.contains("AUTH:auth1"));
    assert!(full_trace.contains("READY"));

    println!("handshake_typestate_fsm: PASS");
}
