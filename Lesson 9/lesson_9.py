# def prime(n: int) -> bool:
#     i = 2
#     while i <= int(n ** 0.5):
#         if n % i == 0:
#             return False
#         i += 1
#     else:
#         return True
#
# def lst_prime(array: list) -> bool:
#     a = list(filter(lambda x: prime(x), array))
#     if len(array) == len(a):
#         return True
#     else:
#         return False
#
# print(lst_prime([1, 17, 31, 43, 12]))


# Вывести сумму всех элементов [12, 2, 3, [[123], [12331]], [231, 123, 54]]

# import re
#
# def tree(array: list) -> int:
#     str_array = str(array)
#     nums = re.findall(r'\d+', str_array)
#     summ = sum(list(map(int, nums)))
#     return summ
#
#
# print(tree([12, 2, 3, [[123], [12331]], [231, 123, 54]]))


# Проверить какая функция работает быстрее

from datetime import datetime


def time_benchmark(func):
    def wrapper():
        start = datetime.now()
        func()
        result = datetime.now() - start
        print(result)
    return wrapper


@time_benchmark
def lst_comprehension() ->None:
    result = [x for x in range(10_000) if x % 2 == 0]


@time_benchmark
def lst_cicle() -> None:
    n = []
    for i in range(10_000):
        if i % 2 == 0:
            n.append(i)

lst_comprehension()
lst_cicle()