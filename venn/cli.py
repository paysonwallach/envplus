#!/usr/bin/env python3

import importlib
import inspect
import pkgutil
import os

import cleo

import venn.commands
import venn.pathfile
import venn.utils

if "VIRTUAL_ENV" not in os.environ:
    console = cleo.io.ConsoleIO()
    text = (
        "$VIRTUAL_ENV missing. It seems you're not currently in an active "
        "virtual environment."
    )
    styled_text = "<{0}>{1}</{0}>".format("error", text)

    console.error_line(styled_text)

    exit(1)


def get_pathfile_path(pathfile_name="_venn.pth"):
    sp_dir = venn.utils.get_site_packages_dir(os.environ["VIRTUAL_ENV"])
    pathfile_path = os.path.join(sp_dir, pathfile_name)

    return pathfile_path


def main():
    app = cleo.Application("venn", "0.2.0", complete=True)
    pf = venn.pathfile.PathFile(get_pathfile_path())
    for _, name, _ in pkgutil.walk_packages(venn.commands.__path__):
            full_name = '.'.join([venn.commands.__name__, name])
            module = importlib.import_module(full_name)

            for name, member in inspect.getmembers(module, inspect.isclass):
                if issubclass(member, cleo.Command):
                    app.add(member(pf))

    app.run()


if __name__ == "__main__":
    main()
