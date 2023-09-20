"""one shot wordle exercise."""
__author__ = "730713746"
y: str = "python"
x: str = input("What is your 6-letter guess?")
green = "\U0001F7E9"
yellow = "\U0001F7E8"
white = "\U00002B1C"
while len(x) != 6:
    x = input("That was not 6 letters! Try again:")
if x != y:
    index: int = 0
    output: str = ("")
    while index <= 5:
        if x[index] == y[index]:
            output = output + f"{green}"
        elif x[index] in {"p", "y", "t", "h", "o", "n"}:
            output = output + f"{yellow}"
        else:
            output = output + f"{white}"
        index = index + 1
    print(f"{output}")
    print("Not quite. Play again soon!")
else:
    print(f"{green}{green}{green}{green}{green}{green}")
    print("Woo! You got it!")