# Strings are an ordered sequence of chars and are indexef
# This is good for manipulation
selifish = "me me me"
print(f"the first char of selfish is {selifish[0]}")
print(f"The first 4 chars of selfish is {selifish[0:4]}")
# It is done as [x:y:z] where:
    # x is the start
    # y is the end (so the last to be printed is index 3 abover)
    # z skip
print(selifish[0:8:2])

# Can also find last char
print(f"The last char of selfish is {selifish[-1]}")

# Can also reverse the string
print(f"To reverse selfish we say {selifish[::-1]}")