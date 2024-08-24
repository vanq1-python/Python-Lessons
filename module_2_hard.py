import random
first_field = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
first_field = random.choice(first_field)

if first_field > 2 and first_field < 21:
    print('Число первого поля:', first_field)

password = []

list_second_field = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in list_second_field:
    for j in list_second_field:
        num = i + j
        if first_field % num == 0 and i != j and j > i:
            password.append(i)
            password.append(j)


print('Пароль:', ''.join(map(str, password)))

