# Если содержится одинаковое количество х и о -> True, иначе False

def xo_count(array: str) -> bool:
    return array.lower().count("x") == array.lower().count("o")


print(xo_count("xXoOo"))