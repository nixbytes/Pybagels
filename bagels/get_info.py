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


def getClues():
    pass
