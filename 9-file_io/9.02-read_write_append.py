# Read, Write and Append
    # Contrary to the above, use the "with" statement
    # This returns 2 and replaces the first two letters of text.txt with the below (:D)

with open("text.txt", mode = "r+") as my_file:
    text = my_file.write(":D")
    print(text)