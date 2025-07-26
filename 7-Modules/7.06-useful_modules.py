# Useful Modules
    # These are some useful modules to consider:

# 1. ----- Collections -----
from collections import Counter, defaultdict, OrderedDict
hello_letter = "hello"
print(Counter(hello_letter)) # This creates a dictionary keeping track of how frequently an item occurs

dictionary = defaultdict(lambda: "Does not exist", {"a": 1, "b": 2})
# The first arg is a func, providing value when a missing key is accessed
# Second arg is an optional dictionary, used to populate initial key-value pairs
print(dictionary)
print(dictionary["a"])
print(dictionary["b"])

dict_1 = OrderedDict()
dict_1["a"] = 1
dict_1["b"] = 2

dict_2 = OrderedDict()
dict_2["a"] = 1 
dict_2["b"] = 2

dict_3 = OrderedDict()
dict_3["a"] = 2
dict_3["b"] = 1

print(dict_1 == dict_2) # True
print(dict_1 == dict_3) # False

# OrderedDict remembers the order where keys are inserted
# Although dict_1 and 3 have the same keys, the values r diff therefore false

# 2. ----- datetime -----
    # Helps with dates and times
import datetime
print(datetime.time(4, 45, 2)) # 04:45:02
print(datetime.date.today()) # prints todays date

# 3. ----- array -----
    # Similar to lists, but take up less memory and performs faster
    # Sets how much memory we can use in the machine when we create it
    # Good substitute for generators
from array import array
test_array = array("i", [1, 2, 3]) #  i is a TYPE CODE telling python what kind of data is stored in the array. i is a SIGNED INT
print(test_array)
print(test_array[0])