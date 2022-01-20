from weeklycodingchallenge.week1 import uncompress


def test_uncompress():
    """ Test the uncompress function """

    # Given
    input = "127y"
    expected = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"  # noqa
    # When
    result = uncompress(input)
    # Then
    assert result == expected
