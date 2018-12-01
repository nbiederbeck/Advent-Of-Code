def main(path: str):
    offset = 0
    with open(path, "r") as f:
        for line in f:
            offset += int(line)
    return offset

def test_01_01():
    f = "./01/test_a1"
    assert main(f) == 3

def test_01_02():
    f = "./01/test_a2"
    assert main(f) == 0

def test_01_03():
    f = "./01/test_a3"
    assert main(f) == -6

if __name__ == "__main__":
    offset = main("./01/input_a")
    print(f"Day  1: {offset}")
