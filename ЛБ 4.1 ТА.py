import re
from collections import Counter

text = r"Paths: /home/user/docs and C:\Users\\."

words = re.findall(r"\w+", text.lower())
unique_words = set(words)
sorted_by_length = tuple(sorted(words, key=len))
frequencies = dict(Counter(words))
top5 = Counter(words).most_common(5)

print("Список слів:", words)
print("Унікальні слова:", sorted(unique_words))
print("Кортеж за довжиною:", sorted_by_length)
print("Частоти:", frequencies)
print("Усього слів:", len(words))
print("Унікальних слів:", len(unique_words))
print("Топ-5:", top5)