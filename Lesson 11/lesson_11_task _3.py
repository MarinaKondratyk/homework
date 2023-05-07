#['07.05.2023', '08.06.2023'], ['2023-05-07', '2023-06-08']


def edit_date(array: str) -> str:
    array_lst = array.split('.')
    day = array_lst[0]
    month = array_lst[1]
    year = array_lst[2]
    return '-'.join([year, month, day])


def sort_date(array: list) -> list:

    return sorted([edit_date(x) for x in array])

print(sort_date(['11.09.2024', '07.05.2023', '08.06.2023']))
