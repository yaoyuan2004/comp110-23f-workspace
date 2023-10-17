"""Three way for sum."""


def w_sum(x: list[float]) -> float:
    """Using the while loop."""
    index = 0
    outcome = 0.0
    while index < len(x):
        outcome += x[index]
        index += 1
    return outcome


def f_sum(x: list[float]) -> float:
    """Using the for loop."""
    outcome = 0.0
    for i in x:
        outcome += i
    return outcome


def f_range_sum(x: list[float]) -> float:
    """Using the for loop in range."""
    outcome = 0.0
    for i in range(0, len(x), 1):
        outcome += x[i]
    return outcome