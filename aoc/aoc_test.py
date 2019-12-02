from aoc.dec01 import calculate_fuel, calculate_fuel_for_fuel
from aoc.dec02 import intcode


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
