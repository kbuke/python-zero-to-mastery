# 1. Encapsulation
    # Binding of data and functions that manipulate data and are encapsulated into one big object (like attributes, functions and methods)
class PlayerChar:
    membership=True

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def speak(self):
        print(f"My name is {self.name}, I am {self.age} years old.")

player_1 = PlayerChar("Kaan", 31)
player_1.speak()
# We add another method (speak) into the class, speak is a form of encapsulaton

# 2. Abstractions
    # is where we hide certain information, and only give access to what is necessary
    # again speak is an example of this, as player_1 has access to it, w.o. knowing how it was implemented
    # however this could lead to an issue such as 
        # player_1.speak = "Boo"
    # if called, this would result in an error.
    # There is a way to mark attributes as private and not to be changed
        # self._name = name
        # self._age = age
    # however like the way we mark const variables in python this is just a sign to other developers

# 3. Inheritance
    # allows objects to take on properties of existing ones, and can inherit class
class User:
    #if we have no variables, no need for __init__
    def sign_in(self):
        print("Logged In")
    
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power 
    def attack(self):
        print(f"Attach with power {self.power}")

class Archer(User):
    def __init__(self, name, num_arrow):
        self.name = name 
        self.num_arrow = num_arrow
    def attack(self):
        while self.num_arrow > 0:
            print(f"Firing arrow {self.num_arrow}")
            self.num_arrow -= 1
            print(f"{self.num_arrow} left")
        else:
            print("uh oh out of arows")

wizard_1 = Wizard("Merlin", 100)
wizard_1.attack()

archer_1 = Archer("Legolas", 5)
archer_1.attack()
#In this example we can use the ISINSTANCE function to see if something is an instance of another
print(isinstance(wizard_1, Wizard)) # True
print(isinstance(archer_1, Wizard)) # False
print(isinstance(archer_1, User)) # True
print(archer_1.sign_in()) # prints "Logged In" as it inherits Users sign_in method

# 4. Polymorphism
    # Refers to how object classes can share a method, but they can act different based on the object that calls them, such as Wizard.attack() and Archer.attack()