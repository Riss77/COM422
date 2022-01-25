class Car:
    def __init__(self, colour, model, maxSpeed, currentSpeed, fuelLevel):
        self.colour = colour
        self.model = model
        self.maxSpeed = maxSpeed
        self.currentSpeed = currentSpeed
        self.fuelLevel = fuelLevel

    def accelerate(self, increase):
        if self.fuelLevel == 0:
            self.currentSpeed = 0
            print("Fuel is empty")
        elif self.currentSpeed + increase <= self.maxSpeed:
            self.currentSpeed += increase
        else:
            self.currentSpeed = self.maxSpeed

        if self.fuelLevel - 1 >= 1:
            self.fuelLevel -= 1

    def brake(self, decrease):
        if self.currentSpeed - decrease >= 0:
            self.currentSpeed = self.currentSpeed - decrease

    def refuel(self, amount):
        if self.fuelLevel + amount <= 100:
            self.fuelLevel = self.fuelLevel + amount
        else:
            self.fuelLevel = 100
