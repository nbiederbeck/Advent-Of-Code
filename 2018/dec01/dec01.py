def a(path: str):
    offset = 0
    with open(path, "r") as f:
        for line in f:
            offset += int(line)
    return offset


def b(path: str):
    offset = 0
    frequencies = {offset}
    while True:
        with open(path, "r") as f:
            for line in f:
                offset += int(line)
                if offset in frequencies:
                    return offset
                frequencies.add(offset)


def test_a1():
    f = "./dec01/test_a1"
    assert a(f) == 3


def test_a2():
    f = "./dec01/test_a2"
    assert a(f) == 0


def test_a3():
    f = "./dec01/test_a3"
    assert a(f) == -6


def test_b1():
    f = "./dec01/test_b1"
    assert b(f) == 2


def test_b2():
    f = "./dec01/test_b2"
    assert b(f) == 0


def test_b3():
    f = "./dec01/test_b3"
    assert b(f) == 10


def test_b4():
    f = "./dec01/test_b4"
    assert b(f) == 5


def test_b5():
    f = "./dec01/test_b5"
    assert b(f) == 14


if __name__ == "__main__":
    print(f"Day  1 (a): {a('./dec01/input_a')}")
    print(f"Day  1 (b): {b('./dec01/input_a')}")
