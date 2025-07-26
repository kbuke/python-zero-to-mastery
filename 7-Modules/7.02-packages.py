# Packages
    # We can create folders/packages and import them.
    # Say we have this module:
    # This procedure is done on the main.py and utility.py

# ----- utility.py -----
# def multiply(num1, num2):
#     return num1 * num2 

    # Now if we had another module:

# ----- main.py -----
# import utility
# print(utility.multiply(1, 2))

# We could do it in a cleaner way
# from utility import multiply
# print(multiply(1, 2))