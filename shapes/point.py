from typing import Self
from shapes.base import Shape


class Point(Shape):
    def __init__(self, *, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __str__(self):
        return f"Point(X={self.x}, Y={self.y})"

    def get_center(self):
        return self

    def translate(self, dx: float, dy: float):
        self.x += dx
        self.y += dy
