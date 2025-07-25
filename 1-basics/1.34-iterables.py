# An object/collection that can be iterated over such as lists, sets, dictionaries and strings
# Dictionaries are most specific to iterate over due to their key-value pairing

user = {
    "name": "Kaan",
    "age": 31,
    "can_swim": True
}

# This prints out each key-value pair in a tuple
for i in user.items():
    print(i)

# To print out the key-value pair not in tuple form:
for key, value in user.items():
    print(f"{key}: {value}")

# To print only the values, use VALUES() method
for i in user.values():
    print(i)

# To show keys, use the KEYS() method
for i in user.keys():
    print(i)
