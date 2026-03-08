from typing import List

from manager import ShapeManager


def list_handler(_, manager: ShapeManager) -> str:
    shapes = manager.list()

    if not shapes:
        return "No shapes created yet"

    lines = [f"{shape_id}: {shape}" for shape_id, shape in shapes.items()]
    return "\n".join(lines)


def delete_handler(args: List[str], manager: ShapeManager) -> str:
    shape_id = int(args[0])
    shape_type = manager.get_type(shape_id=shape_id)

    manager.delete(shape_id=shape_id)
    return f"{shape_type} <{shape_id}> was deleted"


def length_handler(args: List[str], manager: ShapeManager) -> str:
    shape_id = int(args[0])
    length = manager.length(shape_id=shape_id)
    return f"{manager.get_type(shape_id=shape_id)} <{shape_id}> length: {length} ea."


def area_handler(args: List[str], manager: ShapeManager) -> str:
    shape_id = int(args[0])
    area = manager.area(shape_id=shape_id)
    return f"{manager.get_type(shape_id=shape_id)} <{shape_id}> area: {area} ea."


def perimeter_handler(args: List[str], manager: ShapeManager) -> str:
    shape_id = int(args[0])
    perimeter = manager.perimeter(shape_id=shape_id)
    return f"{manager.get_type(shape_id=shape_id)} <{shape_id}> perimeter: {perimeter} ea."


def distance_handler(args: List[str], manager: ShapeManager) -> str:
    shape_id1 = int(args[0])
    shape_id2 = int(args[1])

    distance = manager.distance(shape_id1=shape_id1, shape_id2=shape_id2)
    shape1 = manager.get_type(shape_id=shape_id1)
    shape2 = manager.get_type(shape_id=shape_id2)

    return f"Distance between {shape1} <{shape_id1}> and {shape2} <{shape_id2}>: {distance} ea."


def translate_handler(args: List[str], manager: ShapeManager) -> str:
    shape_id = int(args[0])
    dx = float(args[1])
    dy = float(args[2])

    manager.translate(shape_id=shape_id, dx=dx, dy=dy)
    return f"{manager.get_type(shape_id=shape_id)} <{shape_id}> moved by ({dx}, {dy})"


def compare_handler(args: List[str], manager: ShapeManager) -> str:
    shape_id1 = int(args[0])
    shape_id2 = int(args[1])

    b_id, s_id, diff = manager.compare(shape_id1=shape_id1, shape_id2=shape_id2)

    bigger = manager.get_type(shape_id=b_id)
    smaller = manager.get_type(shape_id=s_id)

    if not diff:
        return f"{bigger} <{b_id}> and {smaller} <{s_id}> are equal in area"

    return f"{bigger} <{b_id}> is bigger than {smaller} <{s_id}> by: {diff} ea."
