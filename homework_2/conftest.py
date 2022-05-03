import pytest

from homework_2.src.Triangle import Triangle
from homework_2.src.Square import Square
from homework_2.src.Rectangle import Rectangle
from homework_2.src.Circle import Circle

from homework_2.tests.FakeFigure import FakeFigure


@pytest.fixture()
def create_triangle():
    triangle = Triangle(13, 14, 15)
    yield triangle
    del triangle


@pytest.fixture()
def create_square():
    square = Square(10)
    yield square
    del square


@pytest.fixture()
def create_rectangle():
    rectangle = Rectangle(5, 8)
    yield rectangle
    del rectangle


@pytest.fixture()
def create_circle():
    circle = Circle(8)
    yield circle
    del circle


@pytest.fixture()
def create_fake_figure():
    fake_figure = FakeFigure(fake_name="Triangle", some_side=8)
    yield fake_figure
    del fake_figure
