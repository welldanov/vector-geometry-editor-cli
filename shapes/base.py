from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shapes import Point


class Shape(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    def length(self) -> float:
        raise NotImplementedError(f"{self.__class__.__name__} has no length")

    def area(self) -> float:
        raise NotImplementedError(f"{self.__class__.__name__} has no area")

    def perimeter(self) -> float:
        raise NotImplementedError(f"{self.__class__.__name__} has no perimeter")

    def get_center(self) -> "Point":
        raise NotImplementedError(f"{self.__class__.__name__} has no center")

    def translate(self, dx: float, dy: float) -> None:
        raise NotImplementedError(f"{self.__class__.__name__} can't be translated")
