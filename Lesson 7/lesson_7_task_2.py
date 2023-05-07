# Передана строка, у которой внутри каждого слова спрятана цифра.
# Отсортируйте эти слова по значению спрятанной цифры.
# "is2 Thi1s T4est 3a"  ->  "Thi1s is2 3a T4est"


def custom_sort(array: str) -> str:
    list_array = array.split()
    list_array.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))
    return ' '.join(list_array)


print(custom_sort("is2 Thi1s T4est 3a"))
