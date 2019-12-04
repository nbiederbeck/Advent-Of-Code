import numpy as np


def is_password(number):
    number = np.array(number).reshape(-1, 1)

    stripped = np.asarray(number % np.logspace(1, 6, 6), dtype=np.int64)
    digits = np.asarray(stripped // np.logspace(0, 5, 6), dtype=np.int64)

    increasing = np.all((np.diff(digits, axis=1) <= 0), axis=1)

    double = np.any(digits[:, 1:] == digits[:, :-1], axis=1)

    return double & increasing


def is_strong_password(number: int):
    is_pw = is_password(number)

    number = np.array(number).reshape(-1, 1)

    stripped = np.asarray(number % np.logspace(1, 6, 6), dtype=np.int64)
    digits = np.asarray(stripped // np.logspace(0, 5, 6), dtype=np.int64)

    strong = np.diff(np.diff(digits)).sum(axis=1) == 0

    return strong & is_pw


def n_pw(puzzle, is_pw):
    rng = puzzle[0]
    start, stop = map(int, rng.split("-"))
    puzzle = np.arange(start, stop + 1)
    return np.sum(is_pw(puzzle))


def number_of_passwords(puzzle):
    return n_pw(puzzle, is_password)


def number_of_strong_passwords(puzzle):
    return n_pw(puzzle, is_strong_password)
