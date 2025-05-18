class Vehicle:
    def general_usage(self):
        print("general use : transporation")

class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specific use: commute to work, vacation with family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm Motor Cycle")
        self.wheels = 2
        self.has_roof = True

    def specific_usage(self):
        print("specific use: road trip, racing")

car = Car()
car.general_usage()
car.specific_usage()
print(car.wheels)

motor = MotorCycle()
motor.general_usage()
motor.specific_usage()
print(motor.has_roof)