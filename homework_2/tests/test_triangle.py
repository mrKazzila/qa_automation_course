import pytest
from src.Figure import Figure, ImpossibleFigureError
from src.Triangle import Triangle


@pytest.mark.smoke
def test_triangle_init(create_triangle):
    assert isinstance(create_triangle, Figure) is True


@pytest.mark.smoke
def test_create_triangle(create_triangle):
    assert create_triangle.name == "Triangle"


@pytest.mark.smoke
def test_triangle_perimeter(create_triangle):
    assert create_triangle.perimeter == 42


@pytest.mark.smoke
def test_triangle_area(create_triangle):
    assert create_triangle.area == 84


@pytest.mark.smoke
def test_triangle_add_area_fake_figure(create_triangle, create_fake_figure):
    with pytest.raises(ValueError):
        create_triangle.add_area(create_fake_figure)


@pytest.mark.smoke
def test_triangle_add_area_rectangle(create_triangle, create_rectangle):
    assert create_triangle.add_area(create_rectangle) == 124


def test_triangle_add_area_square(create_triangle, create_square):
    assert create_triangle.add_area(create_square) == 184


def test_triangle_add_area_circle(create_triangle, create_circle):
    assert create_triangle.add_area(create_circle) == 285.06192982974676


def test_fake_triangle_init(create_fake_figure):
    assert isinstance(create_fake_figure, Triangle) is False


def test_create_triangle_bad_side():
    with pytest.raises(ImpossibleFigureError):
        Triangle(side_a=13, side_b=-14, side_c=-15)


def test_create_triangle_sides_is_0():
    with pytest.raises(ImpossibleFigureError):
        Triangle(side_a=0, side_b=0, side_c=0)
