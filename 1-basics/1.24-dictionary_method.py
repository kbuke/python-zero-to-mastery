# If we reference a key that doesn't exist it creates an error and stops program.
# We can see if a key exists without causin the program to crash by using GET() method
user = {
    "basket": [1, 2, 3],
    "greet": "hello",
    "age": 29
}
print(user.get('age')) # shows 29
print(user.get('help')) # shows None

# Can create a dictioary using DICT() function
user_2 = dict(name = "Kaan")
print(user_2)

# To see if certain keys, or values exist in a dictionary:
print("greet" in user.keys()) #True
print("gender" in user.keys()) #False
print("hello" in user.values()) #True

# To create an empty dictionary use CLEAR method
user.clear()
print(user)

# To copy a dictionary user the COPY() method
user_3 = user_2.copy()
print(user_3)

# To rm a key-value pair use POP() method
user_4 = {
    "name": "Zahra",
    "age": 29,
    "hair": "black",
    "eyes": "brown"
}
user_4.pop("hair")
print(user_4)
# To remove last item use POPITEM() method
user_4.popitem()
print(user_4)

# To update a dictionary we use UPDATE() method
user_4.update({"age": 30})
print(user_4)
# We can also use it to add key-value pair
user_4.update({"father": "Iqbal"})
print(user_4)
