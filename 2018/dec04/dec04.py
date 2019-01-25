from pprint import pprint


def main():
    f = 'dec04/input'
    sol = a(f)
    print(f"Day  4 (a): {sol}")


def a(path: str):
    f = open(path, 'r')
    times = []
    for line in f:
        splits = line.split()
        year = int(splits[0][1:5])
        month = int(splits[0][6:8])
        day = int(splits[0][9:11])
        hour = int(splits[1][:2])
        minute = int(splits[1][3:5])
        try:
            idnr = int(splits[3][1:])
        except ValueError:
            pass
        if splits[2] == "falls":
            action = 1
        elif splits[2] == "wakes":
            action = 2
        else:
            action = 0
        times.append([month, day, minute, idnr, action])
    f.close()
    times.sort()

    guards = {}
    for row in times:
        idn = row[-2]
        action = row[-1]
        min_asleep = row[2]
        if idn not in guards and action == 0:
            guards[idn] = {}
            for i in range(60):
                guards[idn][i] = 0
        elif action == 1:
            guards[idn][min_asleep] = 1

    pprint(guards)
    return 0


def test_a():
    f = 'dec04/test_a'
    assert a(f) == 240


if __name__ == "__main__":
    main()
