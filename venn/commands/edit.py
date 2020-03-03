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

import venn.env

from venn import command


class EditCommand(command.BaseCommand):
    """
    Edit the active virtual environment

    edit
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self):
        super().handle()

        venn.env.execute(self.pf, [os.environ["EDITOR"], self.pf.filepath])
