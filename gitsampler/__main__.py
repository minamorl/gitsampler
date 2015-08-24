import clint
from gitsampler import messages
from gitsampler import github
from functools import partialmethod
import argparse


def main():
    parser = argparse.ArgumentParser(description="auto cloaning github repos")
    parser.add_argument('--load')
    parser.add_argument('repos', nargs='+')
    
    args = parser.parse_args()
    if args.load:
        github.clone_from_file(args.load)

    else:
        for repo_name in args.repos:
            messages.downloading(repo_name)
            uri = github.extract_github_uri(repo_name)
            github.clone_from(uri)
            messages.done(repo_name)


if __name__ == "__main__":
    main()
