#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#

from venn import command


class PauseCommand(command.BaseCommand):
    """
    Temporarily remove environments from the active virtual environment

    pause
        {environments?* : Virtual environments to temporarily remove from the currently-active environment}
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self):
        super().handle()

        environments = self.argument("environments")

        for environment in [
            environment if len(environments) else self.pf.ls()
            for environment in environments
        ]:
            self.pf.pause_env(environment)

        self.pf.save()
