from lib.check_todo import *

def test_check_todo():
    result = check_todo('string #TODO')
    assert result == True

    result = check_todo('string string')
    assert result == False