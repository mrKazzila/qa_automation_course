from homework_2.src.Figure import Figure, ImpossibleFigureError


class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.validate_args(side)
        self.__side = side

    def validate_args(self, side):
        if side <= 0:
            raise ImpossibleFigureError(f'Cannot create {self.__class__.__name__} with side: {side}')

    @property
    def area(self):
        return self.__side ** 2

    @property
    def perimeter(self):
        return 4 * self.__side
