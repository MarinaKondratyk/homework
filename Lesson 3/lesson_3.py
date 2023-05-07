# Задача калькулятор
number_1 = float(input())
operation = input()
number_2 = float(input())
if operation == "*":
    print(number_1 * number_2)
elif operation == "/":
    if number_2 == 0:
        print("Var number_2 can't == 0")
    else:
        print(number_1 / number_2)
elif operation == "+":
    print(number_1 + number_2)
elif operation == "-":
    print(number_1 - number_2)
else:
    raise Exception("Введен неверный оператор")


# Задача Пользователь вводит число — номер месяца (от 1
# до 12), программа должна вывести время года, которому
# этот месяц принадлежит (зима, весна, лето или осень).

a = int(input('Ввведите месяц '))
months = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
if a in months['Winter']:
    print('Winter')
elif a in months['Spring']:
    print('Spring')
elif a in months['Summer']:
    print('Summer')
elif a in months['Autumn']:
    print('Autumn')
else:
    raise Exception("It isn't number of month")

# Проверить является ли слово палиндромом
    # 1 способ
word = input('Enter word ')
a = list(word)
a.reverse()
word_reverse = "".join(a)

if word == word_reverse:
    print(f"'{word}' is palindrom")
else:
    print(f"'{word}' isn't palindrom")

    # 2 способ
word = input('Enter word ')
if word == word[::-1]:
    print(f"'{word}' is palindrom")
else:
    print(f"'{word}' isn't palindrom")

# Пользователь вводит количество месяцев и лет. Нужно вывести сколько это дней.
years = int(input('Enter years: '))
months = int(input('Enter months: '))
days = (years * 12 + months) * 30
print(days)