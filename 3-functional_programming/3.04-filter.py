# Filter
    # Uses the same format as MAP functions
my_list = [1, 2, 3]
def is_odd(li):
    return li % 2 != 0
print(list(filter(is_odd, my_list)))