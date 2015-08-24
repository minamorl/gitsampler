def import_from_list(file):
    with open(file) as f:
        return f.read().splitlines()
