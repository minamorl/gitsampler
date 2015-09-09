import sys
import os
from gitsampler import utils


def test_argparser():
    parser = utils.setup_argparser()
    assert parser.parse_args(
        "repo1 repo2 repo3 --output hoge.txt".split(' ')).output == "hoge.txt"
    assert parser.parse_args(
        "--load any_filename".split(' ')).load == "any_filename"
    assert parser.parse_args(
        "repo1 repo2 repo3".split(' ')).repos == ["repo1", "repo2", "repo3"]
