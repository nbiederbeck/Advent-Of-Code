from dec01 import read_fuel


def print_solution(day, solution):
    print(f"December, {day}: {solution}")


def main():
    print_solution(1, read_fuel("data/01.dat"))


if __name__ == "__main__":
    main()
