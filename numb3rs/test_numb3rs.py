from numb3rs import validate

def test_numb3rs():
    assert validate("127.0.0.1") == True
    assert validate("1000.2.3.24") == False
def test_string():
    assert validate("cat") == False
def test_out_range():
    assert validate("275.255.255.255") == False
    assert validate("69.276.256.257") == False

