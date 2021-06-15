from fibonacci import fib
import pytest

# write one or more pytest functions below, they need to start with test_
def test_first():
    assert fib(0) == 0
    assert fib(1) == 1


def test_later():
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(10) == 55


def test_negative():
    with pytest.raises(ValueError):
        fib(-1)
