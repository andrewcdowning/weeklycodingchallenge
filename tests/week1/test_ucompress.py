from weeklycodingchallenge.week1 import uncompress
import pytest

@pytest.mark.parametrize("test_input,expected", [
    ("127y", "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"),
     ("2p1o5p", "ppoppppp"), 
     ("3n12e2z", "nnneeeeeeeeeeeezz")])  # noqa
def test_uncompress():
    """ Test the uncompress function """

    # Given
    """ test_input and expected """
    # When
    result = uncompress(test_input)
    # Then
    assert result == expected
