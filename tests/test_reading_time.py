from lib.reading_time import *

def test_reading_time():
    result = reading_time('this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for')
    assert result == '0:00:30'