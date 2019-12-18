import requests


def get_riddle(day: int):
    res = requests.get(
        f"https://adventofcode.com/2019/day/{day}/input",
        cookies={
            "session": "53616c7465645f5f0c0c69777b7b49cc76b78f56184ad64aacf97cef49b7cb37ba09ff718cc1d199170e9933b7409ff2"
        },
    )

    lines = res.text.split()

    return lines
