# Написать функцию, принимающую число и возвращающую ближайший к этому числу палиндром.
# 11 -> 22
# 188 -> 191
# 191 -> 202
# 2541 -> 2552


def palindrom(value: int) -> int:

    while str(value) != str(value)[::-1]:
        value += 1
    return value


print(palindrom(2541))