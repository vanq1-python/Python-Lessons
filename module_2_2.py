first = input('Введите первое целое число: ')
second = input('Введите второе целое число: ')
third = input('Введите третье целое число: ')
a = first
b = second
c = third
if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)