# Dunder Methods
    # Marked by a __ before and after the text.
    # Used a python function on object created through the class
class Toy():
    def __init__(self, colour):
        self.colour = colour 
    
    def __str__(self):
        return(self.colour)
    
action_figure = Toy("green")
print(action_figure.__str__())
print(str(action_figure))