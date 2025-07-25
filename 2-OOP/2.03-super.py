# If we add a function to the User class below
class User:
    def __init__(self, email):
        self.email = email

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email) # refers to the parent class (User)
        self.name = name
        self.power = power 

wizard_1 = Wizard("Merlin", 60, "merlin@gmail.com")
print(wizard_1.email)