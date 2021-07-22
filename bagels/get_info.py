import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main() -> None:
    print(
        """
    
    Bagels, a deductive logic game.
    from Al Sweigart al@inventwithpython.com and edit by nixbytes
    I am thinking of a {}-digit number 

    """.format(
            NUM_DIGITS
        )
    )

    while True:

        secretNum = getSecretNum()

        print(
            "I have though up a number.\nYou have {} guesses to get it.".format(
                MAX_GUESSES
            )
        )

        numGuesses = 1

        while numGuesses <= MAX_GUESSES:
            guess = ""
            # keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input("> ")
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("you ran out of guesses")
                print("The answer was {}.\n".format(secretNum))

        # ask player if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input(">").lower().startswith("y"):
            break
    print("Thanks for playing!")


def getSecretNum() -> str:
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    secretNum = ""

    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum


def getClues(guess, secretNum) -> str:
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""

    if guess == secretNum:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)
