# Написать функцию, которая принимает на вход два списка чисел и возвращает новый список,
# содержащий суммы соответствующих элементов этих списков. Использовать функцию map и lambda.


def sum_lst(array_1: list, array_2: list) -> list:
    if len(array_1) > len(array_2):
        while len(array_2) != len(array_1):
            array_2.append(0)
    else:
        while len(array_1) != len(array_2):
            array_1.append(0)
    sum = list(map(lambda x, y: x + y, array_1, array_2))
    return sum


print(sum_lst([1, 2, 3, 4, 5], [1, 2, 3, 4, 1, 1]))