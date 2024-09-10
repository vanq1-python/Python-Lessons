from collections import Counter

# Чтение числа n
n = int(input().strip())

# Чтение массива a
a = list(map(int, input().strip().split()))

# Подсчет частоты каждого числа в массиве
count = Counter(a)

# Находим число с максимальной частотой
# Если несколько чисел имеют одинаковую частоту, выбираем наибольшее
max_count = max(count.values())
most_frequent_numbers = [num for num, freq in count.items() if freq == max_count]

result = max(most_frequent_numbers)

# Вывод результата
print(result)