import argparse


def build_parser():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format", default="stylish", help="set format of output"
    )
    return parser


def parse_args(argv=None):
    return build_parser().parse_args(argv)
