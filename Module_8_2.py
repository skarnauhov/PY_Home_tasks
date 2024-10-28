def personal_summ(numbers):
    summ = 0
    incorrect_data =0
    for number in numbers:
        try:
            summ += number
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы: {number}')
            incorrect_data += 1
    return (summ, incorrect_data)

def calculate_average(numbers):
    avrg = 0
    try:
        avrg = personal_summ(numbers)[0] / len(numbers)
    except ZeroDivisionError:
        return avrg
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None
    else:
        return avrg

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
print(f'Результат 5: {calculate_average([])}')