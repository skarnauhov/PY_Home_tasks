first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

set_1 = {first, second, third}

if len(set_1) == 1:
    print('3')
elif len(set_1) == 2:
    print('2')
else:
    print('0')