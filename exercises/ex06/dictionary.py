"""Combining two lists into a dictionary."""
__author__ = "730713746"

def invert(x: dict[str: str]) -> dict[str: str]:
    """Exchange key and value."""
    y: dict[str, str] = {}
    for i in x:
        y[x[i]] = i
    if len(y) != len(x):
        return exit("KeyError")
    return y


def favorite_colors(x: dict[str: str]) -> str:
    """Find highest frequency."""
    bank: dict[str: int] ={}
    for i in x:
        if (x[i] in bank) == False:
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


def count(x: list[str]) -> dict[str: int]:
    """Count all frequency."""
    num: dict[str: int] = {}
    for i in x:
        if (i in num) == False:
            num[i] = 1
        else:
            num[i] += 1
    return num


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """Count all frequency."""
    num: dict[str, list[str]] = {}
    for i in x:
        if (i[0] in num) == False:
            num[i[0]] = [i]
        else:
            num[i[0]].append(i)
    return num


def update_attendance(x: dict[str, list[str]], y: str, z: str) -> dict[str, list[str]]:
    """Update the new dictionary."""
    if (y in x) == False:
        x[y] = [z]
    else:
        x[y].append(z)
    return x
