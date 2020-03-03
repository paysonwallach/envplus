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

import venn.command
import venn.commands
import venn.exceptions
import venn.pathfile
import venn.utils

from venn import __version__


class Application(cleo.Application):
    def __init__(self):
        super(Application, self).__init__("venn", __version__, complete=True)

        for _, name, _ in pkgutil.walk_packages(venn.commands.__path__):
            full_name = ".".join([venn.commands.__name__, name])
            module = importlib.import_module(full_name)

            for name, member in inspect.getmembers(module, inspect.isclass):
                if issubclass(member, venn.command.BaseCommand):
                    self.add(member())


if __name__ == "__main__":
    Application().run()
