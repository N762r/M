import math

# Количество символов в пароле
password1_length = 6
password2_lendth = 9
# Количество символов в алфавите
alphabet1_size = 30
alphabet2_size = 9

# Вычисление минимального количества бит для одного символа
bits1_per_character = math.ceil(math.log2(alphabet1_size))
bits2_per_character = math.ceil(math.log2(alphabet2_size))

# Вычисление общего количества бит для одного пароля
total_bits_per_password = bits1_per_character * password1_length + bits2_per_character * password2_lendth

# Перевод бит в байты
total_bytes_per_password = math.ceil(total_bits_per_password / 8)

# Общее количество байт, использованное для 20 пользователей
total_bytes_for_20_users = 4098

# Вычисление байт, выделенных для дополнительных сведений об одном пользователе
additional_info_per_user = (total_bytes_for_20_users - (total_bytes_per_password * 128)) // 128

print(f'Количество байт, выделенное для хранения дополнительных сведений об одном пользователе: {additional_info_per_user}')
