from src.adder import add
import pytest

def test_empty_string():
    assert add('') == 0

def test_single_number():
    assert add('1') == 1

def test_two_numbers():
    assert add('1,2') == 3

def test_newline_between_numbers():
    assert add('1\n2,3') == 6

def test_different_delimiter():
    assert add('//;\n1;2;2') == 5

def test_negative_values():
    with pytest.raises(ValueError) as erinfo:
        add('1,2,-4,-6,3')
    assert str(erinfo.value) == 'negative numbers not allowed: -4, -6'
