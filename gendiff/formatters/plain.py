"""A plain-English description of the diff, one line per change.

Unchanged nodes produce no line at all; a nested branch just extends
the dotted path handed down to its children.
"""


def stringify(value):
    if isinstance(value, bool):
        return "true" if value else "false"

    if value is None:
        return "null"

    if isinstance(value, (dict, list)):
        return "[complex value]"

    if isinstance(value, str):
        return f"'{value}'"

    return str(value)


def render(node, path):
    node_type = node["type"]

    if node_type == "root":
        lines = []
        for child in node["children"]:
            lines.extend(render(child, path))
        return lines

    full_path = f"{path}{node['key']}"

    if node_type == "nested":
        lines = []
        for child in node["children"]:
            lines.extend(render(child, f"{full_path}."))
        return lines

    if node_type == "added":
        value = stringify(node["value"])
        return [f"Property '{full_path}' was added with value: {value}"]

    if node_type == "deleted":
        return [f"Property '{full_path}' was removed"]

    if node_type == "changed":
        old = stringify(node["value1"])
        new = stringify(node["value2"])
        return [f"Property '{full_path}' was updated. From {old} to {new}"]

    if node_type == "unchanged":
        return []

    raise ValueError(f"Unknown node type: '{node_type}'")


def format_plain(tree):
    return "\n".join(render(tree, ""))
