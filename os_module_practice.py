import os
import time
from os import chdir, makedirs
from os.path import join, getsize, dirname, getmtime

directory = os.getcwd()
print(directory)
os.chdir(os.pardir)
# os.chdir(r'C:\Users\KSK\PycharmProjects\Module_6')
# directory = os.getcwd()
print(os.getcwd())
print()

# os.makedirs(r'1234\123')

for root, dirs, files in os.walk(directory):
    print(root)
    print(dirs)
    print(files)
    print()

# for i in os.walk(directory):
#     print(i)
#     print()
#
# for root, dirs, files in os.walk(directory):
#     print(root, "потребляет")
#     print(sum(getsize(join(root, name)) for name in files), end=" ")
#     print("байт в", len(files), "файлах вне директорий")
#     print()

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = join(root, file)
        filetime = getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = getsize(filepath)
        dir_name = dirname(filepath)
        parent_dir = dirname(dir_name)
        print(f'Обнаружен файл: {file:<50}, Путь: {filepath:<90}, '
              f'Размер: {file_size:<7} байт, Время изменения: {formatted_time}, '
              f'Текущая директория: {dir_name:<70}, '
              f'Родительская директория: {parent_dir}')