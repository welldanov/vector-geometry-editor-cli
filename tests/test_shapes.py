import math
from shapes import Point, Segment, Circle, Square


def test_point_translate():
    p = Point(x=1, y=2)

    p.translate(3, -1)

    assert p.x == 4
    assert p.y == 1


def test_point_center():
    p = Point(x=5, y=7)

    center = p.get_center()

    assert center.x == 5
    assert center.y == 7


def test_segment_length():
    s = Segment(
        point1=Point(x=0, y=0),
        point2=Point(x=3, y=4)
    )

    assert s.length() == 5


def test_segment_center():
    s = Segment(
        point1=Point(x=0, y=0),
        point2=Point(x=4, y=4)
    )

    c = s.get_center()

    assert c.x == 2
    assert c.y == 2


def test_segment_translate():
    s = Segment(
        point1=Point(x=1, y=1),
        point2=Point(x=2, y=2)
    )

    s.translate(1, 1)

    assert s.point1.x == 2
    assert s.point1.y == 2

    assert s.point2.x == 3
    assert s.point2.y == 3


def test_circle_area():
    c = Circle(center=Point(x=0, y=0), radius=1)

    assert math.isclose(c.area(), math.pi)


def test_circle_length():
    c = Circle(center=Point(x=0, y=0), radius=2)

    assert math.isclose(c.length(), 2 * math.pi * 2)


def test_circle_translate():
    c = Circle(center=Point(x=1, y=1), radius=2)

    c.translate(3, 4)

    assert c.center.x == 4
    assert c.center.y == 5


def test_square_area():
    s = Square(center=Point(x=0, y=0), side=5)

    assert s.area() == 25


def test_square_perimeter():
    s = Square(center=Point(x=0, y=0), side=4)

    assert s.perimeter() == 16


def test_square_translate():
    s = Square(center=Point(x=1, y=1), side=3)

    s.translate(2, 3)

    assert s.center.x == 3
    assert s.center.y == 4
