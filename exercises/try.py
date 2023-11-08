from exercises.ex06.dictionary import invert
import pytest

def test_invert_b() -> None:
    """It would test with an dict with same value."""
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)