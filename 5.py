import struct

# Функция для кодирования числа в формат IEEE-754
def encode_ieee_754(number):
    # Кодируем число в байты с помощью стандартной библиотеки
    return struct.pack('f', number)

# Функция для преобразования байтов в шестнадцатеричное представление
def bytes_to_hex(bytes):
    return ''.join(f"{byte:02x}" for byte in bytes)

# Число для кодирования
number = -97.625

# Кодирование числа
encoded_bytes = encode_ieee_754(number)

# Преобразование в шестнадцатеричный формат
encoded_hex = bytes_to_hex(encoded_bytes)
encoded_hex = encoded_hex[-2]+encoded_hex[-1]+encoded_hex[-4]+encoded_hex[-3]+encoded_hex[2]+encoded_hex[3]+encoded_hex[0]+encoded_hex[1]

print(f"Число {number} в формате IEEE-754 (32 бита): {encoded_hex}") 