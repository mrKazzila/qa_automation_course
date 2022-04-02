class FakeFigure:
    def __init__(self, fake_name, some_side):
        self.name = fake_name
        self.some_side = some_side

    @property
    def area(self):
        return self.some_side ** 2
