from cars import Car

c_one = Car('Purple', 'Fiesta', 80, 0, 50)
c_two = Car('Green', 'Vectra', 70, 0, 70)

print(f"The first car is: {c_one.model}, the colour is {c_one.colour}, current speed is {c_one.currentSpeed} and {c_one.fuelLevel}% fuel")
print(f"The second car is: {c_two.model} the colour is {c_two.colour}, current speed is {c_two.currentSpeed} and {c_two.fuelLevel}% fuel")

c_one.accelerate(20)
print(f"{c_one.currentSpeed}")
print(f"Fuel is {c_one.fuelLevel}")
c_one.brake(10)
print(f"{c_one.currentSpeed}")
print(f"Fuel is {c_one.fuelLevel}")
c_one.accelerate(80)
print(f"{c_one.currentSpeed}")
print(f"Fuel is {c_one.fuelLevel}")
