from collections import Counter

# Товар -> категорія
products = {
    "Ноутбук": "Електроніка",
    "Миша": "Електроніка",
    "Клавіатура": "Електроніка",
    "Стіл": "Меблі",
    "Стілець": "Меблі",
    "Зошит": "Канцелярія",
    "Ручка": "Канцелярія",
    "Олівець": "Канцелярія",
}

category_counts = Counter(products.values())

for category, count in sorted(category_counts.items()):
    print(f"{category}: {count}")