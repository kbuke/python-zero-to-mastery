# Decorators
    # Are marked by @
    # Work similar to Call Back Functions, and make use of functions acting as FIRST CLASS CITIZENS
    # First-Class-Citizens act as variables and can be used as parameters, a.k.a. Higher Order Functions

def my_decorator(fn): # This is a Higher Order Func, as it accepts a func as para,
    # def wrapper():
    #     print("***")
    #     fn()
    #     print("***")

    def wrapper(*args, **kwargs):
        print("***")
        fn(*args, **kwargs)
        print("***")
    return wrapper 

@my_decorator # Same as saying def my_decorator(hello)
# def hello():
#     print("hi")
def hello(greeting, emoji = "😃"):
    print(greeting, emoji)

# hello()
hello("hi")

    # In this example lines[(7 - 10), (19 - 20), (24)] represent a base example
    # However for the other part, this is an example of a DECORATOR PATTERN, where we give as many arguments as possible

    # Decorators are good for keeping code DRY and efficient, especially for authentication
user_1 = {
    "name": "Zahra",
    "valid": True
}
user_2 = {
    "name": "Kaan",
    "valid": False
}

def validate(fn):
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            print("Invalid User")
    return wrapper 

@validate
def message(user):
    print(f"user {user['name']} sent")

message(user_1) # user Zahra sent
message(user_2) # Invalid user
