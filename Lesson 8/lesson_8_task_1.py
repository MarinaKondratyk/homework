# Напишите функцию, которая принимает два числа в кач-ве аргументов и считает наименьшее
# общее кратное для этих чисел.


def calculate_lcm(x: int, y: int) -> int:
    max_num = max(x, y)
    while True:
        if max_num % y == 0 and max_num % x == 0:
            lcm = max_num
            break
        max_num += max(x, y)
    return lcm


print(calculate_lcm(246, 4465348))
