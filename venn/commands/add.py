#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#

import cleo


class AddCommand(cleo.Command):
    """
    Add environments to the active virtual environment

    add
        {environments* : Virtual environments to add to the currently-active environment}
    """

    def __init__(self, pf, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pf = pf

    def handle(self):
        environments = self.argument("environments")

        for environment in environments:
            self.pf.add_env(environment)

        self.pf.save()
