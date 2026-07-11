#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn parse_dns_name(data: &[u8]) -> Result<String, &'static str> {
    let mut name = String::new();
    let mut pos = 0;
    let mut pointer_depth = 0;
    const MAX_POINTER_DEPTH: usize = 10;

    loop {
        if pos >= data.len() {
            return Err("Overrun buffer");
        }

        let byte = data[pos];
        pos += 1;

        // Check for pointer (high 2 bits = 11)
        if byte & 0xC0 == 0xC0 {
            // Pointer
            if pos >= data.len() {
                return Err("Pointer incomplete");
            }
            let low_byte = data[pos];

            let pointer = (((byte & 0x3F) as usize) << 8) | (low_byte as usize);

            if pointer >= data.len() {
                return Err("Pointer out of bounds");
            }

            pointer_depth += 1;
            if pointer_depth > MAX_POINTER_DEPTH {
                return Err("Pointer depth limit exceeded");
            }

            pos = pointer;
            continue;
        }

        // Check for end of name (zero length)
        if byte == 0 {
            return Ok(name);
        }

        // Label
        let len = byte as usize;
        if pos + len > data.len() {
            return Err("Label overrun");
        }

        if !name.is_empty() {
            name.push('.');
        }

        let label = std::str::from_utf8(&data[pos..pos + len])
            .map_err(|_| "Invalid UTF-8 in label")?;
        name.push_str(label);
        pos += len;
    }
}

fn main() {
    // Test 1: Simple name
    let data = b"\x03www\x07example\x03com\x00";
    assert_eq!(
        parse_dns_name(data).unwrap(),
        "www.example.com",
        "Parse simple name"
    );

    // Test 2: Overrun length
    let data_overrun = b"\x05www"; // Length 5, but only "www"
    assert!(
        parse_dns_name(data_overrun).is_err(),
        "Should reject overrun length"
    );

    // Test 3: Overrun at buffer end
    let data_incomplete = b"\x03www\x07example"; // No terminator, incomplete
    assert!(
        parse_dns_name(data_incomplete).is_err(),
        "Should reject incomplete name"
    );

    // Test 4: Valid pointer to label in same message
    let mut data_ptr = Vec::new();
    data_ptr.extend_from_slice(b"\x03www"); // offset 0-3: "www"
    data_ptr.extend_from_slice(b"\xC0\x04"); // offset 4-5: pointer to offset 4... wait that's itself
    // Let me recalculate:
    // offset 0: 0x03
    // offset 1-3: "www"
    // offset 4: 0xC0
    // offset 5: 0x04
    // offset 6: 0x03
    // So pointer value (0xC0, 0x04) -> offset = ((0x00) << 8) | 0x04 = 4... that's the 0xC0 itself
    // Let me point to offset 6 instead
    data_ptr.pop(); data_ptr.pop(); // Remove the bad pointer
    data_ptr.extend_from_slice(b"\xC0\x06"); // pointer to offset 6
    data_ptr.extend_from_slice(b"\x03com\x00"); // offset 6+: "com" then terminator
    let result = parse_dns_name(&data_ptr).unwrap();
    assert_eq!(result, "www.com", "Should correctly dereference pointer");

    // Test 5: Pointer LOOP must be caught by the depth limit (self-referential + 2-cycle).
    // [0xC0,0x00]: pointer at offset 0 points to offset 0 → infinite self-loop.
    let data_self_loop = vec![0xC0u8, 0x00];
    assert!(
        parse_dns_name(&data_self_loop).is_err(),
        "Should reject self-referential pointer loop via depth limit"
    );
    // [0xC0,0x02, 0xC0,0x00]: offset 0 → 2, offset 2 → 0 → 2-cycle.
    let data_cycle = vec![0xC0u8, 0x02, 0xC0u8, 0x00];
    assert!(
        parse_dns_name(&data_cycle).is_err(),
        "Should reject 2-cycle pointer loop via depth limit"
    );

    // Test 6: Pointer out of bounds
    let data_oob = b"\xC0\xFF"; // Pointer to offset 255, likely out of bounds
    assert!(
        parse_dns_name(data_oob).is_err(),
        "Should reject pointer out of bounds"
    );

    // Test 7: Valid multi-label
    let data_multi = b"\x05hello\x05world\x04test\x00";
    assert_eq!(
        parse_dns_name(data_multi).unwrap(),
        "hello.world.test",
        "Parse multi-label name"
    );

    println!("dns_name_wire_parser: PASS");
}
