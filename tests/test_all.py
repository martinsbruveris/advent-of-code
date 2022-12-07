import importlib
from pathlib import Path

import pandas as pd
import pytest


def solved_puzzles():
    solved = {2015: [1], 2021: range(1, 19), 2022: range(1, 8)}
    solved_list = [(year, day) for year, day_list in solved.items() for day in day_list]
    return solved_list


@pytest.mark.parametrize("test", [True, False])
@pytest.mark.parametrize("part", ["a", "b"])
@pytest.mark.parametrize("year, day", solved_puzzles())
def test_one_puzzle(year: int, day: int, part: str, test: bool):
    mod = importlib.import_module(f"aoc.aoc_{year}.day_{day:02}")
    input_file = f"data/{year}/day_{day:02}" + ("_test" if test else "") + ".txt"
    exp_result = read_result(year, day, part, test)

    data = Path(input_file).read_text()
    result = mod.main(data, part)

    assert str(result) == exp_result


def read_result(year: int, day: int, part: str, test: bool) -> str:
    df = pd.read_csv(f"data/{year}/outputs.csv", index_col=0, dtype=str)
    col = part + ("_test" if test else "")
    return df.loc[day, col]
