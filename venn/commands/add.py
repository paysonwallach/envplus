#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#

from venn import command


class AddCommand(command.BaseCommand):
    """
    Add environments to the active virtual environment

    add
        {environments* : Virtual environments to add to the currently-active environment}
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self):
        super().handle()

        environments = self.argument("environments")

        for environment in environments:
            self.pf.add_env(environment)

        self.pf.save()
