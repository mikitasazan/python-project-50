"""Building the diff as a tree, independent of any output format.

Every node carries a 'type' and a 'key'; leaves carry 'value' (or
'value1'/'value2' when changed), branches carry 'children'. The tree
knows nothing about how it will be printed later.
"""

ADDED = "added"
DELETED = "deleted"
UNCHANGED = "unchanged"
CHANGED = "changed"
NESTED = "nested"
ROOT = "root"


def build_diff(data1, data2):
    return {"type": ROOT, "children": build_children(data1, data2)}


def build_children(data1, data2):
    keys = sorted(set(data1) | set(data2))
    return [build_node(key, data1, data2) for key in keys]


def build_node(key, data1, data2):
    if key not in data1:
        return {"key": key, "type": ADDED, "value": data2[key]}

    if key not in data2:
        return {"key": key, "type": DELETED, "value": data1[key]}

    value1, value2 = data1[key], data2[key]

    if isinstance(value1, dict) and isinstance(value2, dict):
        return {
            "key": key,
            "type": NESTED,
            "children": build_children(value1, value2),
        }

    if value1 == value2:
        return {"key": key, "type": UNCHANGED, "value": value1}

    return {"key": key, "type": CHANGED, "value1": value1, "value2": value2}
