"""Ex04 detais are shown here."""
__author__ = "730713746"


def all(list: list[int], element: int) -> bool:
    """Find if all is match."""
    if len(list) == 0:
        return False
    index = 0
    while index < len(list):
        if list[index] != element:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    """To find the largest."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index = 0
    largest = input[0]
    while index < len(input):
        if input[index] > largest:
            largest = input[index]
        index += 1
    return largest


def is_equal(list_x: list[int], list: list[int]) -> bool:
    """To check if 2 lists are equal."""
    if len(list_x) == 0 and len(list) == 0:
        return True
    if len(list_x) == 0 or len(list) == 0:
        return False
    index = 0
    if len(list_x) != len(list):
        return False
    while index < len(list_x) and index < len(list):
        if list_x[index] != list[index]:
            return False
        index += 1
    return True