from gitsampler import github


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
