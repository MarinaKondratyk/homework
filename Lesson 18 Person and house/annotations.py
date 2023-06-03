from typing import NamedTuple


class PersonAnnotation(NamedTuple):
    name: str
    age: int
    own_money: int
    own_house: int


class HouseAnnotation(NamedTuple):
    square: int
    price: float