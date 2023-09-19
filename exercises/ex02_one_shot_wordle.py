"""one shot wordle exercise"""
__author__ = 730713746
y: str = "python"
x: str = input("What is your 6-letter guess?")
while len(x) != 6:
    x: str = input("That was not 6 letters! Try again:")
if x != y:
    index: int = 0
    output = ("")
    while index <= 5:
        if x[index] == y[index]:
            output = output + f"\U0001F7E9"
        elif x[index] in {"p", "y", "t", "h", "o", "n"}:
            output = output + f"\U0001F7E8"
        else:
            output = output + f"\U00002B1C"
        index = index + 1
    print(str(output))
    print("Not quite. Play again soon!")
else:
    print(f"\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9")
    print("Woo! You got it!")