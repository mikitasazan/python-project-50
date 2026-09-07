from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish

RENDERERS = {
    "stylish": format_stylish,
    "plain": format_plain,
    "json": format_json,
}


def format_diff(tree, format_name):
    try:
        renderer = RENDERERS[format_name]
    except KeyError:
        raise ValueError(f"Unknown format: '{format_name}'") from None
    return renderer(tree)
