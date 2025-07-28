# Regular Expressions
    # Good for validations, marked by re
import re 
example_string = "search for this inside of this text please!"
print(re.search("this", example_string)) # shows if there's a match, and the range it is in

# However it only picks up the first instance, to find if there is more than one
pattern = re.compile("this")
a = pattern.findall(example_string)
print(a)

# Can also check to see if there are any matches
new_pattern = re.compile("search for this inside of this text please?")
b = new_pattern.fullmatch(example_string)
c = new_pattern.match(example_string)
print(b) # returns None due to ! and ?
print(c) # returns a match even with the diff

# As mentioned they are good for validation and collecting emails
# Use website regex to help tinker with functions
# below we got from link https://emailregex.com/
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
def test_email():
    email = input("Please enter email: ")
    if pattern.match(email):
        print("Valid email")
    else:
        print("Invalid email")

test_email()