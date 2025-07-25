# Object Introspection
    # The ability to determine the type of object at run time (when code's running)
class User:
    def __init__(self, email):
        self.email = email

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email) # refers to the parent class (User)
        self.name = name
        self.power = power 

wizard_1 = Wizard("Merlin", 60, "merlin@gmail.com")
print(dir(wizard_1))
    #This shows all methods and attributes of the instance