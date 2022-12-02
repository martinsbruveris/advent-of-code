import importlib

import pandas as pd
import pytest
from click.testing import CliRunner


def solved_puzzles(year=None):
    solved = {2015: [1], 2021: range(1, 11), 2022: range(1, 3)}
    if year is not None:
        solved_list = [(year, day) for day in solved[year]]
    else:
        solved_list = [
            (year, day) for year, day_list in solved.items() for day in day_list
        ]
    return solved_list


@pytest.mark.parametrize("test", [True, False])
@pytest.mark.parametrize("part", ["a", "b"])
@pytest.mark.parametrize("year, day", solved_puzzles())
def test_one_puzzle(year: int, day: int, part: str, test: bool):
    mod = importlib.import_module(f"aoc.aoc_{year}.day_{day:02}")
    input_file = f"data/{year}/day_{day:02}" + ("_test" if test else "") + ".txt"
    exp_result = read_result(year, day, part, test)

    runner = CliRunner()
    run_result = runner.invoke(mod.main, ["--part", part, input_file])
    # There is always a `\n` at the end, leading to an empty string when we split.
    result = run_result.output.split("\n")[-2]
    assert run_result.exit_code == 0
    assert int(result) == exp_result


def read_result(year: int, day: int, part: str, test: bool) -> int:
    df = pd.read_csv(f"data/{year}/outputs.csv", index_col=0)
    col = part + ("_test" if test else "")
    return df.loc[day, col]
