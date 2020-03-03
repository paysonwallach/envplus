#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#

from venn import command


class ResumeCommand(command.BaseCommand):
    """
    Add temporarily-removed environments back to the active virtual environment

    resume
        {environments?* : Paused virtual environments to add back to the currently-active environment}
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self):
        super().handle()

        environments = self.argument("environments")

        for environment in [
            environment if len(environments) else self.pf.ls_paused()
            for environment in environments
        ]:
            self.pf.resume_env(environment)

        self.pf.save()
