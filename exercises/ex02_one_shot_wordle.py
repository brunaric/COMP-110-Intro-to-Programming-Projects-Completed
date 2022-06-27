"""One Shot Wordle."""


__author__ = 730466477

secret_word: str = "python"
guess: str = input(" What is your 6 letter guess? ")
while len(guess) != len(secret_word): 
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
    
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
emoji: str = ""
guessed_character: bool = False
alternate_index: int = 0

while index < len(secret_word):
    if guess[index] == secret_word[index]:
        emoji += GREEN_BOX
    else:
        guessed_character = False
        alternate_index = 0
        while not guessed_character and alternate_index < len(secret_word):
            if secret_word[alternate_index] == guess[index]:
                guessed_character = True
            alternate_index = alternate_index + 1
        if guessed_character:
            emoji += YELLOW_BOX
        else: 
            emoji += WHITE_BOX
    index = index + 1

print(emoji)
if guess == secret_word: 
    print("Woo! You got it! ")
else:
    print("Not quite. Play again soon! ")
 