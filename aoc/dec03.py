from aoc.riddle import get_riddle

riddle = get_riddle(3)


def manhatten(x: int, y: int):
    return x + y


def crossing(wire0: str, wire1: str):
    x = 1
    y = 1000

    directions = {"R": +x, "L": -x, "U": +y, "D": -y}

    wire0 = wire0.split(",")
    wire1 = wire1.split(",")

    wirepath0 = [0]

    return
