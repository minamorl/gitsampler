import clint
from gitsampler import messages
from gitsampler import github
from functools import partialmethod


def main():
    args = clint.Args()
    repo_name = args.get(0)
    messages.downloading(repo_name)
    uri = github.extract_github_uri(repo_name)
    github.clone_from(uri)
    messages.done(repo_name)

if __name__ == "__main__":
    main()
