# Сделать каждое слово в списке с большой буквы

# a = ['dog', 'cat', 'bird']
# a_capitalize = list(map(lambda word: word.capitalize(), a))
# print(a_capitalize)

# Все четные числа возвести в квадрат, а от нечетных отнять единицу

# from random import randint
#
# nums = [randint(1, 10) for i in range(5)]
# print(nums)
#
# edit_nums = list(map(lambda x: x ** 2 if x % 2 == 0 else x -1, nums))
# print(edit_nums)


# Найти все элементы в которых содержится буква 'а'

# animals = ['dog', 'cat', 'bird', 'shark', 'panda']
# animals_a = list(filter(lambda animal: 'a' in animal, animals))
# print(animals_a)


# Вычислить факториал числа при помощи фунцкии reduce

# from functools import reduce
# num = int(input("Enter value: "))
# def factorial(num):
#     result = reduce(lambda x, y: x * y, range(1, num+1))
#     return result
#
# print(factorial(num))


# Найти сумму всех чисел спрятанных в словах
#
# from functools import reduce
# def summ(array: str) -> int:
#     nums = list(filter(str.isdigit, array))
#     nums_int = list(map(int, nums))
#     result = reduce(lambda x, y: x + y, nums_int)
#     return result
#
# print(summ("is4 Thi1s T4est 3a"))


# На 1-ой автобусной остановке зашло 10 человек, вышло 5, на 2-ой зашло 3, вышло 2
# и на 4-ой зашло 4, вышло 7. Итого в конце осталось 3 человека.

a = [[10, 5], [3, 2], [4, 7]]

into = 0
out = 0

# 1 вариант решения:
# for station in a:
#     into += station[0]
#     out += station[1]
#
# # 2 вариант решения:
# for k, x in a:  # k, x то же самое что [k, x]
#     into += k
#     out += x
#
# print(into - out)

# Передается список, все четные числа оставить на месте, нечетные отсортировать в порядке возрастания

# def custom_sort(array: list) -> list:
#     odds = list(sorted(x for x in array if x % 2 != 0))
#     return [x if x % 2 == 0 else odds.pop(0) for x in array]
#
# print(custom_sort([3, 2, 1, 4]))

def fib(n):
    if n in (1, 2): #Условие завершения, рекурсия останавливается в момент удовлетворения условиям
        return 1
    else:
        return fib(n - 1) + fib(n - 2)