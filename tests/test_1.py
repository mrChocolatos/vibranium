import pytest

from src.figure import Figure
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize("figure, area",
                         [(Triangle(13, 14, 15), 84), (Square(5), 25),
                          (Circle(10), 314), (Rectangle(4, 5), 20)])
def test_for_correct_area(figure, area):
    assert figure.area == area


@pytest.mark.parametrize("figure, perimeter",
                         [(Triangle(13, 14, 15), 42), (Square(5), 20),
                          (Circle(10), 31), (Rectangle(4, 5), 18)])
def test_for_correct_perimeter(figure, perimeter):
    assert figure.get_perimeter == perimeter


@pytest.mark.parametrize("a, b, c", [(13, 14, -15), (3, 4, -5), (4, -5, 6), (-1, 2, 2)])
def test_for_correct_sides_triangle(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


def test_for_correct_sides_square():
    with pytest.raises(ValueError):
        Square(-5)


def test_for_correct_radius_circle():
    with pytest.raises(ValueError):
        Circle(-10)


def test_for_correct_sides_rectangle():
    with pytest.raises(ValueError):
        Rectangle(4, -5)


@pytest.mark.parametrize("figure, figure_to_add, result_area",
                         [(Triangle(13, 14, 15), Square(5), 109),
                          (Circle(10), Rectangle(4, 5), 334)])
def test_add_figure_area(figure: Figure, figure_to_add: Figure, result_area):
    assert figure.add_area(figure_to_add) == result_area


@pytest.mark.parametrize("figure", [(Triangle(13, 14, 15)), (Square(5)), (Circle(10)), (Rectangle(4, 5))])
def test_add_figure_area_negative(figure: Figure):
    with pytest.raises(AssertionError):
        assert figure.add_area(4)
