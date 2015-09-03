import clint
import sys, os
from gitsampler import github, utils, messages

def _main(args):
    for repo_name in args.repos:
        if not args.silent:
            messages.downloading(repo_name)
        uri = github.extract_github_uri(repo_name)
        repo = github.clone_from(uri)

        for msg in github.read_log(repo):
            print(msg)
        if not args.silent:
            messages.done(repo_name)


def main():
    parser = utils.setup_argparser()
    args = parser.parse_args()

    if args.load:
        args.repos = utils.import_from_list(args.load)

    return _main(args)


if __name__ == "__main__":
    main()
