import pytest
import os
import logging
from gitsampler import github
from gitsampler import utils

pytestmark = pytest.mark.usefixtures("cleandir")
logging.basicConfig(level=logging.DEBUG)


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


@pytest.mark.slowtest
def test_clone_from():
    sample_repo_full = "git@github.com:minamorl/minamorl.com.git"
    github.clone_from(sample_repo_full)


def test_read_log():
    log = logging.getLogger("test_read_log")
    sample_repo_full = "git@github.com:minamorl/minamorl.com.git"
    repo = github.clone_from(sample_repo_full)
    for msg in github.read_log(repo):
        log.debug(msg)
