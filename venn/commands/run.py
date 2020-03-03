#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#

import os

import venn.env

from venn import command


class RunCommand(command.BaseCommand):
    """
    Run a give command in the active virtual environment

    run
        {command* : Command to run in the currently-active virtual environment, with optional arguments}
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self):
        super().handle()

        cmd = self.argument("command")

        venn.env.execute(self.pf, [os.environ["SHELL"], "-c", "-i", " ".join(cmd)])
