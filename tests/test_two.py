
from lib.two import reduce_string
### Unit Tests

def test_reduce_string_works():
    input = "elephant"
    result = reduce_string(input)
    assert result == "lephan"
    