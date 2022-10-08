from .Figure import Figure, ImpossibleFigureError


class Square(Figure):
    def __init__(self, side: float):
        self.validate_args(side=side)
        self.__side: float = side

        super().__init__()

    def validate_args(self, side: float):
        if side <= 0:
            raise ImpossibleFigureError(f'Cannot create {self.__class__.__name__} with side: {side}')

    @property
    def area(self) -> float:
        return self.__side ** 2

    @property
    def perimeter(self) -> float:
        return 4 * self.__side
