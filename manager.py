import math
from typing import Dict, Tuple, Optional

from shapes import Shape, Point, Segment, Circle, Square


class ShapeManager:
    def __init__(self) -> None:
        self.shapes: Dict[int, Shape] = {}
        self.id: int = 1

    @staticmethod
    def _round_to_two(*, number: float) -> float:
        return round(number, 2)

    def _get_shape(self, *, shape_id: int) -> Shape:
        shape = self.shapes.get(shape_id)

        if not shape:
            raise ValueError(f"Shape with id {shape_id} doesn't exist")

        return shape

    def _add(self, *, shape: Shape) -> int:
        current_id = self.id
        self.shapes[current_id] = shape
        self.id += 1
        return current_id

    def get_type(self, *, shape_id: int) -> str:
        return self._get_shape(shape_id=shape_id).__class__.__name__

    def get_details(self, *, shape_id: int) -> str:
        return str(self._get_shape(shape_id=shape_id))

    def create_point(self, *, x: float, y: float) -> int:
        return self._add(shape=Point(x=x, y=y))

    def create_segment(self, *, x1: float, y1: float, x2: float, y2: float) -> int:
        return self._add(shape=Segment(point1=Point(x=x1, y=y1), point2=Point(x=x2, y=y2)))

    def create_circle(self, *, x: float, y: float, radius: float) -> int:
        return self._add(shape=Circle(center=Point(x=x, y=y), radius=radius))

    def create_square(self, *, x: float, y: float, side: float) -> int:
        return self._add(shape=Square(center=Point(x=x, y=y), side=side))

    def distance(self, *, shape_id1: int, shape_id2: int) -> float:
        shape1 = self._get_shape(shape_id=shape_id1)
        shape2 = self._get_shape(shape_id=shape_id2)

        try:
            center1 = shape1.get_center()
            center2 = shape2.get_center()
        except NotImplementedError as e:
            raise ValueError(e)

        distance = math.sqrt((center2.x - center1.x) ** 2 + (center2.y - center1.y) ** 2)
        return self._round_to_two(number=distance)

    def translate(self, *, shape_id: int, dx: float, dy: float) -> None:
        shape = self._get_shape(shape_id=shape_id)

        try:
            shape.translate(dx, dy)
        except NotImplementedError as e:
            raise ValueError(e)

    def compare(self, *, shape_id1: int, shape_id2: int) -> Tuple[int, int, Optional[float]]:
        shape1 = self._get_shape(shape_id=shape_id1)
        shape2 = self._get_shape(shape_id=shape_id2)

        area1, area2 = shape1.area(), shape2.area()
        diff = self._round_to_two(number=abs(area1 - area2))

        if math.isclose(area1, area2):
            return shape_id1, shape_id2, None

        if area1 > area2:
            return shape_id1, shape_id2, diff

        return shape_id2, shape_id1, diff

    def length(self, *, shape_id: int) -> float:
        shape = self._get_shape(shape_id=shape_id)

        try:
            value = shape.length()
        except NotImplementedError as e:
            raise ValueError(e)

        return self._round_to_two(number=value)

    def area(self, *, shape_id: int) -> float:
        shape = self._get_shape(shape_id=shape_id)

        try:
            value = shape.area()
        except NotImplementedError as e:
            raise ValueError(e)

        return self._round_to_two(number=value)

    def perimeter(self, *, shape_id: int) -> float:
        shape = self._get_shape(shape_id=shape_id)

        try:
            value = shape.perimeter()
        except NotImplementedError as e:
            raise ValueError(e)

        return self._round_to_two(number=value)

    def delete(self, *, shape_id: int) -> None:
        self._get_shape(shape_id=shape_id)
        del self.shapes[shape_id]

    def list(self) -> Dict[int, Shape]:
        return self.shapes
