from src.Figure import Figure, ImpossibleFigureError
from math import pi


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.validate_args(radius)
        self.__radius = radius

    def validate_args(self, radius):
        if radius <= 0:
            raise ImpossibleFigureError(f'Cannot create {self.__class__.__name__} with radius: {radius}')

    @property
    def area(self):
        return pi * (self.__radius ** 2)

    @property
    def perimeter(self):
        return 2 * pi * self.__radius
