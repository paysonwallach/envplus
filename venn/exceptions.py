#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#


class VennException(Exception):
    """Base exception class."""

    pass


class NoVirtualEnvironment(VennException):
    """No virtual environment found."""

    pass
