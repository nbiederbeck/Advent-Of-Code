def main():
    s = a('dec03/input_a')
    print(f"Day  3 (a): {s}")
    s = b('dec03/input_a')
    print(f"Day  3 (b): {s}")


def a(path: str):
    """Scan a grid and add 1 if claimed"""
    n = 1000
    grid = [[0 for _ in range(n)] for _ in range(n)]
    with open(path, 'r') as f:
        for line in f:
            _, l, t, w, h = parse(line)
            for i in range(l, l + w):
                for j in range(t, t + h):
                    grid[i][j] += 1
    claimed_greater_1 = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            claimed_greater_1 += grid[i][j] > 1
    return claimed_greater_1


def b(path: str):
    """Scan grid and add 1 only if whole claim is unclaimed"""
    n = 1000
    grid = [[0 for _ in range(n)] for _ in range(n)]
    # set numbers of id in grid
    with open(path, 'r') as f:
        for line in f:
            idnr, l, t, w, h = parse(line)
            for i in range(l, l + w):
                for j in range(t, t + h):
                    grid[i][j] += idnr
    # check if full claim is only claimed once
    with open(path, 'r') as f:
        for line in f:
            single_claimed = True
            idnr, l, t, w, h = parse(line)
            for i in range(l, l + w):
                for j in range(t, t + h):
                    single_claimed *= grid[i][j] == idnr
            if single_claimed:
                return idnr


def parse(claim: str):
    """Input claim of elves and return the orientation and size as tuple"""
    claims = claim.split()
    idnr = int(claims[0][1:])
    lefttop = claims[2].replace(',', ' ').replace(':', ' ')
    widthheight = claims[3].replace('x', ' ')
    left = int(lefttop.split()[0])
    top = int(lefttop.split()[1])
    width = int(widthheight.split()[0])
    height = int(widthheight.split()[1])
    return idnr, left, top, width, height


def test_a1():
    test = "dec03/test_a"
    sol = 4
    assert a(test) == sol


def test_b1():
    test = "dec03/test_a"
    sol = 3
    assert b(test) == sol


if __name__ == "__main__":
    main()
