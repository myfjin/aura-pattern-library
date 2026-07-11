#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct Crc32;

impl Crc32 {
    fn compute(data: &[u8]) -> u32 {
        let mut crc: u32 = 0xFFFFFFFF;
        for &byte in data {
            let index = ((crc ^ (byte as u32)) & 0xFF) as usize;
            crc = (crc >> 8) ^ Self::TABLE[index];
        }
        !crc
    }

    const TABLE: [u32; 256] = Self::make_table();

    const fn make_table() -> [u32; 256] {
        let mut table = [0u32; 256];
        let poly = 0xEDB88320u32;
        let mut i = 0;
        while i < 256 {
            let mut crc = i as u32;
            let mut j = 0;
            while j < 8 {
                if crc & 1 != 0 {
                    crc = (crc >> 1) ^ poly;
                } else {
                    crc >>= 1;
                }
                j += 1;
            }
            table[i] = crc;
            i += 1;
        }
        table
    }
}

struct Packet {
    header: Vec<u8>,
    payload: Vec<u8>,
    crc: u32,
}

impl Packet {
    fn new(header: Vec<u8>, payload: Vec<u8>) -> Self {
        let mut data = header.clone();
        data.extend_from_slice(&payload);
        let crc = Crc32::compute(&data);
        Packet {
            header,
            payload,
            crc,
        }
    }

    fn serialize(&self) -> Vec<u8> {
        let mut result = self.header.clone();
        result.extend_from_slice(&self.payload);
        result.extend_from_slice(&self.crc.to_be_bytes());
        result
    }

    fn deserialize(data: &[u8]) -> Result<Self, String> {
        if data.len() < 4 {
            return Err("packet too short".to_string());
        }

        let crc_bytes = &data[data.len() - 4..];
        let received_crc = u32::from_be_bytes([crc_bytes[0], crc_bytes[1], crc_bytes[2], crc_bytes[3]]);

        let payload_data = &data[..data.len() - 4];
        let computed_crc = Crc32::compute(payload_data);

        if received_crc != computed_crc {
            return Err(format!(
                "CRC mismatch: received 0x{:08x}, computed 0x{:08x}",
                received_crc, computed_crc
            ));
        }

        Ok(Packet {
            header: vec![],
            payload: payload_data.to_vec(),
            crc: received_crc,
        })
    }
}

fn main() {
    // Ground truth: valid packet roundtrip
    let header = vec![0x01, 0x02];
    let payload = vec![b'h', b'e', b'l', b'l', b'o'];
    let packet = Packet::new(header, payload);
    let serialized = packet.serialize();
    let deserialized = Packet::deserialize(&serialized).unwrap();
    // deserialize() verifies the CRC over the whole body; with no length field it cannot
    // re-split header from payload, so `payload` holds the intact CRC-verified body
    // (header bytes followed by the original payload).
    assert_eq!(deserialized.payload, vec![0x01, 0x02, b'h', b'e', b'l', b'l', b'o']);

    // Ground truth: empty payload
    let packet2 = Packet::new(vec![0xFF], vec![]);
    let ser2 = packet2.serialize();
    assert!(Packet::deserialize(&ser2).is_ok());

    // Adversarial: flip one byte in header (first region)
    let header3 = vec![0x01, 0x02];
    let payload3 = vec![b'a', b'b', b'c'];
    let packet3 = Packet::new(header3, payload3);
    let mut corrupted3 = packet3.serialize();
    corrupted3[0] ^= 0x01; // Flip one bit
    assert!(Packet::deserialize(&corrupted3).is_err(), "header corruption not detected");

    // Adversarial: flip one byte in payload (middle region)
    let header4 = vec![0x11];
    let payload4 = vec![b'x', b'y', b'z'];
    let packet4 = Packet::new(header4, payload4);
    let mut corrupted4 = packet4.serialize();
    let payload_start = 1;
    corrupted4[payload_start + 1] ^= 0xFF; // Flip byte in payload
    assert!(Packet::deserialize(&corrupted4).is_err(), "payload corruption not detected");

    // Adversarial: flip one byte in CRC (last region)
    let header5 = vec![0x99];
    let payload5 = vec![b'q', b'u', b'e', b'r', b'y'];
    let packet5 = Packet::new(header5, payload5);
    let mut corrupted5 = packet5.serialize();
    let last5 = corrupted5.len() - 1;
    corrupted5[last5] ^= 0x01; // Flip CRC byte
    assert!(Packet::deserialize(&corrupted5).is_err(), "CRC corruption not detected");

    // Adversarial: truncated packet (missing CRC bytes)
    let packet6 = Packet::new(vec![0xAA], vec![b't', b'e', b's', b't']);
    let mut ser6 = packet6.serialize();
    ser6.truncate(ser6.len() - 2); // Remove some CRC bytes
    assert!(Packet::deserialize(&ser6).is_err());

    println!("crc_framed_packet: PASS");
}
