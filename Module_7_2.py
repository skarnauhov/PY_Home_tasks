import io
from os import path
from pprint import pprint

def custom_write(file_name, strings):
    if path.isfile("C:\\Users\\KSK\\PycharmProjects\\Module_7\\test.txt"):  # этот наворот нужен чтобы не записывать
        file = open(file_name, 'r', encoding='utf-8')                       # символ '\n' в конец файла
        file.read()                                                         #
        t = file.tell()                                                     #
        file.close()                                                        #
    else:                                                                   # иначе можно, написать просто:
        t = 0                                                               # t = 0
    string_positions = {}

    for string in strings:
        file = open(file_name, 'a', encoding='utf-8')
        file.seek(t)
        if t == 0:                                                          # и
            file.write(string)                                              # file.write(string + '\n')
            t = file.tell()
        else:                                                               # вместо решеток
            file.write('\n' + string)                                       #
        file.close()

    file = open(file_name, 'r', encoding='utf-8')
    count = 1
    t = file.tell()
    line_in_file = file.readline()
    string_positions[(count, t)] = line_in_file

    while line_in_file:
        count += 1
        t = file.tell()
        line_in_file = file.readline()
        if line_in_file:
            string_positions[(count, t)] = line_in_file
    file.close()

    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

