import pytest

from src.Circle import Circle
from src.Figure import Figure, ImpossibleFigureError


@pytest.mark.smoke
def test_circle_init(create_circle):
    assert isinstance(create_circle, Figure) is True


@pytest.mark.smoke
def test_create_circle(create_circle):
    assert create_circle.name is "Circle"


@pytest.mark.smoke
def test_circle_perimeter(create_circle):
    assert create_circle.perimeter == 50.26548245743669


@pytest.mark.smoke
def test_circle_area(create_circle):
    assert create_circle.area == 201.06192982974676


@pytest.mark.smoke
def test_circle_add_area_fake_figure(create_circle, create_fake_figure):
    with pytest.raises(ValueError):
        create_circle.add_area(create_fake_figure)


@pytest.mark.smoke
def test_circle_add_area_square(create_circle, create_square):
    assert create_circle.add_area(create_square) == 301.06192982974676


def test_circle_add_area_triangle(create_circle, create_triangle):
    assert create_circle.add_area(create_triangle) == 285.06192982974676


def test_circle_add_area_rectangle(create_circle, create_rectangle):
    assert create_circle.add_area(create_rectangle) == 241.06192982974676


def test_fake_circle_init(create_fake_figure):
    assert isinstance(create_fake_figure, Circle) is False


def test_create_circle_bad_radius():
    with pytest.raises(ImpossibleFigureError):
        Circle(radius=-13)


def test_create_circle_radius_is_0():
    with pytest.raises(ImpossibleFigureError):
        Circle(radius=0)
