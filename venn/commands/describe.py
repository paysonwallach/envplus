#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#

from venn import command


class DescribeCommand(command.BaseCommand):
    """
    Describe the active virtual environment

    describe
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self):
        super().handle()

        self.line(self.pf.to_string())
