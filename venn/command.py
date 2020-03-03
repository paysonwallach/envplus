#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#

import os
import sys

import cleo

import venn.exceptions


class BaseCommand(cleo.Command):
    def get_pathfile_path(self, pathfile_name="_venn.pth"):
        try:
            sp_dir = venn.utils.get_site_packages_dir(os.environ["VIRTUAL_ENV"])
        except KeyError as e:
            raise venn.exceptions.NoVirtualEnvironment(e)
        pathfile_path = os.path.join(sp_dir, pathfile_name)

        return pathfile_path

    def handle(self):
        try:
            self.pf = venn.pathfile.PathFile(self.get_pathfile_path())
        except venn.exceptions.NoVirtualEnvironment:
            self.add_style("exception", fg="red")
            self.add_style("bold", fg="red", options="bold")

            self.line(
                "\n<exception>"
                "<bold>$VIRTUAL_ENV</bold> is not set.\n"
                "Are you in an active virtual environment?"
                "</exception>"
            )

            sys.exit(1)
