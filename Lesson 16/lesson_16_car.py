# Реализовать класс Car с атрибутами название, километраж, страна производитель. Переопределять
# метод eq (на основании страны производителя), создать метод для обнуления километража.
# Реализовать метод, возвращающий значение кол-ва созданных экземпляров.
# 2. Создать функцию для генерирования заданного количества экземпляров.
# 3. Создать функцию, которая будет сортировать полученный список по переданному
# параметру(атрибут экземпляру)

from random import randint
from typing import NamedTuple

MODELS = ['Acura', 'Alfa', 'Romeo', 'Aston', 'Martin', 'Audi', 'Bentley', 'BMW', 'Brilliance', 'Bugatti']
COUNTRIES = ['China', 'USA', 'Japan', 'Germany', 'South Korea', 'India', 'Mexico', 'Spain', 'Brazil', 'Canada']


class CarsAnnotation(NamedTuple):
    model: str
    mileage: int
    country: str


class Car:
    __count_object = 0

    def __init__(self, model: str, mileage: int, country: str):
        self.model = model
        self.mileage = mileage
        self.country = country
        Car.__count_object += 1

    def __eq__(self, other) -> str:
        if self.country == other.country:
            return f"{self.model} and {other.model} are from {self.country}."
        else:
            return f"{self.model} is from {self.country} and {other.model} is from {other.country}."

    def reset_mileage(self) -> str:
        self.mileage = 0
        return f"Mileage is {self.mileage}."

    @staticmethod
    def get_count_object():
        return Car.__count_object

    def __str__(self):
        return f'Model: {self.model}\nMileage: {self.mileage}\nCountry: {self.country}'

    def __repr__(self):
        return f'\nModel: {self.model}  Mileage: {self.mileage}  Country: {self.country}'


def create_cars(count: int) -> list[Car]:
    return [Car(model=MODELS[randint(0, len(MODELS) - 1)], mileage=randint(0, 200_000),
                country=COUNTRIES[randint(0, len(COUNTRIES) - 1)]) for _ in range(count)]


def sort_cars(cars_list: list[CarsAnnotation], attribute: str) -> list[CarsAnnotation]:
    if attribute == 'model':
        return sorted(cars_list, key=lambda car: car.model)
    elif attribute == 'mileage':
        return sorted(cars_list, key=lambda car: car.mileage)
    elif attribute == 'country':
        return sorted(cars_list, key=lambda car: car.country)
    else:
        raise ValueError('Value is not correct!')


create_cars_list = create_cars(6)
print(sort_cars(create_cars_list, 'mileage'))
print(Car.get_count_object())

# my_car = Car('Audi', 10_000, 'Germany')
# your_car = Car('BMW', 100_000, 'Germany')
# print(my_car.__eq__(your_car))
# print(my_car.reset_mileage())
# print(my_car.mileage)