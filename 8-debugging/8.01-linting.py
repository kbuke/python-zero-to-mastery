# Linting
    # Detects issues with code before we run it by installing pylint
    # Marked by pdb
    # It allows us to work in the terminal, we can type
        # help => showing commands we can use with pdb
        # help list => shows how list commands work specifically
        # step => allows us to go to the next line in function
    # You can reassign variables in function

import pdb
def add(num1, num2):
    pdb.set_trace()
    t = 4 * 5
    return num1 + num2

print(add(1, 3))