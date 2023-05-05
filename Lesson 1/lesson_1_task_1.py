side_a = float(input("Введите длину стороны равностороннего треугольника:"))
height = (side_a * (3 ** 0.5)) / 2
square = side_a * height * 0.5
perimetr = side_a * 3

print("Высота треугольника:", height)
print("Площадь треугольника:", square)
print("Периметр треугольника:", perimetr)