from aoc.dec01 import read_fuel, read_fuel_with_fuel
from aoc.dec02 import read_intcode, find_word


def print_solution(day, solution):
    print(f"December, {day}: {solution}")


def main():
    print_solution("2b", find_word("data/02.dat"))
    print_solution("2a", read_intcode("data/02.dat"))
    print_solution("1b", read_fuel_with_fuel("data/01.dat"))
    print_solution("1a", read_fuel("data/01.dat"))


if __name__ == "__main__":
    main()
