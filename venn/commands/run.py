#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#

import os

import cleo

from . import common


class RunCommand(cleo.Command):
    """
    Run a give command in the active virtual environment

    run
        {command* : Command to run in the currently-active virtual environment, with optional arguments}
    """

    def __init__(self, pf, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pf = pf

    def handle(self):
        command = self.argument("command")

        common.run_in_env(
            self.pf,
            [os.environ["SHELL"], "-c", "-i", " ".join(command)]
        )
