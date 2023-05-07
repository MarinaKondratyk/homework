from random import choice, randint
from string import ascii_letters


def random_string(word_count: int) -> str:
    random_word = lambda : ''.join(choice(ascii_letters) for _ in range(randint(5, 10)))
    words = [random_word() for _ in range(word_count)]
    print(words)
    return ' '.join(words)


def count_vowels(array: str) -> int:
    vowels = "aeiuoyAEYUIO"
    k = 0
    for i in array:
        if i in vowels:
            k += 1
    return k >= 3


def custom_sort(array: str) -> int:
    count_words = list(filter(lambda x: count_vowels(x), array.split()))
    return len(count_words)


print(custom_sort(random_string(7)))