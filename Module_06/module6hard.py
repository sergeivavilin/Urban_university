from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color: tuple[int, int, int], *sides):
        self.filled = False
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1 for _ in range(self.sides_count)]

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_color(self, r, g, b):
        return all(isinstance(color, int) and 0 <= color <= 255 for color in (r, g, b))

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        # Проверяем, что количество сторон совпадает с sides_count и они все положительные
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        # Perimetr
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__radius = round(len(self) / (2 * pi), 2)

    def get_square(self):
        return round(pi * self.__radius ** 2, 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.__sides
        p = (a + b + c) / 2

        # Площадь треугольника по формуле Герона
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        return round(s, 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):

        if len(sides) != 1:
            sides = tuple(1 for _ in range(self.sides_count))
        else:
            sides = tuple(sides[0] for _ in range(self.sides_count))
        super().__init__(color, *sides)

    def get_volume(self):
        # Объём куба
        return round(self.get_sides()[0] ** 3, 2)


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())

    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
