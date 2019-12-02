def calculate_fuel(mass):
    return mass // 3 - 2


def read_fuel(file):
    with open(file, "r") as f:
        masses = f.readlines()
    fuels = [calculate_fuel(int(mass)) for mass in masses]
    return sum(fuels)
