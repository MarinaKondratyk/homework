# Напишите программу, принимающую три числа, третье число это приблизительная
# сумма первых двух, программа должна возвращать сообщения вида: "больше", "меньше" или "равно".

a = float(input('Enter number 1: '))
b = float(input('Enter number 2: '))
c = float(input('Enter number 3 (≈ number 1 + number 2): '))
if (a + b) > c:
    print('Bigger')
elif (a + b) < c:
    print('Smaller')
else:
    print('Equal')
