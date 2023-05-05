# Напишите декоратор timer, который измеряет время выполнения функции и выводит его на экран.
# Используйте модуль time для измерения времени.

from time import time

def timer(func):
    def wrapper():
        start = time.clock()
        func
        result = time.clock() - start
    return wrapper


@timer
def lst_comprehension() ->None:
    result = [x for x in range(10_000) if x % 2 == 0]


@timer
def lst_cicle() -> None:
    n = []
    for i in range(10_000):
        if i % 2 == 0:
            n.append(i)


lst_comprehension()
lst_cicle()
