# Задание "Средний балл"

"""
Вам необходимо решить задачу из реальной жизни:
"школьные учителя устали подсчитывать вручную средний балл каждого ученика,
поэтому вам предстоит автоматизировать этот процесс":
"""

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Переведем set в list и отсортируем в алфавитном порядке
students_sorted_list = sorted(students)

# Посчитаем средний балл каждого студента используя "list comprehension"
average_grades = [sum(grade) / len(grade) for grade in grades]

# Так как список студентов и оценки отсортированы соберем словарь с помощью функции "zip"
result = dict(zip(students_sorted_list, average_grades))

print(result)

