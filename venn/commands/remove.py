#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#

from venn import command


class RemoveCommand(command.BaseCommand):
    """
    Remove environments from the active virtual environment

    remove
        {environments* : Virtual environments to remove from the currently-active environment}
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self):
        super().handle()

        environments = self.argument("environments")

        for environment in environments:
            self.pf.remove_env(environment)

        self.pf.save()
