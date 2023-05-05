# Есть два списка одинаковой длины, необходимо составить словарь из этих двух списков. Напримр:
# products = [apple, milk, orange]
# count = [1, 3, 12]
# Результат должен быть: {apple: 1, milk: 3, orange: 12}

products = ['apple', 'milk', 'orange']
count = [1, 3, 12]
print(dict.fromkeys(*[products], *[count]))