
a, b, c = int(input('enter a :')), int(input('enter b :')), int(input('enter c :'))
max: int = a
if b > max:
    max: int = b
if c > max:
    max: int = c
print(max)


