# Tuples are another data-structure similar to lists, but:
    # marked by ()
    # immutable
my_tuple = (1, 2, 3, 4, 5)
print(f"The 2nd value of my tuple is {my_tuple[1]}")
# to check if a value is in a tuple
print(4 in my_tuple)

# Good for when a list doesn't need to be changed 
# It processes information faster
print(my_tuple.items())