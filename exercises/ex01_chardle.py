"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730466477"

word: str = input("Enter a 5 character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters") 
    exit()
single: str = input("Enter a single character: ")
if len(single) != 1:
    print("Error: Character must be a single character")
    exit()
accumulator: int = 0
print("Searching for " + single + " in " + word)
if word[0] == single:
    print(single + " found at index 0")
    accumulator = accumulator + 1
if word[1] == single:
    print(single + " found at index 1")
    accumulator = accumulator + 1
if word[2] == single:
    print(single + " found at index 2")
    accumulator = accumulator + 1
if word[3] == single:
    print(single + " found at index 3")
    accumulator = accumulator + 1
if word[4] == single:
    print(single + " found at index 4")
    accumulator = accumulator + 1
if accumulator == 0:
    print("No instances of " + single + " found in " + word)
if accumulator == 1:
    print(str(accumulator) + " instance of " + single + " found in " + word)
if accumulator > 1:
    print(str(accumulator) + " instances of " + single + " found in " + word)