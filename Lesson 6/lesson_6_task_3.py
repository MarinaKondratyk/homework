# Написать функцию, которая будет конвертировать строку в CamelCase. Например:
# "the-stealth-warrior" -> "theStealthWarrior"
# "The_Stealth_Warrior" -> "TheStealthWarrior"
# "The_Stealth-Warrior" -> "TheStealthWarrior"


SEPARATORS = '-_'


def to_camelcase(array: str) -> str:
        for symbol in array:
            if symbol in SEPARATORS:
                array = array.replace(symbol, ' ')
        first_word = array.split()[0]   #immutable
        res = [word.capitalize() for word in array.split()[1:]]
        return first_word + (''.join(res))

print(to_camelcase("the_stealth-warrior"))



