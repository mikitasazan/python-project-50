"""Reading and parsing configuration files.

Format is picked by file extension; parsing itself has no idea a
filesystem exists — it only turns a stream of bytes into a plain dict.
"""

import json
import os

import yaml


def detect_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lstrip(".").lower()


def parse(stream, file_format):
    if file_format == "json":
        return json.load(stream)
    if file_format in ("yml", "yaml"):
        return yaml.safe_load(stream)
    raise ValueError(f"Unsupported file format: '.{file_format}'")


def load_data(file_path):
    file_format = detect_format(file_path)
    with open(file_path) as stream:
        return parse(stream, file_format)
