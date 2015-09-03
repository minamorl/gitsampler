import sys
import os
from gitsampler import utils


def test_import_repos_list():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    sample_file = os.path.join(current_dir, 'misc/test-repos')
    sample = utils.import_from_list(sample_file)
    assert len(sample) == 5


def test_argparser():
    parser = utils.setup_argparser()
    assert parser.parse_args(
        "repo1 repo2 repo3 --silent".split(' ')).silent == True
    assert parser.parse_args(
        "--load any_filename".split(' ')).load == "any_filename"
    assert parser.parse_args(
        "repo1 repo2 repo3".split(' ')).repos == ["repo1", "repo2", "repo3"]
