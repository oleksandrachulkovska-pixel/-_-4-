numbers = [6, 5, 4, 3, 2, 1, 0]

# Видалення дублікатів зі збереженням порядку
unique_numbers = list(dict.fromkeys(numbers))

# Отримання множини парних чисел
even_numbers = {n for n in numbers if n % 2 == 0}

# П'ять найменших чисел
five_minimum = tuple(sorted(numbers)[:5])

# Створення словника "позиція -> значення"
position_value = dict(enumerate(numbers))

# Підрахунок дублікатів
duplicates_count = len(numbers) - len(unique_numbers)

print("Без дублікатів:", unique_numbers)
print("Парні числа:", sorted(even_numbers))
print("П'ять мінімальних:", five_minimum)
print("Позиція -> значення:", position_value)
print("Кількість елементів:", len(numbers))
print("Кількість дублікатів:", duplicates_count)
print("Мінімум:", min(numbers) if numbers else None)
print("Максимум:", max(numbers) if numbers else None)