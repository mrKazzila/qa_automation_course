from math import pi

from .Figure import Figure, ImpossibleFigureError


class Circle(Figure):
    def __init__(self, radius: float):
        self.validate_args(radius=radius)
        self.__radius: float = radius

        super().__init__()

    def validate_args(self, radius: float):
        if radius <= 0:
            raise ImpossibleFigureError(f'Cannot create {self.__class__.__name__} with radius: {radius}')

    @property
    def area(self) -> float:
        return pi * (self.__radius ** 2)

    @property
    def perimeter(self) -> float:
        return 2 * pi * self.__radius
