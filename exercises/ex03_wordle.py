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
    index: int = 0
    output: str = ("")
    while index <= len(x) - 1:
        if x[index] == y[index]:
            output = output + f"{green}"
        elif contains_char(y, x[index]) is True:
            output = output + f"{yellow}"
        else:
            output = output + f"{white}"
        index = index + 1
    return f"{output}"
    

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
    if gues == secret:
        print(f"You won in {t}/6 turns!")
    t = t + 1
    while gues != secret and t <= 6:
        print(f"=== Turn {t}/6 ===")
        gues = input_guess(len(secret))
        print(emojified(gues, secret))
        t = t + 1
    if t == 7:
        print("X/6 - Sorry, try again tomorrow!")
    if t != 1 and gues == secret:
        print(f"You won in {t-1}/6 turns!")


if __name__ == "__main__":
    main()