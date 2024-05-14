def find_programs(start, end, must_include, must_not_include):
    # Функция для рекурсивного поиска всех возможных программ
    def search(current, history):
        # Если текущее число уже есть в истории, прекращаем поиск, чтобы избежать циклов
        if current in history:
            return 0
        # Если достигли начального числа, проверяем условия задачи
        if current == start:
            if must_include in history and must_not_include not in history:
                return 1
            else:
                return 0
        # Если число меньше начального, прекращаем поиск
        if current < start:
            return 0
        
        # История для текущего шага
        new_history = history + [current]
        
        # Счетчик программ
        count = 0
        
        # Применяем обратные операции, если возможно, и увеличиваем счетчик
        count += search(current - 1, new_history)  # Обратное A
        if current % 2 == 0:
            count += search(current // 2, new_history)  # Обратное B
        if current % 3 == 0:
            count += search(current // 3, new_history)  # Обратное C
        
        return count
    
    # Начинаем поиск с конечного числа
    return search(end, [])

# Исходные данные задачи
start_number = 1
end_number = 25
must_include_number = 11
must_not_include_number = 15

# Поиск всех программ
programs_count = find_programs(start_number, end_number, must_include_number, must_not_include_number)
print(f'Количество программ: {programs_count}')
