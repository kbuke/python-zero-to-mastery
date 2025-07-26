# Pure Functions
    # Functions that produce some output, and those that don't produce side-effects
    # SIDE-EFFECTS are things that are effected outside the function
    # It is best to keep them contained and pure to refrain from errors
    # However this is impossible to do everywhere, as we usually want functions to effect things outside of it

def multiply_by_2(li):
    new_list = []
    for i in li:
        new_list.append(i * 2)
    return new_list

print(multiply_by_2([1, 2, 3]))