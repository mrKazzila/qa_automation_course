import pytest
from homework_2.src.Figure import Figure, ImpossibleFigureError
from homework_2.src.Rectangle import Rectangle


@pytest.mark.smoke
def test_rectangle_init(create_rectangle):
    assert isinstance(create_rectangle, Figure) is True


@pytest.mark.smoke
def test_create_rectangle(create_rectangle):
    assert create_rectangle.name is "Rectangle"


@pytest.mark.smoke
def test_rectangle_perimeter(create_rectangle):
    assert create_rectangle.perimeter == 26


@pytest.mark.smoke
def test_rectangle_area(create_rectangle):
    assert create_rectangle.area == 40


@pytest.mark.smoke
def test_rectangle_add_area_fake_figure(create_rectangle, create_fake_figure):
    with pytest.raises(ValueError):
        create_rectangle.add_area(create_fake_figure)


@pytest.mark.smoke
def test_rectangle_add_area_circle(create_rectangle, create_circle):
    assert create_rectangle.add_area(create_circle) == 241.06192982974676


def test_rectangle_add_area_square(create_rectangle, create_square):
    assert create_rectangle.add_area(create_square) == 140


def test_rectangle_add_area_triangle(create_rectangle, create_triangle):
    assert create_rectangle.add_area(create_triangle) == 124


def test_fake_rectangle_init(create_fake_figure):
    assert isinstance(create_fake_figure, Rectangle) is False


def test_create_rectangle_bad_side():
    with pytest.raises(ImpossibleFigureError):
        Rectangle(13, -14)


def test_create_rectangle_sides_is_0():
    with pytest.raises(ImpossibleFigureError):
        Rectangle(0, 0)
