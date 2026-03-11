import pytest
from validators import cmd_validator


def test_valid_create_point():
    command, args = cmd_validator("create point 1 2")

    assert command == "create"
    assert args == ["point", "1", "2"]


def test_valid_delete():
    command, args = cmd_validator("delete 1")

    assert command == "delete"
    assert args == ["1"]


def test_valid_distance():
    command, args = cmd_validator("distance 1 2")

    assert command == "distance"
    assert args == ["1", "2"]


def test_invalid_command():
    with pytest.raises(ValueError):
        cmd_validator("unknown command")


def test_create_without_shape():
    with pytest.raises(ValueError):
        cmd_validator("create")


def test_invalid_shape():
    with pytest.raises(ValueError):
        cmd_validator("create triangle 1 2 3")


def test_invalid_id():
    with pytest.raises(ValueError):
        cmd_validator("delete abc")


def test_translate_invalid_args():
    with pytest.raises(ValueError):
        cmd_validator("translate 1 a b")


def test_segment_same_points():
    with pytest.raises(ValueError):
        cmd_validator("create segment 1 1 1 1")
