# Список
L = [3, 1, 4, 1, 5]
L.append(9)
L.extend([2, 6])
L.insert(1, 7)
L.remove(1)
last = L.pop()
L.sort()
print("Список:", L)
print("Перші 3:", L[:3], "Зріз:", L[1:4], "Довжина:", len(L))

# Кортеж
t = (1, 2, 3, 2)
print("Кортеж:", t, "count(2):", t.count(2), "index(3):", t.index(3))
try:
    t[0] = 9
except TypeError as e:
    print("Помилка зміни кортежу:", e)
print("Кортеж -> список -> кортеж:", tuple(list(t)))

# Множини
A, B = {1, 2, 3}, {3, 4, 5}
print("Об'єднання:", A.union(B), A | B)
print("Перетин:", A.intersection(B), A & B)
print("Різниця:", A.difference(B), A - B)
print("Симетрична різниця:", A.symmetric_difference(B), A ^ B)
print("{1, 2} — підмножина A:", {1, 2} <= A)

# Словник
d = {'a': 1, 'b': 2}
d.update({'b': 5, 'c': 3})
d['d'] = 4
print("Значення для b:", d.get('b'))
print("Ключі:", list(d.keys()))
print("Значення:", list(d.values()))
print("Пари:", list(d.items()))
d.pop('a')
print("Після видалення:", d)