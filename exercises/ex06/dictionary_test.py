"""Testing the dictionary methods."""
__author__ = "730713746"
from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_a() -> None:
    """It would test with an empty list."""
    x: dict[str, str] = {}
    assert invert(x) == {}


def test_invert_b() -> None:
    """It would test with an dict with same value."""
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)


def test_invert_c() -> None:
    """The main usage of the invert function."""
    x: dict[str, str] = {"cat": "fish"}
    assert invert(x) == {"fish": "cat"}


def test_favorite_color_a() -> None:
    """The return an empty list."""
    x: dict[str, str] = {}
    assert favorite_color(x) == ""


def test_favorite_color_b() -> None:
    """The return an one color exist."""
    x: dict[str, str] = {"Marc": "blue", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(x) == "blue"


def test_favorite_color_c() -> None:
    """The return of multipul color exist."""
    x: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(x) == "blue"


def test_count_a() -> None:
    """This should return an empty dict for an empty input."""
    x: list[str] = []
    assert count(x) == {}


def test_count_b() -> None:
    """This should return value of 1 for each str for a nonreplicate list."""
    x: list[str] = ["apple", "banana", "strawberry"]
    assert count(x) == {"apple": 1, "banana": 1, "strawberry": 1}


def test_count_c() -> None:
    """This should return value of frequecy for each str for a nonreplicate list."""
    x: list[str] = ["apple", "banana", "strawberry", "banana"]
    assert count(x) == {'apple': 1, 'banana': 2, 'strawberry': 1}


def test_alphabetizer_a() -> None:
    """This should return an empty dict for an empty input."""
    x: list[str] = []
    assert alphabetizer(x) == {}


def test_alphabetizer_b() -> None:
    """This should return an empty dict for an empty input."""
    x: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(x) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_c() -> None:
    """This should return an empty dict for an empty input."""
    x: list[str] = ["python", "sugar", "turtle", "party", "table"]
    assert alphabetizer(x) == {'p': ['python', 'party'], 's': ['sugar'], 't': ['turtle', 'table']}


def test_update_attendance_a() -> None:
    """This should return an empty dict for an empty input."""
    x: dict[str, list[str]] = {}
    y: str = ""
    z: str = ""
    assert update_attendance(x, y, z) == {}


def test_update_attendance_b() -> None:
    """This should return an empty dict for an empty input."""
    x: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    y: str = "Tuesday"
    z: str = "Vrinda"
    assert update_attendance(x, y, z) == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}


def test_update_attendance_c() -> None:
    """This should return an empty dict for an empty input."""
    x: dict[str, list[str]] = {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}
    y: str = "Wednesday"
    z: str = "Kaleb"
    assert update_attendance(x, y, z) == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}