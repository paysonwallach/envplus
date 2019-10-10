#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#

import cleo

class PathCommand(cleo.Command):
    """
    Print the $PATH of the active virtual environment

    path
    """

    def __init__(self, pf, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pf = pf

    def handle(self):
        self.line(self.pf.filepath)
