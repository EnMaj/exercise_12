from math import pi


class GeometricObject:
    def __init__(self, x: float = 0.0, y: float = 0.0, color: str = 'black', filled: bool = False):
        if isinstance(x, float) and isinstance(y, float):
            self.__x = x
            self.__y = y
        elif isinstance(x, int) and isinstance(y, int):
            self.__x = float(x)
            self.__y = float(y)
        else:
            print('ошибка')
        self.color = color
        self.filled = filled

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_color(self):
        return self.color

    def is_filled(self):
        return self.filled

    def set_coordinate(self, x: float, y: float):
        if isinstance(x, float) and isinstance(y, float):
            self.__x = x
            self.__y = y
        elif isinstance(x, int) and isinstance(y, int):
            self.__x = float(x)
            self.__y = float(y)
        else:
            pass

    def set_color(self, color: str):
        if isinstance(color, str):
            self.color = color
        else:
            pass

    def set_filled(self, state):
        if isinstance(state, bool):
            self.filled = state
        else:
            pass

    def __str__(self):
        return f'({self.__x},{self.__y})\n' \
               f'color: {self.color}\n' \
               f'filled: {self.filled}'

    def __repr__(self):
        return f'({int(self.__x)},{int(self.__y)}) {self.color} {"filled" if self.filled else "not filled"}'


class Circle(GeometricObject):
    def __init__(self, x: float = 0.0, y: float = 0.0, radius: float = 0.0, color: str = 'black', filled: bool = False):
        super().__init__(x, y, color, filled)
        if isinstance(radius, float):
            if radius >= 0:
                self.__radius = radius
            else:
                self.__radius = 0.0
        elif isinstance(radius, int):
            if radius >= 0:
                self.__radius = float(radius)
            else:
                self.__radius = 0.0
        else:
            print('ошибка')

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius: float):
        if isinstance(radius, float) and radius >= 0:
            self.__radius = radius
        elif isinstance(radius, int) and radius >= 0:
            self.__radius = float(radius)
        else:
            pass

    @radius.getter
    def radius_getter(self):
        return self.__radius

    def get_diametr(self):
        return 2 * self.__radius

    def get_perimetr(self):
        return 2 * pi * self.__radius

    def get_area(self):
        return pi * self.__radius ** 2

    def __str__(self):
        return f'radius: {self.__radius}\n' \
               f'{super().__str__()}'

    def __repr__(self):
        return f' radius:  {int(self.__radius)} {super().__repr__()}'


class Rectangle(GeometricObject):
    def __init__(self, x: float = 0.0, y: float = 0.0, width: float = 0.0, height: float = 0.0, color: str = 'black',
                 filled: bool = False):
        super().__init__(x, y, color, filled)
        if isinstance(width, float):
            if width >= 0:
                self.width = width
            else:
                self.width = 0.0
        elif isinstance(width, int):
            if width >= 0:
                self.width = float(width)
            else:
                self.width = 0.0
        else:
            print('ошибка')

        if isinstance(height, float):
            if height >= 0:
                self.height = height
            else:
                self.height = 0.0
        elif isinstance(height, int):
            if height >= 0:
                self.height = float(height)
            else:
                self.height = 0.0
        else:
            print('ошибка')

    def set_width(self, value: float):
        if isinstance(value, float) and value >= 0:
            self.width = value
        elif isinstance(value, int) and value >= 0:
            self.width = float(value)
        else:
            pass

    def set_height(self, value: float):
        if isinstance(value, float) and value >= 0:
            self.height = value
        elif isinstance(value, int) and value >= 0:
            self.height = float(value)
        else:
            pass

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimetr(self):
        return 2 * self.width + 2 * self.height

    def __str__(self):
        return f'width: {self.width}\n' \
               f'height: {self.height}\n' \
               f'{super().__str__()}'

    def __repr__(self):
        return f'width: {int(self.width)} height: {int(self.height)} {super().__repr__()}'


point = GeometricObject()
print(point)
print()
point.set_coordinate(-4, 9)
print(point.get_x())
print(point.get_y())
point.set_color('red')
print(point.get_color())
point.set_filled(True)
print(point.is_filled())
print()
print(point)
print()
point_2 = GeometricObject(8, -4, 'blue', True)
print(point_2)
print()
circle = Circle()
print(circle)
print()
circle.radius = -34
print(circle.radius)
circle.radius = 12
print(circle.radius)
print()
circle_2 = Circle(3, -100, 20, 'green', True)
print(circle_2)
print()
circle_2.set_color('grey')
print(circle_2.get_color())
print()
print(circle_2.get_area())
print(circle_2.get_perimetr())
print(circle_2.get_diametr())
print()
circle_3 = Circle(90, -84, -223, 'pink')
print(circle_3)
print()
rectangle = Rectangle()
print(rectangle)
print()
rectangle.set_coordinate(11, 29)
rectangle.set_color('yellow')
rectangle.set_width(-10)
rectangle.set_height(20)
print(rectangle)
print()
rectangle.set_width(100)
print(rectangle.get_width())
print(rectangle.get_height())
print()
print(rectangle.get_area())
print(rectangle.get_perimetr())
print()
rectangle_2 = Rectangle(10, 20, 30, -40, 'brown', True)
print(rectangle_2)
print()
figures = []
figures.append(point)
figures.append(circle_2)
figures.append(rectangle)
print(figures)