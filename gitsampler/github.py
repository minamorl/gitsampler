import git
import os
from parse import parse
from gitsampler import utils


def extract_github_uri(uri):
    slashed = uri.split('@')
    if len(slashed) > 1:
        return uri

    return "git@github.com:{}.git".format(uri)


def abbr_github_uri(uri):
    return parse("git@github.com:{user}/{repo}.git", uri)["repo"]


def clone_from(repo_uri):
    repo_name = abbr_github_uri(repo_uri)
    dest = os.path.join(os.getcwd(), "misc/repos/", repo_name)
    return git.Repo.clone_from(repo_uri, dest)


def clone_from_file(file):
    def _clone_from_list(list):
        for r in list:
            repo_uri = extract_github_uri(r)
            repo_name = abbr_github_uri(repo_uri)
            dest = os.path.join(os.getcwd(), "misc/repos/", repo_name)
            git.Repo.clone_from(repo_uri, dest)

    list = utils.import_from_list(file)
    _clone_from_list(list)


def read_log(repo):
    commits = repo.iter_commits('master', max_count=100)

    return (c.message.rstrip("\n") for c in commits)
