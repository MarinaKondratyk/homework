# Передается строка из слов, необходимо вернуть самое короткое из них (мб несколько)

a = input('Введите строку: ')
c = a.split(" ")
c.sort(key=len)
print(c)
b = []
for word in c:
    if len(word) == len(c[0]):
        b.append(word)
print(b)