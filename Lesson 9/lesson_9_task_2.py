# Написать функцию, которая принимает на вход список строк и возвращает новый список,
# содержащий только те строки, которые содержат заданную подстроку.
# Пример использования:
# words = ["Apple", "Banana", "Apricot", "Cherry"]
# substring = "a"
# print(find_substring(words, substring)) # Output: [“Apple”, "Apricot"]


def find_substring(words: list, substring: str) -> list:
    # sort_words = []
    lower_words = list(map(lambda word: word.lower(), words))
    sort_words = [word for word in lower_words if word.count(substring) == 1]
    # for word in lower_words:
    #     if word.count(substring) == 1:
    #         sort_words.append(word)
    capitalize_words = list(map(lambda word: word.capitalize(), sort_words))
    return capitalize_words


print(find_substring(["Apple", "Banana", "Apricot", "Cherry"], 'a'))