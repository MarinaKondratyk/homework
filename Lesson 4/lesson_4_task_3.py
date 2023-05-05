# "1 2 3 4 5" найдите самое большое и маленькое число в этой строке и верните их кортежем.

a = '1 2 3 4 5'
d = a.split()
c = []

for number in d:
    number = int(number)
    c.append(number)

b = min(c), max(c)
print(tuple(b))

