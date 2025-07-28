def do_stuff(num=0): #set default to prevent null
    try:
        if num:
            return int(num) + 5
        else: 
            return "Please enter number"
    except ValueError as err:
        return err # This is used to help with test_do_stuff2
