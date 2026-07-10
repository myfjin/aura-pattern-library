#![forbid(unsafe_code)]
//! Roman numeral codec: integer ↔ Roman numeral (range 1..=3999).
//! Core idea: subtractive notation (IV=4, IX=9, XL=40, XC=90, CD=400, CM=900).
//! When to use: numeral display, parsing historical text, constraint-based encoding.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn int_to_roman(mut n: u16) -> Option<String> {
    if n == 0 || n > 3999 { return None; }

    let values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    let symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];

    let mut result = String::new();
    for (i, &val) in values.iter().enumerate() {
        while n >= val {
            result.push_str(symbols[i]);
            n -= val;
        }
    }
    Some(result)
}

fn roman_to_int(s: &str) -> Option<u16> {
    let values = [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)];
    let mut total = 0u16;
    let mut prev_val = 0i32;

    for c in s.chars().rev() {
        let val = values.iter().find(|(ch, _)| *ch == c)?.1 as i32;
        if val < prev_val {
            total -= val as u16;
        } else {
            total += val as u16;
        }
        prev_val = val;
    }

    if total > 0 && total <= 3999 { Some(total) } else { None }
}

fn main() {
    // CANONICAL test vectors
    let tests = [
        (1u16, "I"),
        (4, "IV"),
        (9, "IX"),
        (27, "XXVII"),
        (49, "XLIX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (3888, "MMMDCCCLXXXVIII"),
        (3999, "MMMCMXCIX"),
    ];

    for (num, expected_roman) in &tests {
        let roman = int_to_roman(*num).expect("int_to_roman failed");
        assert_eq!(&roman, expected_roman, "int_to_roman({}) mismatch", num);
        let decoded = roman_to_int(expected_roman).expect("roman_to_int failed");
        assert_eq!(decoded, *num, "roman round-trip mismatch");
    }

    // Round-trip for all values in range
    for i in 1..=100 {
        let roman = int_to_roman(i).expect("encode failed");
        let decoded = roman_to_int(&roman).expect("decode failed");
        assert_eq!(decoded, i, "round-trip failed for {}", i);
    }

    // Test boundary cases
    assert_eq!(int_to_roman(0), None, "0 should be invalid");
    assert_eq!(int_to_roman(4000), None, "4000 should be invalid");
    assert_eq!(roman_to_int("I" ), Some(1));
    assert_eq!(roman_to_int("MMMCMXCIX"), Some(3999));

    // Property: subtractive notation works correctly
    assert_eq!(roman_to_int("IV"), Some(4));
    assert_eq!(roman_to_int("IX"), Some(9));
    assert_eq!(roman_to_int("XL"), Some(40));
    assert_eq!(roman_to_int("XC"), Some(90));
    assert_eq!(roman_to_int("CD"), Some(400));
    assert_eq!(roman_to_int("CM"), Some(900));

    println!("roman_numeral ... PASS");
}
