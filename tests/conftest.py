import pytest
from manager import ShapeManager


@pytest.fixture
def manager():
    return ShapeManager()
