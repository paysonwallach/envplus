import os

from glob import glob


def get_site_packages_dir(envname):
    sections = [
        os.environ["WORKON_HOME"],
        envname,
        "lib",
        "*",
        "site-packages"
    ]
    joined = os.path.join(*sections)
    matching = glob(joined)
    return matching[0] if len(matching) else None

