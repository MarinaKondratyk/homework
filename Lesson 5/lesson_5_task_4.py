#Написать программу на определение, является ли введенное число простым.
# Число должно вводится с клавиатуры любое количество раз без запуска программы заново,
# завершение программы произойдет только при вводе пользователем слова "exit" вместо числа.

number = int(input('Enter number: '))
k = 0
while number != 'exit':
    for element in range(2, number):
        if number % element == 0:
            k = k + 1
    if k > 0:
        print("The number isn't prime")
    else:
        print("The number is prime")
