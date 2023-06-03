from annotations import (PersonAnnotation, HouseAnnotation)
from models import (generate_person, generate_house)


def price_with_discount(house: HouseAnnotation, discount: int) -> float:
    print(house)
    house.price -= house.price * (discount / 100)
    return house.price


def buy_house(person: PersonAnnotation, super_price: float):
    print(person)
    print(f'Price of house with discount {super_price}$')
    if person.own_money >= super_price:
        person.own_money -= super_price
        person.own_house += 1
        return f"Now I have {person.own_house} house."
    else:
        return "Unfortunately, I don't have enough money."


print(buy_house(generate_person(), price_with_discount(generate_house(), 10)))