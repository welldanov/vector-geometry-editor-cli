import math

from shapes import Shape
from shapes import Point


class Segment(Shape):
    def __init__(self, *, point1: Point, point2: Point):
        self.point1: Point = point1
        self.point2: Point = point2

    def __str__(self):
        return f"Segment({self.point1} -> {self.point2})"

    def length(self):
        return math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)

    def get_center(self):
        return Point(x=(self.point1.x + self.point2.x) / 2, y=(self.point1.y + self.point2.y) / 2)

    def translate(self, dx: float, dy: float):
        self.point1.translate(dx, dy)
        self.point2.translate(dx, dy)
