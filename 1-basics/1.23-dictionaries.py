# Similar to JS objects, marked by dict and use {}
# Data-types that use key-value pairs (keys and strings) to grab info.
# They are unordered, therefore you may not receive values as you submit them.
dictionaries = {
    "a": 1,
    "b": 2
}

# Dictionary-keys must be immutable, therefore we use strings
# The keys must be unique, if there are two keys with same name we use most recent
new_dict = {
    "123": "a",
    "test": "b",
    "123": "c"
}
print(f"The value of 123 is {new_dict['123']}") #use single quotes to reference key

