# 1. Создайте класс "Человек" с атрибутами "имя", "возраст" и "рост". Используя property декоратор,
# реализуйте методы получения и установки значений для каждого атрибута.


class Human:
    def __init__(self, age, height):
        self.__age = age
        self.__height = height

    @property
    def age(self):
        return self.__age

    @age.getter
    def age(self):
        return f"Age's {self.__age}."

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def height(self):
        return self.__height

    @height.getter
    def height(self):
        return f"Height's {self.__height}."

    @height.setter
    def height(self, new_height):
        self.__height = new_height


# 2. Создайте класс "Круг" с атрибутом "радиус". Используя property декоратор, реализуйте
# методы получения и установки значения радиуса. Также добавьте метод для вычисления площади круга.


import math


class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.getter
    def radius(self):
        return f"The circle radius is {self._radius}"

    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius

    def square(self):
        return round(math.pi * (self._radius ** 2), 2)


circle_1 = Circle(2)
print(circle_1.radius)
print(circle_1.square())
circle_1.radius = 4
print(circle_1.radius)
print(circle_1.square())


# 3. Создайте класс "Банк" с атрибутом "баланс". Используя property декоратор, реализуйте
# методы получения и установки значения баланса. Также добавьте методы для пополнения и
# снятия денег со счета.


class Bank:

    def __init__(self):
        self.__account = 0

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, sum_money: int) -> None:
        self.__account = sum_money

    @account.getter
    def account(self) -> str:
        return f"You have {self.__account}$ in your account."

    def deposit(self, plus_sum_money: int) -> str:
        self.__account += plus_sum_money
        return f"Putted {plus_sum_money}. You have {self.__account} in your account."

    def cash(self, minus_sum_money: int) -> str:
        if self.__account >= minus_sum_money:
            self.__account -= minus_sum_money
            return f"Account balance {self.__account}"
        else:
            return f"You don't have enough money. You have only {self.__account}"


bank_1 = Bank()
print(bank_1.account)
bank_1.account = 20
print(bank_1.account)
print(bank_1.deposit(20))
print(bank_1.cash(50))


# 4. Создайте класс "Телефон" с атрибутами "модель", "цвет" и "стоимость".
# Используя property декоратор, реализуйте методы получения и установки значений для каждого атрибута.
# Также добавьте метод для вычисления скидки на телефон в зависимости от его стоимости.


class Phone:

    def __init__(self, model=None, color=None, price=0):
        self._model = model
        self._color = color
        self._price = price

    @property
    def model_color_price(self) -> str:
        return f"{self._model} {self._color} {self._price}"

    @model_color_price.setter
    def model_color_price(self, new_model_color_price: str) -> None:
        first, second, third = new_model_color_price.split()
        self._model = first
        self._color = second
        self._price = int(third)

    @model_color_price.getter
    def model_color_price(self) -> str:
        return f"Model's {self._model}, color's {self._color}, price's {self._price}$."

    def discount(self) -> float:
        if self._price in range(1000, 1501):
            return self._price * 0.85
        elif self._price in range(700, 1000):
            return self._price * 0.9
        else:
            return self._price * 0.95


my_phone = Phone()
print(my_phone.model_color_price)
my_phone.model_color_price = "Iphone red 1450"
print(my_phone.model_color_price)
print(my_phone.discount())







