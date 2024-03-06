from working import convert
import pytest



def test_hours():
    assert convert("9 AM to 12 AM") == "09:00 to 00:00"



def test_errors():
    with pytest.raises(ValueError):
        convert("9:62 AM to 8 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 12 PM")