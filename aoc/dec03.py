from aoc.riddle import get_riddle

riddle = get_riddle(3)


def manhatten(x: int, y: int):
    return x + y


def crossing(wire0: str, wire1: str):
    start = 0

    wire0 = wire0.split(",")
    wire1 = wire1.split(",")

    x = 1
    y = 1000000
    dirs = {"R": +x, "L": -x, "D": -y, "U": +y}

    wirepaths = ({start}, {start})

    for j, wire in enumerate([wire0, wire1]):
        point = start
        for path in wire:
            d = path[0]
            a = int(path[1:])
            for i in range(a):
                point += dirs[d]
                wirepaths[j].add(point)
                # wirepaths[j].append(wirepaths[j][-1] + )

    wp0, wp1 = wirepaths

    crossings = wp0.intersection(wp1)

    dists = set()
    for point in crossings:
        dist = manhatten(abs(point) // y, abs(point) % y)
        dists.add(dist)

    dists.pop()

    return min(dists)
