grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = sorted(list(students)) # преобразование множества в отсортированный список

average_grades_list = []
number_of_students_list = []
students_and_average_grades_list =[]
n = -1
for grade in grades:
    average_grades_list.append(sum(grade) / len(grade)) # поэлементное созданме списка со средним баллом
    n=n+1
    number_of_students_list.append(n) # поэлеменое создание списка с порядковым номером ученика -1 для дальнейшего использования
    students_and_average_grades_list.append([students_list[n], average_grades_list[n]]) # создание списка с парами значений для преобразования в словарь

students_dict = dict(students_and_average_grades_list) 

print(students_dict)
