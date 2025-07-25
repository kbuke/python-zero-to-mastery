# These are unordered collections of unique objects
# These r marked by {}, but unlike dictionaries, have no keys
my_set = {1, 2, 3, 4, 5, 5}
print(my_set) # only one 5 will show up

# Used for things like ensuring no duplicate emails
# Due to being unordered there is no indexing, therefore use:
print(1 in my_set)

your_set = {4, 5, 6, 7, 8, 9, 10}

# To show difference between the first set when compared to second use DIFFERENCE method
print(my_set.difference(your_set)) # Shows {1, 2, 3} as these r in 1st but not 2nd

# To rm a value from a set use DISCARD() method
your_set.discard(4)
print(your_set)

my_set.difference_update(your_set)
print(my_set)

# To check if two sets have no values in common
print(my_set.isdisjoint(your_set)) #Here there's nothing in common {1, 2, 3, 4} and {5, 6, 7, 8, 9, 10}

