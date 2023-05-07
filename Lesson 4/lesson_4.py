# Проверить является ли число, числом Армстронга
a = input()
degree = len(a)
c = 0
for element in list(a):
    c += int(element) ** degree
if c == int(a):
    print('Да')
else:
    print('Нет')

# Таже задача через функциональное программирование


def narcissistic(value: int) -> bool:
    value = str(value)
    extent = len(value)
    sum = 0
    for element in value:
        sum += int(element) ** extent
    return int(value) == sum

print(narcissistic(153))

# Таже задача через ленивое выражение


def narcissistic(value: int) -> bool:
    return value == sum(int(x) ** len(str(value)) for x in str(value))


# Проверить есть ли в списке элемент с типом данных строка (вообще задача решается через for)
a = [1, 2, 3, 4, 5, 'hello']
i = 0
while i <= len(a) - 1:
    if type(a[i]) == str:
        print(f'Есть строка {a[i]}')
        break
    i += 1

# Проверить правильность введенного email
    email = input('Введите ваш email: ')
    while '@' not in email:
        email = input('Введите ваш email: ')

# Возводить число в квадрат пока не будет введено слово exit
while True:
    a = input('Enter ')
    if a == 'exit':
        break
    else:
        print(int(a) ** 2)
print('Exit')

# Вычислить факториал числа
a = 3
i = 1

while a != 1:
    i *= a
    print(i)
    a -= 1
print(i)