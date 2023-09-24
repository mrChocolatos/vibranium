import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Trinagle import Triangle


def test_for_correct_area():
    triangle = Triangle(13, 14, 15)
    square = Square(5)
    circle = Circle(10)
    rectangle = Rectangle(4, 5)

    assert triangle.get_area == 84
    assert square.get_area == 25
    assert circle.get_area == 314
    assert rectangle.get_area == 20


def test_for_correct_perimeter():
    triangle = Triangle(13, 14, 15)
    square = Square(5)
    circle = Circle(10)
    rectangle = Rectangle(4, 5)

    assert triangle.get_perimeter == 42
    assert square.get_perimeter == 20
    assert circle.get_perimeter == 31
    assert rectangle.get_perimeter == 18


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


def test_add_figure_area():
    triangle = Triangle(13, 14, 15)
    square = Square(5)
    circle = Circle(10)
    rectangle = Rectangle(4, 5)
    assert triangle.add_area(square) == 109
    assert circle.add_area(rectangle) == 334


def test_add_figure_area_negative():
    triangle = Triangle(13, 14, 15)
    square = Square(5)
    circle = Circle(10)
    rectangle = Rectangle(4, 5)
    with pytest.raises(AssertionError):
        assert triangle.add_area(5)
    with pytest.raises(AssertionError):
        assert square.add_area("asd")
    with pytest.raises(AssertionError):
        assert circle.add_area({"asd": 12})
    with pytest.raises(AssertionError):
        assert rectangle.add_area(MemoryError)
