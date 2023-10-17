def w_sum(x: list[float]) -> float:
    index = 0
    outcome = 0.0
    while index < len(x):
        outcome += x[index]
        index += 1
    return outcome


def f_sum(x: list[float]) -> float:
    outcome = 0.0
    for i in x:
        outcome += i
    return outcome


def f_range_sum(x: list[float]) -> float:
    outcome = 0.0
    for i in (0,len(x),1):
        outcome += x[i]
    return outcome