import pytest


def sr1(my_str):
    print(my_str[::-1])
    return my_str[::-1]


def sr2(my_str):
    return ''.join(reversed(my_str))


def sr3(my_str):
    result = ''
    for char in my_str:
        result = char + result
    print(result)
    return result

@pytest.mark.parametrize("function", [sr1, sr2, sr3])
@pytest.mark.parametrize("test_input,expected", [
    ("", ""),
    (" ", " "),
    ("ab", "ba"),
    ("123", "321"),
    ("String to reverse!", "!esrever ot gnirtS"),
])
def test_one(function, test_input, expected):
    assert function(test_input) == expected


if __name__ == "__main__":
    pytest.main([__file__])
