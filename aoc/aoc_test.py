from aoc.dec01 import calculate_fuel, calculate_fuel_for_fuel
from aoc.dec02 import intcode, replace_input
from aoc.dec03 import crossing, manhatten


def test_01a():
    assert calculate_fuel(12) == 2
    assert calculate_fuel(14) == 2
    assert calculate_fuel(1969) == 654
    assert calculate_fuel(100756) == 33583


def test_01b():
    assert calculate_fuel_for_fuel(14) == 2
    assert calculate_fuel_for_fuel(1969) == 966
    assert calculate_fuel_for_fuel(100756) == 50346


def test_02a():
    assert intcode([1, 0, 0, 0, 99]) == 2
    assert intcode([2, 3, 0, 3, 99]) == 2
    assert intcode([2, 4, 4, 5, 99, 0]) == 2
    assert intcode([1, 1, 1, 4, 99, 5, 6, 0, 99]) == 30


def test_02b():
    assert replace_input([0, 1, 2], 10, 10) == ([0, 10, 10], 1010)


def test_03a():
    assert manhatten(3, 3) == 6
    assert crossing("R8,U5,L5,D3", "U7,R6,D4,L4") == 6
    assert (
        crossing(
            "R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"
        )
        == 159
    )
    assert (
        crossing(
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
        )
        == 135
    )
