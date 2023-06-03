from random import randint

from constants import NAMES


class Person:

    def __init__(self, name: str, age: int, own_money=0):
        self.name = name
        self.age = age
        self.own_money = own_money
        self.own_house = 0

    def __repr__(self):
        return f"My name's {self.name}. My age's {self.age}."\
               f"I don't have my own house. I have {self.own_money}$."

    def __str__(self):
        return f"My name's {self.name}. My age's {self.age}." \
               f"I don't have my own house. I have {self.own_money}$."

    def make_money(self, salary):
        self.own_money += salary


class House:

    def __init__(self, square: int, price: int):
        self.square = square
        self.price = price

    def __repr__(self):
        return f"House:\nSquare: {self.square}m2\nPrice: {self.price}$\n"

    def __str__(self):
        return f"House:\nSquare: {self.square}m2\nPrice: {self.price}$\n"


def generate_person() -> Person:
    return Person(name=NAMES[randint(0, len(NAMES)-1)], age=(randint(30, 50)),
                  own_money=randint(50_000, 1_000_000))


def generate_house() -> House:
    return House(square=randint(70, 500), price=randint(50_000, 1_000_000))




