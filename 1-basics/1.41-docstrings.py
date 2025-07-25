# These are unique to functions
# They allow us to make comments in functions, revealing their use
# Marked by '''
# To access we call the HELP() function to see purpose
def test(a):
    '''
    Info: this is a test function
    '''
    print(a)
test("Hi")
help(test)
# Press q to exit the help function in terminal