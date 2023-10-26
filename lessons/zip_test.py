"""Test my zip function."""
__author__ = "730713746"
from lessons.zip import zip


def test_empty_list() -> None:
    """Test the output of two empty lists."""
    x: list = []
    y: list = []
    assert zip (x, y) == {}


def test_different_lenth() -> None:
    """Test the output of lists with differet len"""
    x: list = ["a", "b", "c"]
    y: list = [1, 2]
    assert zip (x, y) == {}


def test_usage() -> None:
    """Test the output of main usage"""
    x: list = ["a", "b", "c"]
    y: list = [1, 2, 3]
    assert zip (x, y) == {"a": 1, "b": 2, "c": 3}