
from plates import is_valid

def test_plates():
    assert is_valid("CS50") == True
    assert is_valid("50") == False
def test_num():
    assert is_valid("CS05") == False
    assert is_valid("ASD89A") == False
def test_char():
    assert is_valid("PI3.14") == False
    assert is_valid("3ASDFA") == False
def test_lenght():
    assert is_valid("ASDASFD32") == False

