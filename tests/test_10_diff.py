import json
import os
import typing

import pytest
from gendiff import generate_diff


def get_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "test_data", file_name)


def read(file_path):
    with open(file_path, "r") as f:
        result = f.read()
    return result


def get_file_data(file_name):
    return read(get_path(file_name)).strip()


result_stylish = get_file_data("result_stylish")
result_plain = get_file_data("result_plain")
result_json = get_file_data("result_json")

test_cases = ["yml", "json"]


@pytest.mark.parametrize("format", test_cases)
def test_generate_diff(format):
    file_path1 = get_path(f"file1.{format}")
    file_path2 = get_path(f"file2.{format}")

    assert isinstance(
        generate_diff, typing.Callable
    ), "gendiff.generate_diff must be function"
    assert generate_diff(file_path1, file_path2) == result_stylish
    assert generate_diff(file_path1, file_path2, "stylish") == result_stylish
    assert generate_diff(file_path1, file_path2, "plain") == result_plain
    data = generate_diff(file_path1, file_path2, "json")

    try:
        json.loads(data)
    except Exception as e:
        msg = (
            'json diff is not a valid json string, '
            'got error: "{}", got diff: {}'
        ).format(e, data)
        pytest.fail(msg)
