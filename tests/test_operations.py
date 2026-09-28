try:
    from src.math_operations import add, subtract
except ImportError:
    from src.math_operations import add, subtact as subtract


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(1, 2) == -1
