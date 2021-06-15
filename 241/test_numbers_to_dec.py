import pytest

from numbers_to_dec import list_to_decimal


def test_single():
    assert list_to_decimal([1]) == 1
    assert list_to_decimal([0]) == 0


def test_multiple():
    assert list_to_decimal([1, 1]) == 11
    assert list_to_decimal([0, 1, 1]) == 11


def test_float():
    with pytest.raises(TypeError):
        list_to_decimal([0.5])


def test_string():
    with pytest.raises(TypeError):
        list_to_decimal(["a"])


def test_bool():
    with pytest.raises(TypeError):
        list_to_decimal([True])


def test_negative():
    with pytest.raises(ValueError):
        list_to_decimal([-1])
