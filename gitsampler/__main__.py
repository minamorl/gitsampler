import clint
from . import github, utils, messages

from functools import partialmethod


def main():
    parser = utils.argparser()
    args = parser.parse_args()

    if args.load:
        args.repos = utils.import_from_list(args.load)

    for repo_name in args.repos:
        messages.downloading(repo_name)
        uri = github.extract_github_uri(repo_name)
        repo = github.clone_from(uri)

        for msg in github.read_log(repo):
            print(msg)

        messages.done(repo_name)


if __name__ == "__main__":
    main()
