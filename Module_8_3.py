class Car:

    def __init__(self, model, vin_number, car_numbers):
        self.model = model
        self.__vin = None
        self.__is_valid_vin(vin_number)
        self.__numbers = None
        self.__is_valid_numbers(car_numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип данных vin номера')
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Некорректный диапазон для vin номера')
        else:
            self.__vin = vin_number
            return True

    def __is_valid_numbers(self, car_numbers):
        if not isinstance(car_numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных номера автомобиля')
        elif len(car_numbers) != 6:
            raise IncorrectCarNumbers('Некорректная длина номера автомобиля')
        else:
            self.__numbers = car_numbers
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    second_ = Car('Model2_', '3000000', 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second_.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

try:
    third_ = Car('Model3_', 2020202, 234.123)
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third_.model} успешно создан')
