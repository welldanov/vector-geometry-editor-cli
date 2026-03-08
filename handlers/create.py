from typing import List, Dict, Callable

from manager import ShapeManager


def create_handler(args: List[str], manager: ShapeManager) -> str:
    shape, *shape_args = args
    message = create_handlers[shape](shape_args, manager)
    return f"Success: {message} was created"


def create_point(args: List[str], manager: ShapeManager) -> str:
    x, y = map(float, args)
    shape_id = manager.create_point(x=x, y=y)
    return manager.get_details(shape_id=shape_id)


def create_segment(args: List[str], manager: ShapeManager) -> str:
    x1, y1, x2, y2 = map(float, args)
    shape_id = manager.create_segment(x1=x1, y1=y1, x2=x2, y2=y2)
    return manager.get_details(shape_id=shape_id)


def create_circle(args: List[str], manager: ShapeManager) -> str:
    x, y, radius = map(float, args)
    shape_id = manager.create_circle(x=x, y=y, radius=radius)
    return manager.get_details(shape_id=shape_id)


def create_square(args: List[str], manager: ShapeManager) -> str:
    x, y, side = map(float, args)
    shape_id = manager.create_square(x=x, y=y, side=side)
    return manager.get_details(shape_id=shape_id)


create_handlers: Dict[str, Callable] = {
    "point": create_point,
    "segment": create_segment,
    "circle": create_circle,
    "square": create_square,
}
