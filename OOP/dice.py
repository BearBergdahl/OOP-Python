import random

class Dice():
    value = 0
    def __init__(self, sides):
        self.sides = sides

    def __str__(self):
        if self.value:
            return f"This {self.sides}-ed dice rolled a " +str(self.value)
        else:
            return "This dice is not rolled"
    
    def roll(self):
        self.value = random.randint(1,self.sides)
        return self.value
    
"""
thirteen = Dice(13)
print(thirteen)
print(thirteen.roll())
print(thirteen)
"""