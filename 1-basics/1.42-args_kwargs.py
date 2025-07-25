# ARGS
    # marked by * when being used as a parameter
    # they collect extra positional arguments as a tuple
    # useful for when you don't know how many arguments to expect

# KWARGS
    # marked by ** when being used as a paramter
    # returns a dictionary version of key-value pairs

def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for i in kwargs.values():
        total += i
    return sum(args) + total
print(super_func(1, 2, 3, 4, 5, num1 = 5, num2 = 10))