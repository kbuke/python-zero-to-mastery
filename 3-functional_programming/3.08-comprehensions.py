# Comprehensions
    # Can be used with lists, sets and dicts
    # They're a quick way to create them, instead of looping and appending.

# Creating a list with loops and append:
my_list = []
for char in "hello":
    my_list.append(char)
print(my_list)

# Creating a list with Comprehensions
my_comp_list = [char for char in "hello"]
print(my_comp_list)

# For dictionaries:
simple_dict = {
    "a": 1,
    "b": 2
}
my_dict = {key: value * 2 for key, value in simple_dict.items()}
print(my_dict)

# For sets
my_set = {char for char in "hello"}
print(my_set)