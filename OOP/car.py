import car_color
import car_wheels

class Car:
    wheels = []
    def __init__(self, red, green, blue):
        self.color_of_car = car_color.Color(red, green,blue)
    
    def add_wheel(self, wheel):
        self.wheels.append(wheel)

    def __str__(self):
        temp_string = "A car with the color: " + str(self.color_of_car)
        for wheel in self.wheels:
            temp_string += "\n"
            temp_string += str(wheel)
        return temp_string


my_car = Car(10,10,10)

for i in range(4):
    my_car.add_wheel(car_wheels.Wheel(True, 18))

print(my_car)