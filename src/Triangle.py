from src.Figure import Figure, ImpossibleFigureError
from math import sqrt


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        self.validate_args(side_a, side_b, side_c)
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def validate_args(self, side_a, side_b, side_c):
        if not all([side_a + side_b > side_c, side_b + side_c > side_a, side_c + side_a > side_b]):
            raise ImpossibleFigureError(f'Cannot create {self.__class__.__name__} with sides: {side_a, side_b, side_c}')

    @property
    def area(self):
        half_meter = self.perimeter / 2
        return sqrt(
            half_meter * ((half_meter - self.__side_a) * (half_meter - self.__side_b) * (half_meter - self.__side_c))
        )

    @property
    def perimeter(self):
        return sum([self.__side_a, self.__side_b, self.__side_c])
