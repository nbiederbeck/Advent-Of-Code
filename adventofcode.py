from aoc.riddle import get_riddle
from aoc.dec01 import read_fuel, read_fuel_with_fuel
from aoc.dec02 import read_intcode, find_word
from aoc.dec03 import crossing
from aoc.dec04 import number_of_passwords, number_of_strong_passwords


def print_solution(day, solution):
    print(f"December, {day}: {solution}")


def main():
    print_solution("4b", number_of_strong_passwords(get_riddle(4)))
    print_solution("4a", number_of_passwords(get_riddle(4)))
    print_solution("3a", crossing(*get_riddle(3)))
    print_solution("2b", find_word("data/02.dat"))
    print_solution("2a", read_intcode("data/02.dat"))
    print_solution("1b", read_fuel_with_fuel("data/01.dat"))
    print_solution("1a", read_fuel("data/01.dat"))


if __name__ == "__main__":
    main()
