# Built in Modules
    # External modules and packages we can borrow to expand functions and methods of py
    # There are online resources to check
    # When running in terminal type:
        # python 7.04-built_in_modules.py 1 10
    # This sets the range of numbers from 1 - 10

from random import randint # choose integer between range 
from random import choice # choose random value from iterable
import sys # a module that provides access to system-specific parameters and functions

def random_number():
    first = int(sys.argv[1])
    last = int(sys.argv[2])

    chosen_number = randint(first, last)

    while True:
        try:
            user_number = int(input(f"Please select a number between {first} and {last}: "))
            if first <= user_number <= last:
                if user_number == chosen_number:
                    print("Congrats you win")
                    break 
                else:
                    print("Guess again")
            else:
                print("Please enter a number in the range")
        except ValueError as err:
            print(f"Please enter a valid number, {err}")
print(random_number())

    # There are third party libraries that can be used, using
        # pip install
    # Use the below website for a good selection of libraries
        # pypi.org