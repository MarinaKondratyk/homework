# Реализовать функцию, выполняющую сортировку "пузырьком" переданного списка.
[4, 6, 1, 12, 56]

from random import randint

a = [randint(1, 50) for i in range(10)]
print(a)

def bubble_sort(array: list) -> list:
    count = len(array)
    for _ in range(count):      # количество элементов
        for j in range(count-1):     # j - количество индексов, поэтому на 1 меньше, чем длина списка
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


print(bubble_sort(a))
