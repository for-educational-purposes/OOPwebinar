class Figure:
    def __init__(self, name):
        self.name = name

    def get_area(self):
        pass

    def get_perimeter(self):
        raise NotImplementedError

    def __str__(self):
        return f'Class name: {type(self).__name__}, Instance name: {self.name}'


class Rectangle(Figure):
    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return (self.a + self.b) * 2


class Square(Rectangle):
    def __init__(self, name, a):
        super().__init__(name, a, a)


class Circle(Figure):
    pi = 3.14

    def __init__(self, name, r):
        super().__init__(name)
        self.r = r

    def get_area(self):
        return self.pi * self.r ** 2

    def get_perimeter(self):
        return 2 * Circle.pi * self.r
