
from lib.three import reduce_string
### Unit Tests

def test_reduce_string_works():
    input = "elephant"
    result = reduce_string(input)
    assert result == "lephan"
    

    # test combinations of regex are working. with/without spaces in differint positions. different num of spaces. upper/lowercase
    # test inputs 
    # test name doesn't have numbers
    # test name carries over across pages