import pytest


def test_create_point(manager):
    sid = manager.create_point(x=1, y=2)

    assert sid == 1
    assert manager.get_type(shape_id=sid) == "Point"


def test_create_multiple(manager):
    p = manager.create_point(x=0, y=0)
    c = manager.create_circle(x=0, y=0, radius=5)

    shapes = manager.list()

    assert len(shapes) == 2
    assert p in shapes
    assert c in shapes


def test_create_segment_length(manager):
    sid = manager.create_segment(x1=0, y1=0, x2=3, y2=4)

    assert manager.length(shape_id=sid) == 5


def test_circle_area(manager):
    cid = manager.create_circle(x=0, y=0, radius=1)

    area = manager.area(shape_id=cid)

    assert area == round(3.141592653589793, 2)


def test_square_perimeter(manager):
    sid = manager.create_square(x=0, y=0, side=4)

    assert manager.perimeter(shape_id=sid) == 16


def test_translate_point(manager):
    pid = manager.create_point(x=1, y=1)

    manager.translate(shape_id=pid, dx=2, dy=3)

    details = manager.get_details(shape_id=pid)

    assert "X=3" in details
    assert "Y=4" in details


def test_distance_between_points(manager):
    p1 = manager.create_point(x=0, y=0)
    p2 = manager.create_point(x=3, y=4)

    dist = manager.distance(shape_id1=p1, shape_id2=p2)

    assert dist == 5


def test_compare_shapes(manager):
    c1 = manager.create_circle(x=0, y=0, radius=1)
    c2 = manager.create_circle(x=0, y=0, radius=2)

    bigger, smaller, diff = manager.compare(
        shape_id1=c1,
        shape_id2=c2
    )

    assert bigger == c2
    assert smaller == c1
    assert diff > 0


def test_compare_equal_shapes(manager):
    s1 = manager.create_square(x=0, y=0, side=2)
    s2 = manager.create_square(x=0, y=0, side=2)

    _, _, diff = manager.compare(
        shape_id1=s1,
        shape_id2=s2
    )

    assert diff is None


def test_delete_shape(manager):
    pid = manager.create_point(x=1, y=1)

    manager.delete(shape_id=pid)

    assert manager.list() == {}


def test_delete_invalid_shape(manager):
    with pytest.raises(ValueError):
        manager.delete(shape_id=999)


def test_length_not_supported(manager):
    pid = manager.create_point(x=0, y=0)

    with pytest.raises(ValueError):
        manager.length(shape_id=pid)
