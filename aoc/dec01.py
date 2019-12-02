def calculate_fuel(mass):
    return mass // 3 - 2


def calculate_fuel_for_fuel(mass):
    fuel = 0
    add_fuel = True
    while add_fuel:
        more_fuel = calculate_fuel(mass)
        if more_fuel > 0:
            fuel = fuel + more_fuel
            mass = more_fuel
        else:
            add_fuel = False
    return fuel


def read_fuel(file):
    with open(file, "r") as f:
        masses = f.readlines()
    fuels = [calculate_fuel(int(mass)) for mass in masses]
    return sum(fuels)


def read_fuel_with_fuel(file):
    with open(file, "r") as f:
        masses = f.readlines()
    fuels = [calculate_fuel_for_fuel(int(mass)) for mass in masses]
    return sum(fuels)
