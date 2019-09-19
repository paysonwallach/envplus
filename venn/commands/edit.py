import os

import cleo

from . import common


class EditCommand(cleo.Command):
    """
    Edit the active virtual environment

    edit
    """

    def __init__(self, pf, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pf = pf

    def handle(self):
        common.run_in_env(
            self.pf,
            [os.environ["EDITOR"], self.pf.filepath]
        )
