class FakeFigure:
    def __init__(self, fake_name: str, some_side: float):
        self.name = fake_name
        self.some_side = some_side

    @property
    def area(self) -> float:
        return self.some_side ** 2
