# На вход передается строка, необходимо посчитать количество гласных букв в этой строке.

vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
line = input('Введите строку: ')
line_list = list(line)
i = []

for vowel in line:
    if vowel in vowels:
        i.append(vowel)
print(f'Гласных букв в строке - {len(i)}')