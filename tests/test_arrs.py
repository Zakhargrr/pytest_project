from utils import arrs
import pytest


@pytest.fixture
def three_elems_coll():
    return [1, 2, 3]


@pytest.fixture
def four_elems_coll():
    return [1, 2, 3, 4]


@pytest.fixture
def empty_coll():
    return []


def test_get(three_elems_coll, empty_coll):
    assert arrs.get(three_elems_coll, 1, "test") == 2
    assert arrs.get(three_elems_coll, -1, "test") == "test"
    with pytest.raises(IndexError):
        arrs.get(empty_coll, 0, "test")


def test_slice(four_elems_coll, three_elems_coll, empty_coll):
    assert arrs.my_slice(four_elems_coll, 1, 3) == [2, 3]
    assert arrs.my_slice(three_elems_coll, 1) == [2, 3]
    assert arrs.my_slice(three_elems_coll, -2) == [2, 3]
    assert arrs.my_slice(empty_coll, 10) == []
    assert arrs.my_slice(three_elems_coll, -4) == [1, 2, 3]
