#!/usr/bin/env python3
#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#
# This file incorporates work covered by the following copyright and permission
# notice:
#
#   The MIT License (MIT)
#
#   Copyright (c) 2014, Jeremy Singer-Vine
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#   THE SOFTWARE.
#

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
