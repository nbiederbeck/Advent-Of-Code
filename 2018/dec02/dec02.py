def main():
    print(f"Day  2 (a): {run_a()}")
    print(f"Day  2 (b): {b('./dec02/input_a')}")


def run_a():
    twos = 0
    threes = 0
    with open("dec02/input_a") as f:
        for line in f:
            sol = a(line)
            twos += sol[0]
            threes += sol[1]
    return twos * threes


def a(string: str):
    """
    Returns
    -------
    (bool, bool):
        Tuple containing information if a single letter is contained
        (two, three) times in the input string.
    """
    chars = dict()
    for c in string:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    return (2 in chars.values(), 3 in chars.values())


def b(path: str):
    f = []
    with open(path, "r") as tmp:
        for a in tmp:
            f.append(a)
    for i, a in enumerate(f):
        for c in f[i + 1:]:
            for i in range(len(c)):
                if (a[:i] + a[i + 1:] == c[:i] + c[i + 1:]):
                    return (a[:i] + a[i + 1:]).strip()


def test_a1():
    test = "abcdef"
    sol = False, False
    assert a(test) == sol


def test_a2():
    test = "bababc"
    sol = True, True
    assert a(test) == sol


def test_a3():
    test = "abbcde"
    sol = True, False
    assert a(test) == sol


def test_a4():
    test = "abcccd"
    sol = False, True
    assert a(test) == sol


def test_a5():
    test = "aabcdd"
    sol = True, False
    assert a(test) == sol


def test_a6():
    test = "abcdee"
    sol = True, False
    assert a(test) == sol


def test_a7():
    test = "ababab"
    sol = False, True
    assert a(test) == sol


def test_b1():
    test = "./dec02/test_b"
    sol = "fgij"
    assert b(test) == sol


if __name__ == "__main__":
    main()
