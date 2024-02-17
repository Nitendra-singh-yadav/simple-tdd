from src.adder import add

def test_empty_string():
    assert add('') == 0

def test_single_number():
    assert add('1') == 1

def test_two_numbers():
    assert add('1,2') == 3

def test_newline_between_numbers():
    assert add('1\n2,3') == 6

def test_different_delimiter():
    assert add('//;1\n2,2') == 5
