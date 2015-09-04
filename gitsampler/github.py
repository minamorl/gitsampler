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


def clone_from(repo_uri, dest=None):
    repo_name = abbr_github_uri(repo_uri)
    dest = dest or os.path.join(os.getcwd(), "misc/repos/", repo_name)
    if os.path.exists(dest):
        return git.Repo(dest)
    return _clone_from(repo_uri, dest)


def _clone_from(repo_uri, dest):
    repo_name = abbr_github_uri(repo_uri)
    return git.Repo.clone_from(repo_uri, dest)


def parse_commit(project_name, commit):
    return {
        "project": project_name,
        "author": commit.author.name.rstrip("\n"),
        "summary": commit.summary.rstrip("\n")
    }


def read_log(project_name, repo):
    commits = repo.iter_commits('master', max_count=3000)
    return (parse_commit(project_name, c) for c in commits)
