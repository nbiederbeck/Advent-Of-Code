import numpy as np


def get_digits(number):
    number = np.array(number).reshape(-1, 1)
    stripped = np.asarray(number % np.logspace(1, 6, 6), dtype=np.int64)
    digits = np.asarray(stripped // np.logspace(0, 5, 6), dtype=np.int64)

    return digits


def is_increasing(digits):
    return np.all(np.diff(digits, axis=1) <= 0, axis=1)


def has_double(digits):
    return np.any(np.diff(digits, axis=1) == 0, axis=1)


def double_not_more(digits):
    diff = np.diff(digits)

    ddiff = np.diff(diff)

    a = diff.sum(axis=1) != 0
    c = diff.sum(axis=1) != 1
    b = ddiff.sum(axis=1) == 0

    return a & b & c


def is_password(number):
    digits = get_digits(number)

    return is_increasing(digits) & has_double(digits)


def is_strong_password(number):
    digits = get_digits(number)

    return is_increasing(digits) & has_double(digits) & double_not_more(digits)


def n_pw(puzzle, is_pw):
    rng = puzzle[0]
    start, stop = map(int, rng.split("-"))
    puzzle = np.arange(start, stop)
    return np.sum(is_pw(puzzle))


def number_of_passwords(puzzle):
    return n_pw(puzzle, is_password)


def number_of_strong_passwords(puzzle):
    return n_pw(puzzle, is_strong_password)
