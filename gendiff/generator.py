"""The whole pipeline in one place: read -> parse -> diff -> format.

Nothing else is allowed to live here — each step is delegated to a
module that knows only its own concern.
"""

from gendiff.diff_tree import build_diff
from gendiff.formatters import format_diff
from gendiff.parser import load_data


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)
    tree = build_diff(data1, data2)
    return format_diff(tree, format_name)
