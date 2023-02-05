import pytest
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from tests.FakeFigure import FakeFigure


@pytest.fixture()
def create_triangle():
    triangle = Triangle(side_a=13, side_b=14, side_c=15)
    yield triangle
    del triangle


@pytest.fixture()
def create_square():
    square = Square(side=10)
    yield square
    del square


@pytest.fixture()
def create_rectangle():
    rectangle = Rectangle(side_a=5, side_b=8)
    yield rectangle
    del rectangle


@pytest.fixture()
def create_circle():
    circle = Circle(radius=8)
    yield circle
    del circle


@pytest.fixture()
def create_fake_figure():
    fake_figure = FakeFigure(fake_name="Triangle", some_side=8)
    yield fake_figure
    del fake_figure
