import pytest
from src.Figure import Figure, ImpossibleFigureError
from src.Square import Square


@pytest.mark.smoke
def test_square_init(create_square):
    assert isinstance(create_square, Figure) is True


@pytest.mark.smoke
def test_create_square(create_square):
    assert create_square.name is "Square"


@pytest.mark.smoke
def test_square_perimeter(create_square):
    assert create_square.perimeter == 40


@pytest.mark.smoke
def test_square_area(create_square):
    assert create_square.area == 100


@pytest.mark.smoke
def test_square_add_area_fake_figure(create_square, create_fake_figure):
    with pytest.raises(ValueError):
        create_square.add_area(create_fake_figure)


@pytest.mark.smoke
def test_square_add_area_triangle(create_square, create_triangle):
    assert create_square.add_area(create_triangle) == 184


def test_square_add_area_rectangle(create_square, create_rectangle):
    assert create_square.add_area(create_rectangle) == 140


def test_square_add_area_circle(create_square, create_circle):
    assert create_square.add_area(create_circle) == 301.06192982974676


def test_fake_square_init(create_fake_figure):
    assert isinstance(create_fake_figure, Square) is False


def test_create_square_bad_side():
    with pytest.raises(ImpossibleFigureError):
        Square(-13)


def test_create_square_side_is_0():
    with pytest.raises(ImpossibleFigureError):
        Square(0)
