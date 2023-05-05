a = ['dkeo', 'wej', 'qeij', 'qwiej', 'wej']
if len(a) == 0:
    print("no one likes this")
elif len(a) == 1:
    print(f'{a[0]} likes this')
elif len(a) == 2:
    print(f'{a[0]} and {a[1]} like this')
elif len(a) == 3:
    print(f'{a[0]}, {a[1]}, {a[2]} like this')
else:
    print(f'{a[0]}, {a[1]} and {len(a) - 2} others like this')

