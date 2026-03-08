from shapes import Shape
from shapes import Point


class Square(Shape):
    def __init__(self, *, center: Point, side: float):
        self.center: Point = center
        self.side: float = side

    def __str__(self):
        return f"Square(CENTER={self.center}, SIDE={self.side})"

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4

    def get_center(self):
        return self.center

    def translate(self, dx: float, dy: float):
        self.center.translate(dx, dy)
