# Eveything in Python is an object
# We use the CLASS keyword to mark an object
# it forms the blueprint of what we want to create including:
    # attributes
    # methods
# our object can take

# init refers to the instance of the class:
    # player1.name 
# cls refers to the class itself:
    # PlayerChar.name

class PlayerChar: # we use camel case, and NEVER make it plural
    membership = True # This is a CLASS OBJECT ATTRIBUTE and is static
    def __init__(self, name, age): # this is a dunder method, where self represents the class itself (PlayerChar)
        self.name = name
        self.age = age 
        print(f"Hi {self.name} you are {self.age} years old.")
    
    @classmethod # takes cls as first arg, and can access and modify class state
    def adding_things(cls, num1, num2):
        return(cls("Zahra", num1 + num2))
    
    @staticmethod # just a regular function inside the class, it doesnt care for class or instance
    def adding_things2(*args):
        return sum(args)
    
player1 = PlayerChar("Kaan", 31)
print(player1)

player2 = PlayerChar.adding_things(14, 15)

player_age = PlayerChar.adding_things2(31, 14, 15)
print(player_age)

# In this example (lines 8 - 13):
    # name
    # age
    # membership
# are referred to as attributes/properties
# however membership is a class-object-attribute meaning it is not dynamic
# for the other two, we can set default values

# From lines 15 - 17 we add methods in the class
# cls works exactly the same as self, in that it represents the whole class PlayerChar

# From lines 19 - 21 we put in a staticmethod
# it belongs to the class, but:
    # doesn't receive self or class as 1st arg
    # behanves like a regular function, just org in the class for logical grouping
    # doesn't need access to the class or instance state
    # doesn't know anything about the PlayerChar instances or attributes
