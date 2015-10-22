import clint
import sys, os
from gitsampler import github, utils, messages, redis
import json
import io
import asyncio
import itertools


async def task(repo_name):
    messages.downloading(repo_name)
    uri = github.extract_github_uri(repo_name)
    repo = github.clone_from(uri)
    logs = list(github.read_log(repo_name, repo))
    for l in logs:
        print(l["summary"])
    messages.done(repo_name)
    return logs


async def _main(args):
    
    mio = io.StringIO()
    coroutines = (task(repo_name) for repo_name in args.repos)
    logs = list(itertools.chain(*await asyncio.gather(*coroutines)))
    r = redis.get_redis()
    redis.save_all(r, logs)

def main():
    parser = utils.setup_argparser()
    args = parser.parse_args()

    if args.load:
        args.repos = utils.import_from_list(args.load)

    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_main(args))
    loop.close()


if __name__ == "__main__":
    main()
