import math

# Количество символов в пароле
password_length = 20

# Количество символов в алфавите
alphabet_size = 26

# Вычисление минимального количества бит для одного символа
bits_per_character = math.ceil(math.log2(alphabet_size))

# Вычисление общего количества бит для одного пароля
total_bits_per_password = bits_per_character * password_length

# Перевод бит в байты
total_bytes_per_password = math.ceil(total_bits_per_password / 8)

# Общее количество байт, использованное для 20 пользователей
total_bytes_for_20_users = 500

# Вычисление байт, выделенных для дополнительных сведений об одном пользователе
additional_info_per_user = (total_bytes_for_20_users - (total_bytes_per_password * 20)) // 20

print(f'Количество байт, выделенное для хранения дополнительных сведений об одном пользователе: {additional_info_per_user}')
