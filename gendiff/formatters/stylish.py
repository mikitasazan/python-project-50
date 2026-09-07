"""The default, human-readable diff format.

Indentation is driven purely by depth: a spec character ('+ ', '- ' or
two spaces) is drawn depth*4-2 spaces in, so that together with the
two-character marker every key at a given depth lines up at depth*4.
"""


def marker_indent(depth):
    return " " * (depth * 4 - 2)


def key_indent(depth):
    return marker_indent(depth) + "  "


def stringify(value, depth):
    if isinstance(value, bool):
        return "true" if value else "false"

    if value is None:
        return "null"

    if isinstance(value, dict):
        lines = [
            f"{key_indent(depth + 1)}{key}: {stringify(value[key], depth + 1)}"
            for key in value
        ]
        body = "\n".join(lines)
        return f"{{\n{body}\n{key_indent(depth)}}}"

    return value


def render(node, depth):
    node_type = node["type"]

    if node_type == "root":
        body = "\n".join(render(child, depth + 1) for child in node["children"])
        return f"{{\n{body}\n}}"

    if node_type == "nested":
        body = "\n".join(render(child, depth + 1) for child in node["children"])
        indent = key_indent(depth)
        return f"{indent}{node['key']}: {{\n{body}\n{indent}}}"

    if node_type == "added":
        value = stringify(node["value"], depth)
        return f"{marker_indent(depth)}+ {node['key']}: {value}"

    if node_type == "deleted":
        value = stringify(node["value"], depth)
        return f"{marker_indent(depth)}- {node['key']}: {value}"

    if node_type == "changed":
        old = stringify(node["value1"], depth)
        new = stringify(node["value2"], depth)
        old_line = f"{marker_indent(depth)}- {node['key']}: {old}"
        new_line = f"{marker_indent(depth)}+ {node['key']}: {new}"
        return f"{old_line}\n{new_line}"

    if node_type == "unchanged":
        value = stringify(node["value"], depth)
        return f"{key_indent(depth)}{node['key']}: {value}"

    raise ValueError(f"Unknown node type: '{node_type}'")


def format_stylish(tree):
    return render(tree, 0)
