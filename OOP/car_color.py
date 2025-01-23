class Color: 
    red = 0
    green = 0
    blue = 0

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    
    def __str__(self):
        return str(self.red) + "|" + str(self.green) + "|" + str(self.blue)    