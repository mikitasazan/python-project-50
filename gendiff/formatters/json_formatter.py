"""The 'json' output format: the raw diff tree, JSON-encoded as is."""

import json


def format_json(tree):
    return json.dumps(tree, indent=2)
