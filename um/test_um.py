from um import count

def test_count():
    assert count("hello, um, world") == 1
    assert count("Hello Um, world") == 1
    assert count("Hello Um, um yummy world") == 2