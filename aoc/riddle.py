import requests


def get_riddle(day: int):
    res = requests.get(
        f"https://adventofcode.com/2019/day/{day}/input",
        cookies={
            "session": "53616c7465645f5f7ae36a022092039343425eeee5d2c4c6a0ad288a29097d8756cec3eb7a87a478f1d651e312d56a0f"
        },
    )

    lines = res.text.split()

    return lines
