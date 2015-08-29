import argparse


def import_from_list(file):
    with open(file) as f:
        return f.read().splitlines()


def setup_argparser():
    parser = argparse.ArgumentParser(description="Github log viewer")
    parser.add_argument('--load')
    parser.add_argument('repos', nargs='*')
    return parser
