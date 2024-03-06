from twttr import shorten

def test_letter():
    assert shorten("hola") == "hl"
    assert shorten("HolA") == "Hl"
def test_digits():
    assert shorten("Hol3") == "Hl3"
def test_punctuation():
    assert shorten("ho.la") == "h.l"