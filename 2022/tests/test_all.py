import importlib

import pandas as pd
import pytest
from click.testing import CliRunner


@pytest.mark.parametrize("day", [1])
@pytest.mark.parametrize("part", ["a", "b"])
@pytest.mark.parametrize("test", [True, False])
def test_one_puzzle(day: int, part: str, test: bool):
    mod = importlib.import_module(f"code.day_{day:02}")
    input_file = f"data/day_{day:02}" + ("_test" if test else "") + ".txt"
    num_result = read_result(day, part, test)

    runner = CliRunner()
    run_result = runner.invoke(mod.main, ["--part", part, input_file])
    assert run_result.exit_code == 0
    assert int(run_result.output) == num_result


def read_result(day: int, part: str, test: bool) -> int:
    df = pd.read_csv("data/outputs.csv", index_col=0)
    col = part + ("_test" if test else "")
    return df.loc[day, col]
