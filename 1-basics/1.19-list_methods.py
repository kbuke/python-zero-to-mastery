basket = [1, 2, 3, 4]

# to add values we use the APPEND method:
basket.append(5) #it adds to the end of the list

# to insert we use the INSERT method, which takes two values
    # the index at which to insert
    # the value
basket.insert(2, 100)

#-------------------------------------------------------------------------

# to add an iterable amount to end of list, use EXTEND method
basket.extend([7, 8])

# to remove a value we use the POP method:
    # if we give no arguments, it rm's last value
    # if we give it a value it rm's from that index
    # can assign variables to take the value of rm'd item
basket.pop(0) #rm 1st item
rm_item = basket.pop(3)
basket.pop() #rm last item

print(basket)
print(rm_item)

#-------------------------------------------------------------------------

new_basket = ["a", "b", "c", "d", "e", "f", "a"]
# We can index values from a list using INDEX method
d_index = new_basket.index("d")
print(f"d is at index {d_index}")

# Can check if something exists in an index range by giving
    # variable = list_variable(value, strt_range, end_range)
e_index = new_basket.index("e", 0, 5) #if this was 4 it would return error
print(f"e is between index's 0 and 5? {e_index}")

#-------------------------------------------------------------------------
# To see how many times a value occurs in a list, use COUNT method
a_frequency = new_basket.count("a")
print(f"a occurs in the basket {a_frequency} times!")

#-------------------------------------------------------------------------
# We could sort our list alphabetically using SORT method
new_basket.sort()
print(new_basket)

# To do it automatically, we use SORTED function
print(sorted(new_basket))

#-------------------------------------------------------------------------
# We can copy lists with the COPY method
copy_new_basket = new_basket.copy()
print(copy_new_basket)

#-------------------------------------------------------------------------
# We can also reverse a list by using REVERSE method:
new_basket.reverse()
print(new_basket)

#Using REVERSE and SORT together would be able to alphabetically reverse a list not in order
unordered_list = ["b", "a", "d", "c"]
unordered_list.sort()
unordered_list.reverse()
print(unordered_list)