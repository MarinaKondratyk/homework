# Написать программу, которая посчитает кол-во одинаковых элементов в списке.
# Список будет заполняться рандомными целыми числами. Рекомендую использовать
# несколько функций (для заполнения списка целыми числами, для подсчета количества, для вывода)

from random import randint
from collections import Counter


def random_nums(n: int) -> list:
    lst = [randint(1, 50) for _ in range(n)]
    print(lst)
    return lst


def count_dublicates(array: list) -> int:
    dublicates = 0
    array_counter = Counter(array)
    for i in array_counter.values():
        if i > 1:
            dublicates += 1
    return dublicates


def print_count(dublicate: int) -> str:
   return f'Dublicates count in list {dublicate}'


print(print_count(count_dublicates(random_nums(15))))







