grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [sum(grades[i]) / len(grades[i]) for i in range(len(grades))]
students = sorted(list(students))
students_average_grade = dict(zip(students, grades))
print(students_average_grade)