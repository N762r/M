with open('17.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]
#numbers = [...]  # Здесь должен быть список чисел из файла

# Находим максимальное число, оканчивающееся на 3
max_ending_in_3 = max([x for x in numbers if str(x).endswith('3')])

# Инициализируем счетчик пар и максимальную сумму квадратов
count = 0
max_sum_squares = 0

# Перебираем пары последовательных чисел
for i in range(len(numbers) - 1):
    # Проверяем, оканчивается ли только одно число на 3
    if (str(numbers[i]).endswith('3')) != (str(numbers[i + 1]).endswith('3')):
        # Вычисляем сумму квадратов пары
        sum_squares = numbers[i]**2 + numbers[i + 1]**2
        # Проверяем условие суммы квадратов
        if sum_squares >= max_ending_in_3**2:
            count += 1
            max_sum_squares = max(max_sum_squares, sum_squares)

# Выводим результат
print(count, max_sum_squares)
