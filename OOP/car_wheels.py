class Wheel:
    def __init__(self, is_winter, dimension):
        self.is_winter = is_winter # boolean
        self.dimesion = dimension # measured in inches

    def __str__(self):
        if self.is_winter == True:
            return "Winter wheel with: " + str(self.dimesion) + " inch radius"
        else:
            return "Summer wheel with: " + str(self.dimesion) + " inch radius"