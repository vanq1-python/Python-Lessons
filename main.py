my_list = []
i = 0
while True:
    if my_list[i] < 0:
        break
    elif my_list[i] >= 0 and i <= len(my_list):
        print(my_list[i])
        i += 1
    else:
        continue
