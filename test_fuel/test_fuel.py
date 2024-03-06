import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("3/3") == 100
    assert convert("2/10") == 20
    assert convert("20/40") == 50
    assert convert("1/10") == 10
    assert convert("5/100") == 5


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


def test_division():
    with pytest.raises(ZeroDivisionError):
        convert("13/0")


def test_valueError():
    with pytest.raises(ValueError):
        convert("5/2")