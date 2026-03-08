from typing import TypeAlias, Tuple, Dict, List, Callable

from .shapes import shapes
from utils.is_integer import is_integer
from utils.is_number import is_number

ValidatorType: TypeAlias = Tuple[str, list[str]]


def cmd_validator(command: str) -> ValidatorType:
    parts = command.split()

    keyword = parts[0]

    validator = validators.get(keyword)
    if not validator:
        raise ValueError(f"Unknown command: '{keyword}'. Type 'help' for a list of commands")

    return validator(parts)


def validate_create(parts) -> ValidatorType:
    if len(parts) < 2:
        raise ValueError("Usage: create <SHAPE> <...ARGS>")

    shape = parts[1]
    validate_shape = shapes.get(shape)

    if not validate_shape:
        raise ValueError(f"Shape '{shape}' doesn't exist")

    validate_shape(parts)

    return "create", parts[1:]


def validate_translate(parts: List[str]) -> ValidatorType:
    if len(parts) != 4:
        raise ValueError("Usage: translate <ID> <DX> <DY>")

    shape_id, dx, dy = parts[1], parts[2], parts[3]

    if not is_integer(shape_id) or int(shape_id) < 1 or not is_number(dx) or not is_number(dy):
        raise ValueError(f"<ID='{shape_id}'> must be a positive integer and <DX='{dx}', DY='{dy}'> must be numbers")

    return "translate", parts[1:]


def validate_one_id_command(parts: List[str]) -> ValidatorType:
    command = parts[0]

    if len(parts) != 2:
        raise ValueError(f"Usage: {command} <ID>")

    shape_id = parts[1]
    if not is_integer(shape_id) or int(shape_id) < 1:
        raise ValueError(f"<ID='{shape_id}'> must be a positive integer")

    return command, parts[1:]


def validate_two_id_command(parts: List[str]) -> ValidatorType:
    command = parts[0]

    if len(parts) != 3:
        raise ValueError(f"Usage: {command} <shape ID> <shape ID>")

    shape_id1, shape_id2 = parts[1], parts[2]

    if not is_integer(shape_id1) or int(shape_id1) < 1 or not is_integer(shape_id2) or int(shape_id2) < 1:
        raise ValueError(f"<shape ID='{shape_id1}'> and <shape ID='{shape_id2}'> must be positive integers")

    return command, parts[1:]


def validate_no_args(parts: List[str]) -> ValidatorType:
    command = parts[0]

    if len(parts) != 1:
        raise ValueError(f"Usage: {command}")

    return command, []


validators: Dict[str, Callable] = {
    "create": validate_create,
    "list": validate_no_args,
    "help": validate_no_args,
    "exit": validate_no_args,
    "delete": validate_one_id_command,
    "length": validate_one_id_command,
    "area": validate_one_id_command,
    "perimeter": validate_one_id_command,
    "distance": validate_two_id_command,
    "compare": validate_two_id_command,
    "translate": validate_translate,
}
