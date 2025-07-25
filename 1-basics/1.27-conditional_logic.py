# Relies on the use of Booleans

is_old = False
is_licence = True 

if is_old:
    print("Good to drive.")
elif is_licence:
    print("Nice Licence")
else:
    print("You can't drive")

# Could also use:
if is_old and is_licence:
    print("You got it all")
elif not is_old and is_licence:
    print("How did you get this?")
else:
    print("Keep trying")