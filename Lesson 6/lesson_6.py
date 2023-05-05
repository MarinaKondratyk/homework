# Есть некий список, нужно вывести новый список
# согласно введенного типа данных
#
# lst = [1, 'hello', 3.14]
# data_type = input('Enter values:\n1. int\n2. str\n3. float\nEnter: ')
# c =[]
#
#
# def custom_sort (array, d_type):
#     res = []
#     for value in array:
#        if isinstance(value, d_type):
#            res.append(value)
#     return res
#
#
# if data_type == "1":
#     print(custom_sort(lst, int))
# elif data_type == '2':
#     print(custom_sort(lst, str))
# elif data_type == '3':
#     print(custom_sort(lst, float))
# else:
#     raise ValueError()

# if data_type == "1":
#     for element in lst:
#         if isinstance(element, int):
#            c.append(element)
#     print(c)
# elif data_type == '2':
#     for element in lst:
#         if isinstance(element, str):
#            c.append(element)
#     print(c)
# elif data_type == '3':
#     for element in lst:
#         if isinstance(element, float):
#             c.append(element)
#     print(c)
# else:
#     raise ValueError()

# Дается промежуток чисел и нужно просуммировать
# все целые числа в данном промежутке


# def sum_range(start, end):
#     result_range = list(range(start, end+1))
#     return sum(result_range)
#
# print(sum_range(1, 5))


# Написать функцию, которая будет убирать дубликаты в списке, список будет заполняться
# рандомными целыми числами

from random import randint

def random_range (start, end, count):
    lst = []
# нам нужно запустить функцию rangeit столько раз сколько стоит вводится в count, для этого
# мы как будто будем иттерироваться, перебирать последовательность от 0 до count
# и таким образом мы сможем запустить нужное количество раз операцию rangeit
# в for _ ничего нету, поэтому ничего происходить не будет
# range(count) - вызывает список от 0 до count, если в count = 5, вызовется список от 0 до 4,
# список, который как раз содержит 5 эелементов, по которому мы якоыб будет иттерироваться,
# на самом деле нет. То есть якобы перебирая элементы из списка range(count) мы каждый раз
# вызываем фунцкию lst.append и добавляем одно рандомное значение из библиотеки значений random randint
    for _ in range(count):
        lst.append(randint(start, end))
    return lst


def remove_dublicates(lst):
    if len(lst) == 0:
        return None
    elif len(set(lst)) == len(lst):
        return f"{lst} without dublicates"
    else:
        return f"{list(set(lst))} without dublicates"


print(remove_dublicates(random_range(1, 30, count=20)))