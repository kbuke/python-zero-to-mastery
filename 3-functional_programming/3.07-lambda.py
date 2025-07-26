# Lambda Functions
    # One-time anonymous functions, marked by the LAMBDA keywords
    # It helps to make code DRYER

# W.O Lambda
my_numbers = [1, 2, 3]

def multiply_2(li):
    return li * 2

print(list(map(multiply_2, my_numbers)))

# With Lambda
print(list(map(lambda item: item * 2, my_numbers)))