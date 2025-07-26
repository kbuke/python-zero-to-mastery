# Exceptions
    # Errors that crash our code
    # Raised when the server stops running, and gives an error
    # We use ERROR HANDLING which lets scripts run even with errors
    # Some keywords we use are:
        # try
        # except
        # else

while True:
    try:
        age = int(input("How old are you? "))
        print(f"You are {age} years old")
    except ValueError as err: #where err is the variable of error
        print(f"Please enter a number {err}")
    except ZeroDivisionError as err:
        print(f"Please enter a number greater than 0, {err}")
    else:
        print("Thanks")
        break # break loop when given a number

# Maybe look at some other Python errors