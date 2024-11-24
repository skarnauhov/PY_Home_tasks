import requests
from pprint import pprint
import pandas
from tabulate import tabulate
from extractor_1 import LinkExtractor
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

URL1 = 'https://xakep.ru/'
URL2 = 'https://ya.ru/'

# в результате работы программы будет создано 4 файла.

r1=requests.get(URL1, timeout=0.9) # получаем содержимое сайта в r1 для константы URL1
ext1 = LinkExtractor(URL1) # класс LinkExtractor наследуется от класса анализатора HTML (HTMLParser)
ext1.feed(r1.text) # при "скармливании" классу содержимого сайта в виде HTML, запускается метод handle_starttag,
print(ext1.links) # который в нашем случае анализирует наличие ссылок в определенных тэгах и создает из них список.
print('*'*20)

panda_1=pandas.Series(ext1.links) # создаем табличку panda_1 при помощи метода Series, в один ряд
print(panda_1)
print('*'*20)

print(f'На сайте {r1.url} других ссылок {len(ext1.links)} шт.')
print('*'*20)

#pprint(r1.text)
#print('*'*20)

print(r1.url) # смотрим на разные данные которые мы получили для r1 в результате запроса request
print('*'*20)

print(r1.status_code)
print('*'*20)

print(type(r1.text))
print('*'*20)

print(r1.cookies)
rr = r1.headers
print('*'*20)

print(isinstance(rr, dict))
print('*'*20)

print(type(rr))
print('*'*20)

pprint(rr)
print('*'*20)

print(r1.history)
print('*'*20)

r2=requests.get(URL2) # r2 запрос для второго сайта из URL2
print(r2.__doc__)
print('*'*20)

ext2 = LinkExtractor(URL2)
ext2.feed(r2.text) # создаем список ссылок аналогично r1
print(f'На сайте {r2.url} других ссылок {len(ext2.links)} шт.')
print('*'*20)

panda_2=pandas.Series(ext2.links) # создание табличку методом Series
print(panda_2)
print('*'*20)

index = [x for x in range(len(ext2.links))]
panda_2_1=pandas.DataFrame(ext2.links, index=index, columns=('links',)) # создание табличку другим методом, тоже 1 столбец, но с названием
print(panda_2_1)
print('*'*20)

# создание табличек при помощи словарей
panda_2_2=pandas.DataFrame({'num': [i+1 for i in range(len(ext1.links))],
                            f'{URL1}': ext1.links,
                            'Link_len': [len(link) for link in ext1.links],
                            })
print(panda_2_2)
print('*'*20)

panda_2_3 = pandas.DataFrame({f'{URL2}': ext2.links,
                            'Link_len': [len(link) for link in ext2.links]
                            })
panda_2_3_1 = panda_2_3.style.set_table_styles([dict(selector='th', props=[('text-align', 'right')])])
print(panda_2_3.tail(3))

# сохранение табличек в csv и excel
panda_2_3.to_csv('1234.csv', sep=' ')
panda_2_3.T.to_excel('12345.xlsx', sheet_name='54321')

# библиотека tabulate для простого отображения в виде таблицы в командной строке
print(tabulate(panda_2_3.head(3), headers='keys', tablefmt='psql'))
print('*'*20)

# создаем одномерный массив из 256 элементов и выводим его
test_array_1 = np.random.random(256)
print(test_array_1)
print('*'*20)

# преобразуем одномерный массив в четырехмерный и выводим, а также выводим свойства массива
test_array_2 = test_array_1.reshape(4, 4, 4, 4)
print(test_array_2.ndim, test_array_2.shape, test_array_2.size, test_array_2.dtype)
print('*'*20)

print(test_array_2)
print('*'*20)

# создаем три массива по четвертому измерению и выводим их
test_array_2_sum_ax_0 = ((test_array_2.sum(axis=0)).sum(axis=0)).sum(axis=0)
test_array_2_max_ax_0 = ((test_array_2.max(axis=0)).max(axis=0)).max(axis=0)
test_array_2_min_ax_0 = ((test_array_2.min(axis=0)).min(axis=0)).min(axis=0)
print(test_array_2_sum_ax_0)
print(test_array_2_max_ax_0)
print(test_array_2_min_ax_0)

# создаем обратный массив массиву суммы и выводим его
test_array_2_sum_ax_0_rev=np.flip(test_array_2_sum_ax_0)
print(test_array_2_sum_ax_0_rev)
print('*'*20)

# из массивов создаем табличку и выводим её
test_panda_4 = pandas.DataFrame({'Sum': test_array_2_sum_ax_0,
                                'Max': test_array_2_max_ax_0,
                                'Min': test_array_2_min_ax_0})
print(test_panda_4)
print('*'*20)

# создание, сохранение, а также вывод на экран графика с 4мя кривыми
x=plt.plot(test_array_2_min_ax_0)
y=plt.plot(test_array_2_max_ax_0)
z=plt.plot(test_array_2_sum_ax_0)
w=plt.plot(test_array_2_sum_ax_0_rev)
plt.savefig('1234.png')
plt.show()

# во время работы программы и после закрытия картинки с кривыми, изменяем размеры картинки и сохраняем рядом. А также выводим на экран.
img = Image.open('1234.png')
img_width, img_height = img.size
print(f'Размеры картинки с графиками ШхВ: {img_width}x{img_height}.')
img_bigger = img.resize((img_width*2, img_height*2))
img_width_b, img_height_b = img_bigger.size
print(f'Размеры картинки с графиками после изменения размеров ШхВ: {img_width_b}x{img_height_b}.')
img_bigger.save('4321.png')
img_bigger.show()
