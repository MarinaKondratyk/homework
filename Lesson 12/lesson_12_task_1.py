# Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент
# при инициализации (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и
# {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».


class Soda:
    def __init__(self, addition = 'нет'):
        self.addition = addition

    def show_my_drink(self):
        if self.addition == 'нет':
            return 'Обычная газировка'
        else:
            return f'Газировка и {self.addition}'


drink_1 = Soda('клубничный сироп')
drink_2 = Soda()

print(drink_1.show_my_drink())
print(drink_2.show_my_drink())