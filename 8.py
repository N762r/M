# Заданные значения
p = 6
q = 8
e = 9

# Вычисление функции f(n)
f_n = (p - 1) * (q - 1)

# Поиск наименьшего значения d, которое больше 50
d = 51  # начинаем поиск с 51, так как d должно быть больше 50
while (d * e) % f_n != 1:
    d += 1

print(f'Наименьшее значение числа d, которое больше 50: {d}')