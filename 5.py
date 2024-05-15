import struct

# Число для кодирования
number = -36.875

def encode_ieee_754(number):
    return struct.pack('f', number)

def bytes_to_hex(bytes):
    return ''.join(f"{byte:02x}" for byte in bytes)


encoded_bytes = encode_ieee_754(number)
encoded_hex = bytes_to_hex(encoded_bytes)
encoded_hex = encoded_hex[-2]+encoded_hex[-1]+encoded_hex[-4]+encoded_hex[-3]+encoded_hex[2]+encoded_hex[3]+encoded_hex[0]+encoded_hex[1]

print(f"Число {number} в формате IEEE-754 (32 бита): {encoded_hex}") 