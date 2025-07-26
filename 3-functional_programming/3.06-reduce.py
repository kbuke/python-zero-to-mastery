# Reduce
    # Not a built in Python function, so we need to import it
    # Used for when:
        # You need custom logic (like multiplication, string concatenation, etc.).
        # You're doing non-standard reductions.

from functools import reduce
my_list = [1, 2, 3]
def accumulator(acc, item):
    return acc + item 
print(reduce(accumulator, my_list, 0)) # 6

    # 0 is the initial value, therefore:
        # 1st pass: 0 + 1
        # 2nd pass: 1 + 2
        # 3rd pass: 3+ 3

