"""Structured Wordle."""

__author__ = "730466477"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8" 


def contains_char(string_searched: str, single_character: str) -> bool:
    """Determines if second string single character is found in first string of any length."""
    assert len(single_character) == 1
    index: int = 0
    while index < len(string_searched):
        if single_character == string_searched[index]:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns emojies telling if single character is found in the right place, wrong place, or not found at all."""
    assert len(guess) == len(secret)
    emoji: str = ""
    index: int = 0
    contains: bool = False
    while index < len(secret):
        if guess[index] == secret[index]:
            emoji += GREEN_BOX
        else:
            contains = contains_char(secret, guess[index])
            if contains:
                emoji += YELLOW_BOX
            else: 
                emoji += WHITE_BOX
        index += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Will prompt for a guess and check if it's the right amount of characters."""
    guess: str = input("Enter a " + str(expected_length) + " character word: ")
    while len(guess) != expected_length:
        guess = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    secret_word: str = "track"
    turns: int = 1
    guess: str = ""
    while turns < 7 and secret_word != guess:
        print("=== Turn " + str(turns) + "/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print("You won in " + str(turns) + "/6 turns!")
        turns += 1
    if guess != secret_word:
        print(" X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()