from handlers import main_handler


def test_create_point_handler(manager):
    result = main_handler("create", ["point", "1", "2"], manager)

    assert "Success" in result
    assert "Point" in result


def test_list_handler_empty(manager):
    result = main_handler("list", [], manager)

    assert result == "No shapes created yet"


def test_list_handler_with_shapes(manager):
    main_handler("create", ["point", "1", "2"], manager)

    result = main_handler("list", [], manager)

    assert "Point" in result


def test_delete_handler(manager):
    main_handler("create", ["point", "1", "2"], manager)

    result = main_handler("delete", ["1"], manager)

    assert "deleted" in result


def test_area_handler(manager):
    main_handler("create", ["circle", "0", "0", "1"], manager)

    result = main_handler("area", ["1"], manager)

    assert "area" in result


def test_perimeter_handler(manager):
    main_handler("create", ["square", "0", "0", "2"], manager)

    result = main_handler("perimeter", ["1"], manager)

    assert "perimeter" in result


def test_distance_handler(manager):
    main_handler("create", ["point", "0", "0"], manager)
    main_handler("create", ["point", "3", "4"], manager)

    result = main_handler("distance", ["1", "2"], manager)

    assert "5" in result


def test_translate_handler(manager):
    main_handler("create", ["point", "1", "1"], manager)

    result = main_handler("translate", ["1", "2", "3"], manager)

    assert "moved" in result
