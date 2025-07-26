# Map
    # Takes a function, and an iterable as parameters

my_list = [1, 2, 3]
def multiply_by_2(li):
    return li * 2

print(list(map(multiply_by_2, my_list)))

    # This is a lot more dry, and bears same results as 3.02
    # How MAP works in Python is by:
        # map(function, iterable)
    # So the above is the equivalent to:
        # multiply_by_2(1)
        # multiply_by_2(2)
        # multiply_by_2(3)