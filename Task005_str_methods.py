#module_1_4
my_string = input('Введите любой текст: ')
print('Длина строки: ', len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
print(my_string[:1:])
print(my_string[-1::])
print((''.join(reversed(my_string)))[:1:]) #сложный путь