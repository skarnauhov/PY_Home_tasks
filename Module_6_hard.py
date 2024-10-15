from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides, filled=False):

        if isinstance(__color, (tuple, list)) and len(__color) == 3:
            self.__color = list(__color)
        else:
            self.__color = [0, 0, 0]

        self.__s = []  # вспомогательный список, который после создания ещё раз анализируется на предмет соответствия подклассам
        self.__sides = []
        for side in __sides:
            if isinstance(side, int):
                self.__s.append(side)
        if len(self.__s) == 1 and self.sides_count == 12:
            for s in range(self.sides_count):
                self.__sides.append(self.__s[0])  # куб
        elif len(self.__s) != self.sides_count:
            for s in range(self.sides_count):
                self.__sides.append(1)  # фигуры со стороной 1 при нарушении условий
        else:
            self.__sides = self.__s  # круг, треугольник и родительский класс

        self.filled = filled

    def get_color(self):
        return [self.__color[0], self.__color[1], self.__color[2]]

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *new_sides):
        sides_are_ok = True
        for side in new_sides:
            if isinstance(side, int) and side > 0:
                sides_are_ok = True
            else:
                sides_are_ok = False
        if sides_are_ok and len(new_sides) == self.sides_count:
            return True
        elif sides_are_ok and len(new_sides) == 1 and self.sides_count == 12:
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if len(new_sides) == 1 and self.sides_count == 12:
                self.__sides = []
                for count in range(self.sides_count):
                    self.__sides.append(new_sides[0])
            else:
                self.__sides = list(new_sides)

    def __len__(self): # сумма длин сторон
        perimetr = 0
        for count in range(self.sides_count):
            perimetr += self.__sides[count]
        return perimetr  # для трехмерных фигур не применимо


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides, filled=False):
        super().__init__(__color, *__sides, filled=filled)
        self.__sides = self.get_sides()
        self.__radius = self.__sides[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides, filled=False):
        super().__init__(__color, *__sides, filled=filled)
        self.__sides = self.get_sides()

    def get_square(self):
        a = self.__sides[0]
        b = self.__sides[1]
        c = self.__sides[2]
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides, filled=False):
        super().__init__(__color, *__sides, filled=filled)
        self.__sides = self.get_sides()

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


# circle1 = Figure( [200, 200, 200], 10, 'f', 6, filled = True) # (Цвет, стороны)
# circle2 = Circle((200, 200, 200), 20, filled = True) # (Цвет, стороны)
# triangle= Triangle((200, 200, 200), 10, 5, filled = True) # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
#
# print(circle1.sides_count, circle2.sides_count, triangle.sides_count, cube1.sides_count)
# #print(circle1.__color)
#
# print(circle1.get_color())
# circle1.set_color(0, 100, 100)
# print(circle1.get_color())
#
# print(cube1.get_sides(), triangle.get_sides())
#
# cube1.set_sides(7 )
# triangle.set_sides(2, 2, 2)
#
# print(cube1.get_sides(), triangle.get_sides())
#
# print(circle2.len(), triangle.len(), cube1.len())
#
# print(circle2.get_square(), triangle.get_square())
#
# triangle2 = Triangle((25, 25, 25), 5, 'f', 6, 7)
#
# print(triangle2.get_sides())
