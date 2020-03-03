#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#

from venn import command


class ListCommand(command.BaseCommand):
    """
    List virtual environments

    list
        {--a|all : List all virtual environments, including paused ones}
        {--p|paused : List only virtual environments paused in the currently-active environment}
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self):
        super().handle()

        active = set(self.pf.ls())
        paused = set(self.pf.ls_paused())

        for environment in (paused if self.option("paused") else active) or (
            (paused or active) if self.option("all") else set()
        ):
            self.line(environment + "\n")
