students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average_grades = []

for i in grades:
    grade_average = sum(i[:]) / len(i[:])
    average_grades.append(grade_average)

sort_students = sorted(students)
dictionary = dict(zip(sort_students, average_grades))
print(dictionary)
