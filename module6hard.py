import math


class Figure:
    sides_count = 0

    def __init__(self, __color,  *__sides, filled=True):
        self.__color = [*__color]
        self.__sides = [*__sides]
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.filled = False
        self.r = r
        self.g = g
        self.b = b
        if isinstance(self.r, int) and 0 <= self.r <= 250:
            if isinstance(self.g, int) and 0 <= self.g <= 250:
                if isinstance(self.b, int) and 0 <= self.b <= 250:
                    self.filled = True
        return self.filled

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color[0] = self.r
            self.__color[1] = self.g
            self.__color[2] = self.b
        return self.__color

    def __is_valid_sides(self, *new_sides):
        new_sides = [*new_sides]
        Figure.sides_count = len(self.__sides)
        if len(new_sides) == Figure.sides_count:
            for i in self.__sides:
                if isinstance(i, int):
                    return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimeter = 0
        for i in self.__sides:
            perimeter += i
        return perimeter

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *args):
        if len(args) == Circle.sides_count:
            super().__init__(__color, *args)
        else:
            args = [1]
            super().__init__(__color, *args)

    def get_radius(self):
        __radius = self.__len__()/(2*math.pi)
        return __radius

    def get_square(self):
        self.__len__()**2/(4*math.pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *args):
        if len(args) == Triangle.sides_count:
            super().__init__(__color, *args)
        else:
            args = [1]*Triangle.sides_count
            super().__init__(__color, *args)

    def get_square(self):
        pp = self.__len__()/2
        sd = self.get_sides()
        return (pp*(pp-sd[0])*(pp-sd[1])*(pp-sd[2]))**0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *args):
        if len(args) == Cube.sides_count:
            super().__init__(__color, *args)
        elif len(args) == 1:
            args = args * Cube.sides_count
            super().__init__(__color, *args)
        else:
            args = [1]*Cube.sides_count
            super().__init__(__color, *args)

    def get_volume(self):
        sd = self.get_sides()
        return sd[0]**3


# Проверка на количество переданных сторон:
circle1 = Circle((200, 200, 100), 10, 15, 6)
print(circle1.get_sides())
triangle1 = Triangle((250, 0, 100), 10, 6)
print(triangle1.get_sides())
cube1 = Cube((200, 200, 100), 9)
print(cube1.get_sides())

# Проверка цвета сторон:
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение цветов:
# изменится:
circle1.set_color(55, 66, 77)
print(circle1.get_color())
# не изменится:
cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон:
print(circle1.get_sides())
print(cube1.get_sides())
# изменится:
circle1.set_sides(15)
print(circle1.get_sides())
# не изменится:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка площади (треугольника):
triangle1.set_sides(3, 4, 5)
print(triangle1.get_square())

# Проверка объёма (куба):
print(cube1.get_volume())
