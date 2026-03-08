import math
from typing import Dict, Callable, List

from utils import is_number


def validate_point(parts: List[str]) -> None:
    if len(parts) != 4:
        raise ValueError("Usage: create point <X> <Y>")

    x, y = parts[2], parts[3]

    if not is_number(x) or not is_number(y):
        raise ValueError(f"<X='{x}'> and <Y='{y}'> must be numbers")


def validate_segment(parts: List[str]) -> None:
    if len(parts) != 6:
        raise ValueError("Usage: create segment <X1> <Y1> <X2> <Y2>")

    x1, y1, x2, y2 = parts[2], parts[3], parts[4], parts[5]

    if not is_number(x1) or not is_number(y1) or not is_number(x2) or not is_number(y2):
        raise ValueError(f"<X1='{x1}', Y1='{y1}', X2='{x2}', Y2='{y2}'> must be numbers")

    if math.isclose(float(x1), float(x2)) and math.isclose(float(y1), float(y2)):
        raise ValueError(f"Coordinates must be different")


def validate_circle(parts: List[str]) -> None:
    if len(parts) != 5:
        raise ValueError("Usage: create circle <X> <Y> <RADIUS>")

    x, y, radius = parts[2], parts[3], parts[4]

    if not is_number(x) or not is_number(y) or not is_number(radius) or float(radius) <= 0:
        raise ValueError(f"<X='{x}', Y='{y}'> must be numbers, <RADIUS='{radius}'> must be a positive number")


def validate_square(parts: List[str]) -> None:
    if len(parts) != 5:
        raise ValueError("Usage: create square <X> <Y> <SIDE>")

    x, y, side = parts[2], parts[3], parts[4]

    if not is_number(x) or not is_number(y) or not is_number(side) or float(side) <= 0:
        raise ValueError(f"<X='{x}', Y='{y}'> must be numbers, <SIDE='{side}'> must be a positive number")


shapes: Dict[str, Callable] = {
    "point": validate_point,
    "segment": validate_segment,
    "circle": validate_circle,
    "square": validate_square,
}
