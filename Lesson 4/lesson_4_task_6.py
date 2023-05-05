# Передается список, состоящий из строк и букв, нужно вернуть новый список,
# содержащий только цифры.

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
line = input('Введите строку: ')
numbers_list = []

for number in line:
    if number in numbers:
        numbers_list.append(number)
print(numbers_list)

