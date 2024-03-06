from seasons import days_min_to_words

def test_date():
  assert days_min_to_words(365) == "Five hundred twenty-five thousand, six hundred minutes"