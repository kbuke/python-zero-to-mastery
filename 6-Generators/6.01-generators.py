# Generators
    # Allow us to generate a sequence of values over time, for example RANGE
    # They are iterables and marked by YIELD

def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a # This gives the current value of a to the calling code
        temp = a + b # temporary sum
        a = b # new value of a
        b = temp + b # new value of b
for item in fib(21):
    print(item)

    # They don't store sequence in memory, and yield one value at a time.
    # It's useful if you don't need all results at once, if you want to stop midway, or are dealing with infinite or a large sequence.

    #first few rounds
        #    i.   |.   a(yielded).   |.   b.   |.   temp(a + b).   |.   new a.   |.   new b.   |
        #.   0.   |.        0.       |.   1.   |.     0 + 1 = 1.   |.      1.    |.  1 + 1 = 2 |
        #.   1.   |.        1.       |.   2.   |.     1 + 2 = 3.   |.      2.    |.  3 + 2 = 5 |
        #.   2.   |.        2.       |.   5.   |.     2 + 5 = 7.   |.      5.    |.  7 + 5 = 12|
     