class User:
    logged_in = True

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f"Attack with power {self.power}")

class Archer(User):
    def __init__(self, name, num_arrow):
        self.name = name
        self.num_arrow = num_arrow
    def fire_arrow(self):
        while self.num_arrow > 0:
            print(f"Firing {self.num_arrow}")
            self.num_arrow -= 1
            print(f"{self.num_arrow}'s left")
        else:
            print("No arrows left")

class HybridWarrior(Wizard, Archer):
    def __init__(self, name, power, num_arrow):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrow)

hb1 = HybridWarrior("Borg", 50, 2)
print(hb1.logged_in)
print(hb1.attack())
print(hb1.fire_arrow())

# HybridWarrior class inherits from the preious 3 