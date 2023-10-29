import pytest
import source.my_functions as my_fnc


def test_add():
    result = my_fnc.add(1, 4)
    assert result == 5


def test_add_strings():
    result = my_fnc.add('Hello ', 'World!')
    assert result == 'Hello World!'


def test_divide():
    result = my_fnc.divide(4, 2)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_fnc.divide(4, 0)