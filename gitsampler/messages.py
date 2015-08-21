from clint.textui import colored


def downloading(repo_name):
    return print(
        colored.green(
            "Start downloading {} from github.com.. ".format(repo_name)))


def done(repo_name):
    return print(colored.green("done."))
