class Book:
    def __init__(self, name: str, author: str, publication_year: int):
        self.name = name
        self.author = author
        self.publication_year = publication_year


class Car:
    def __init__(self, brend: str, model: str, car_year: int, color: str):
        self.brend = brend
        self.model = model
        self.car_year = car_year
        self.color = color

    def car_start(self) -> str:
        return 'Start the car'


class Fridge:
    def __init__(self, brend: str, capacity: int, model: str):
        self.brend = brend
        self.capacity = capacity
        self.model = model

    def open_door(self) -> str:
        return "Open the fridge door"

    def close_door(self) -> str:
        return "Close the fridge door"

    def turn_on(self) -> str:
        return "Turn on the fridge"


class Man:
    def __init__(self, name: str, surname: str, age: int, phone_number: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number

    def stand_up(self) -> str:
        return 'A man stood up'

    def sit_down(self) -> str:
        return 'A man sat down'


class Square:
    def __init__(self, side: int, color: str):
        self.side = side
        self.color = color

    def perimeter(self) -> str:
        return f'The perimeter of the square is {self.side * 4}'

    def area(self) -> str:
        return f'The area of the square is {self.side ** 2}'


class House:
    def __init__(self, floors: int, area: int, rooms: int):
        self.floors = floors
        self.area = area
        self.rooms = rooms

    def price(self) -> str:
        return f'The price of the house is {self.area * 1000}$'


class Student:
    def __init__(self, name: str, surname: str, age: int, grades: list):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades
        self.average_grade = round(sum(self.grades) / len(self.grades), 2)

    def average_grades(self) -> str:
        return f"{self.name} {self.surname}'s average is {self.average_grade}"

    def information_on_progress(self) -> str:
        if self.average_grade >= 3:
            return f"{self.name} {self.surname}'s progress is above average"
        else:
            return f"{self.name} {self.surname}'s progress is below average"


student_1 = Student('Ivan', 'Ivanov', 12, [3, 4, 5, 5, 4, 5])
student_2 = Student('Petia', 'Petrov', 12, [3, 2, 2, 2, 2, 1])

print(student_1.average_grades())
print(student_1.information_on_progress())
print(student_2.average_grades())
print(student_2.information_on_progress())