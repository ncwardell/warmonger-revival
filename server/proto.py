"""Warmonger wire format.

Header (16 bytes, little-endian):
  u16 length | u16 magic 0xA53C | u16 opcode | u16 extra | u32 tick | u32 key
Payload u32 words after the header are obfuscated as ~(w - key) when key != 0.
"""
import struct

MAGIC = 0xA53C
HEADER = struct.Struct("<HHHHII")
MASK = 0xFFFFFFFF


def deobfuscate(packet):
    length, magic, opcode, extra, tick, key = HEADER.unpack_from(packet)
    key &= 0xFFFF
    body = bytearray(packet[16:length])
    if key:
        words = len(body) // 4
        for i in range(words):
            (w,) = struct.unpack_from("<I", body, i * 4)
            struct.pack_into("<I", body, i * 4, ((~w) + key) & MASK)
    return opcode, extra, tick, key, bytes(body)


def build(opcode, payload=b"", extra=0, tick=0):
    """Server packet, plaintext (key 0). The client drops packets of 16 bytes or less."""
    if len(payload) == 0:
        payload = bytes(4)
    length = 16 + len(payload)
    return HEADER.pack(length, MAGIC, opcode, extra, tick, 0) + payload


def split(buffer):
    """Yield complete packets from a stream buffer; return the leftover."""
    packets = []
    while len(buffer) >= 4:
        length, magic = struct.unpack_from("<HH", buffer)
        if magic != MAGIC or length < 12:
            raise ValueError(f"bad header {buffer[:16].hex()}")
        if len(buffer) < length:
            break
        packets.append(bytes(buffer[:length]))
        buffer = buffer[length:]
    return packets, buffer
