#module_1_5.py
immutable_var = (1, True, 'Number', 67.7)
print('Неизменяемый кортеж:', immutable_var)
print('При попытке изменить один из объектов: immutable_var[3] = 67.9, выдает ошибку: "tuple" object does not support item assignment')
mutable_list = [2, False, 'String', 89.9]
print('Изменяемый список:', mutable_list)
mutable_list[2] = 'Number'
print('Изменяемый список:', mutable_list)