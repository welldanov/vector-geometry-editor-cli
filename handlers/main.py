from typing import List, Dict, Callable

from handlers.system import help_handler
from handlers.create import create_handler
from handlers.geometry import (
    list_handler,
    delete_handler,
    length_handler,
    area_handler,
    perimeter_handler,
    distance_handler,
    translate_handler,
    compare_handler,
)

from manager import ShapeManager


def main_handler(command: str, args: List[str], manager: ShapeManager) -> str:
    if command == "exit":
        raise SystemExit("CLI is closed")

    return handlers[command](args, manager)


handlers: Dict[str, Callable] = {
    "create": create_handler,
    "list": list_handler,
    "delete": delete_handler,
    "length": length_handler,
    "area": area_handler,
    "perimeter": perimeter_handler,
    "distance": distance_handler,
    "translate": translate_handler,
    "compare": compare_handler,
    "help": help_handler,
}
