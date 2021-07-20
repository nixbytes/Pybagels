import random
import get_info

NUM_DIGIT = 3
MAX_GUESSES = 10


def main():
    print(
        """
    
    Bagels, a deductive logic game.
    from Al Sweigart al@inventwithpython.com
    I am thinking of a {}-digit number 

    """.format(
            NUM_DIGIT
        )
    )


if __name__ == "__main__":
    main()
