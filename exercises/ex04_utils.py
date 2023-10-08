"""Ex04."""
__author__ = "730713746"

def all(list: list, element: int) -> bool:
    if len(list) == 0:
        raise ValueError("all() arg is an empty List")
    index = 0
    while index < len(list):
        if list[index] != element:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index = 0
    largest = input[0]
    while index < len(input):
        if input[index] > largest:
            largest = input[index]
        index += 1
    return largest


def is_equal(x: list[int], y: list[int]) -> bool:
    if len(x) == 0 or len(y) == 0:
        raise ValueError("max() arg is an empty List")
    index = 0
    if len[x] != len(y):
        return False
    while index < len(x):
        if x[index] != y[index]:
            return False
    return True