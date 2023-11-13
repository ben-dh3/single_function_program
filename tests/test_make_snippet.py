from lib.make_snippet import *

def test_make_snippet():
    result = make_snippet("the cow jumped over the moon")
    assert result == "the cow jumped over the ..."

    short_result = make_snippet("forest tree")
    assert short_result == "forest tree"