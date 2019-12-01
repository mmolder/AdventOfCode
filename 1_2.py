import math

def required_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    return fuel + required_fuel(fuel)

with open("input_1_1.csv", 'r') as file:
    fuel_sum = 0
    for row in file:
        fuel_sum += required_fuel(int(row))
    print(fuel_sum)