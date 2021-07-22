import random
from bagels.__main__ import NUM_DIGITS


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    secretNum = ""

    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""

    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)