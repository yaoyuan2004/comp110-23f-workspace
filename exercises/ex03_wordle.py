"""the complete program of wordle."""
__author__ = "730713746"


def contains_char(word: str, character: str) -> bool:
    """Check what inside, and report ture or fauls."""
    assert len(character) == 1
    x: int = 0
    while x < len(word):
        if word[x] == character:
            return True
        x = x + 1
    return False


def emojified(x: str, y: str) -> str:
    """Return a string of emoji whose color show the result."""
    white = "\U00002B1C"
    yellow = "\U0001F7E8"
    green = "\U0001F7E9"
    assert len(x) == len(y)
    if x != y:
        index: int = 0
        output: str = ("")
        while index <= len(y) - 1:
            if x[index] == y[index]:
               output = output + f"{green}"
            elif contains_char(y, x[index]) == True:
                output = output + f"{yellow}"
            else:
                output = output + f"{white}"
            index = index + 1
        return f"{output}"
    else:
        return f"{green}{green}{green}{green}{green}{green}"
    

def input_guess(length: int) -> str:
    """Collect the guess in a right form."""
    guess: str = input(f"Enter a {length} character word")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again:")
    return guess


def main() -> None:
    """The entrypoint of wordle and main game loop."""
    secret: str = "codes"
    t = 1
    print(f"=== Turn {t}/6 ===")
    gues = input_guess(len(secret))
    print(emojified(gues, secret))
    while t <= 6 and gues != secret:
        t = t + 1
        print(f"=== Turn {t}/6 ===")
        gues = input_guess(len(secret))
        print(emojified(gues, secret))
    if t == 7:
        print("X/6 - Sorry, try again tomorrow!")
    print(f"You won in {t}/6 turns!")


if __name__ == "__main__":
    main()