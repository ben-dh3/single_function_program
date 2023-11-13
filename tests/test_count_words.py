from lib.count_words import *

def test_count_words():
    result = count_words('words words words')
    assert result == 3