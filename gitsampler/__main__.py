import clint
import sys, os
from gitsampler import github, utils, messages, redis
import json
import io

def _main(args):
    
    mio = io.StringIO()
    logs = []
    for repo_name in args.repos:
        messages.downloading(repo_name)
        uri = github.extract_github_uri(repo_name)
        repo = github.clone_from(uri)

        for l in github.read_log(repo_name, repo):
            logs.append(l)
            print(l["summary"])

        messages.done(repo_name)

    r = redis.get_redis()
    redis.save_all(r, logs)

def main():
    parser = utils.setup_argparser()
    args = parser.parse_args()

    if args.load:
        args.repos = utils.import_from_list(args.load)

    return _main(args)


if __name__ == "__main__":
    main()
