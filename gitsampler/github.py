import git
from parse import parse


def extract_github_uri(uri):
    slashed = uri.split('@')
    if len(slashed) > 1:
        return uri

    return "git@github.com:{}.git".format(uri)


def abbr_github_uri(uri):
    return parse("git@github.com:{user}/{repo}.git", uri)["repo"]


def clone_from(repo_uri):
    repo_name = abbr_github_uri(repo_uri)
    git.Repo.clone_from(repo_uri, "/tmp/" + repo_name)
