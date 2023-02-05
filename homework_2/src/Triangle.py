from math import sqrt

from .Figure import Figure, ImpossibleFigureError


class Triangle(Figure):

    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.validate_args(side_a=side_a, side_b=side_b, side_c=side_c)
        self.__side_a: float = side_a
        self.__side_b: float = side_b
        self.__side_c: float = side_c

        super().__init__()

    def validate_args(self, side_a: float, side_b: float, side_c: float):
        if not all([side_a + side_b > side_c, side_b + side_c > side_a, side_c + side_a > side_b]):
            raise ImpossibleFigureError(f'Cannot create {self.__class__.__name__} with sides: {side_a, side_b, side_c}')

    @property
    def area(self) -> float:
        half_meter = self.perimeter / 2
        return sqrt(
            half_meter * ((half_meter - self.__side_a) * (half_meter - self.__side_b) * (half_meter - self.__side_c)),
        )

    @property
    def perimeter(self) -> float:
        return sum([self.__side_a, self.__side_b, self.__side_c])
