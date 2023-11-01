"""Combining two lists into a dictionary."""
__author__ = "730713746"


def invert(x: dict[str, str]) -> dict[str, str]:
    """It would exchange key and value."""
    y: dict[str, str] = {}
    for i in x:
        y[x[i]] = i
    if len(y) != len(x):
        return exit("KeyError")
    return y


def favorite_color(x: dict[str, str]) -> str:
    """It would find highest frequency."""
    bank: dict[str, int] = {}
    for i in x:
        if (x[i] in bank) is False:
            bank[x[i]] = 1
        else:
            bank[x[i]] += 1
    max: int = 0
    outcome: str = ""
    for idx in bank:
        if bank[idx] > max:
            max = bank[idx]
            outcome = idx
    return outcome


def count(x: list[str]) -> dict[str, int]:
    """This doc string is used for check if auto grader works well"""
    """It would count all frequency."""
    num: dict[str, int] = {}
    for i in x:
        if (i in num) is False:
            num[i] = 1
        else:
            num[i] += 1
    return num


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """It woule like to count all frequency with capital."""
    num: dict[str, list[str]] = {}
    for i in x:
        if (i[0] in num) is False:
            num[i[0]] = [i]
        else:
            num[i[0]].append(i)
    return num


def update_attendance(x: dict[str, list[str]], y: str, z: str) -> dict[str, list[str]]:
    """Update the new dictionary."""
    if (y in x) is False:
        x[y] = [z]
    else:
        x[y].append(z)
    return x
