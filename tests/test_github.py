from gitsampler import github
from gitsampler import utils
import os

import pytest


def test_extract_github_uri():
    sample_repo_abbr = "minamorl/minamorl.com"
    r1 = github.extract_github_uri(sample_repo_abbr)

    sample_repo_full = "git@github.com:minamorl/minamorl.com.git"
    r2 = github.extract_github_uri(sample_repo_full)
    assert r1 == r2


def test_abbr_github_uri():
    sample_repo_full = "git@github.com:minamorl/dummy.git"
    r1 = github.abbr_github_uri(sample_repo_full)
    assert r1 == "dummy"


def test_clone_from():
    sample_repo_full = "git@github.com:minamorl/minamorl.com.git"
    github.clone_from(sample_repo_full)


def test_clone_from_file():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    sample_file = os.path.join(current_dir, 'misc/test-repos')
    github.clone_from_file(sample_file)
