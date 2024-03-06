from bank import value

def test_greet():
    assert value("Hello") == "$0"

def test_greet2():
    assert value("How are you") == "$20"

def test_greet3():
    assert value("What's up") == "$100"

