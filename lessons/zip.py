"""Combining two lists into a dictionary."""
__author__ = "730713746"


def zip(x: list[str], y: list[int]) -> dict[str, int]:
    """Combining two lists into a dictionary."""
    output: dict[str, int] = {}
    idx = 0
    if len(x) != len(y) or len(x) == 0 or len(y) == 0:
        return output
    while idx < len(x):
        output[x[idx]] = y[idx]
        idx += 1
    return output
    
