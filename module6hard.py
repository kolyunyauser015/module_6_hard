import math


class Figure:
    sides_count = 0

    def __init__(self, color,  *sides, filled=True):
        self.__color = [*color]
        if len(sides) != self.sides_count and self.sides_count == 0:
            self.__sides = []
        else:
            self.__sides = [*sides]
        self.filled = filled

    def get_color(self):
        self.__is_valid_color(*self.__color)
        if self.filled:
            return self.__color
        else:
            self.__color = [0, 0, 0]
            return self.__color

    def __is_valid_color(self, r, g, b):
        self.filled = False
        self.r = r
        self.g = g
        self.b = b
        if isinstance(self.r, int) and 0 <= self.r <= 255:
            if isinstance(self.g, int) and 0 <= self.g <= 255:
                if isinstance(self.b, int) and 0 <= self.b <= 255:
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
        if len(new_sides) == len(self.__sides):
            for i in new_sides:
                if isinstance(i, int):
                    return True
        else:
            return False

    def get_sides(self):
        if len(self.__sides) == self.sides_count:
            return self.__sides
        elif len(self.__sides) == 1:
            self.__sides = self.__sides * self.sides_count
            return self.__sides
        else:
            self.__sides = [1] * self.sides_count
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

    def __init__(self, color, *sides, __radius=0):
        super().__init__(color, *sides)
        self.color = self.get_sides()
        self.sides = self.get_sides()
        self.__radius = __radius

    def get_radius(self):
        self.__radius = self.sides[0]/(2*math.pi)
        return self.__radius

    def get_square(self):
        self.__radius = self.get_radius()
        return math.pi*self.__radius**2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.color = self.get_sides()
        self.sides = self.get_sides()

    def get_square(self):
        pp = self.__len__()/2
        sd = self.get_sides()
        return (pp*(pp-sd[0])*(pp-sd[1])*(pp-sd[2]))**0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.color = self.get_sides()
        self.sides = self.get_sides()

    def get_volume(self):
        sd = self.get_sides()
        return sd[0]**3
