# We do NOT have to use variable declarations in Python like we do in JS
# When naming a variable we use the snake_case format:
    # start with a lowercase letter or _
    # only use; numbers, letters or underscores
    # variables are case sensitive
    # don't name them using Py keywords like print

# Variables can be reassigned
iq = 135
user_age = 31
user_age = 135 // 31 #this will round it down
print(f"I have an iq of {iq} and I am {user_age} years old") #user_age will have changed from 31

# Best practice to label a variable as a CONSTANT is to capitalise all letters
USER_AGE = 31
print(user_age)
print(USER_AGE) #this will not be the same as line 16
# however this is only best-practice there is nothing stopping USER_AGE from changing. It is just best practice to imply other users not to change it

# Variables named with a double underscore __ are called DUNDER METHODS.
# Users should not assign their own Dunder Methods, but Python has built in methods

# We can also use the following method to assign variables rapidly:
[a, b, c] = 1, 2, 3
print(f"a equals {a}, b equals {b}, c equals {c}")