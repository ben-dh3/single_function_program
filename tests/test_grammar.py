from lib.grammar import *

def test_grammar():
    result = grammar('Hello world!')
    assert result == True

    result = grammar('hello world,')
    assert result == False