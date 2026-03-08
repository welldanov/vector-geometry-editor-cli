import math

from shapes import Shape
from shapes import Point


class Circle(Shape):
    def __init__(self, *, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius

    def __str__(self):
        return f"Circle(CENTER={self.center}, RADIUS={self.radius})"

    def length(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def get_center(self):
        return self.center

    def translate(self, dx: float, dy: float):
        self.center.translate(dx, dy)
