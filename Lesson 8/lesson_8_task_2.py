# Написать рекурсивную функцию, которая осуществляет суммирование чисел во входящем списке.
from functools import reduce
def custom_sum(array: int) -> int:
    if array == 1:
        return array
    else:
        return array + custom_sum(array - 1)

print(custom_sum(5))