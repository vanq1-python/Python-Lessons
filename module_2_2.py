first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
a = first
b = second
c = third
if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)