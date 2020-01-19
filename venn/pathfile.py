#
# Venn
#
# Copyright (c) 2019 Payson Wallach
#
# Released under the terms of the Hippocratic License
# (https://firstdonoharm.dev/version/1/1/license.html)
#
# This file incorporates work covered by the following copyright and permission
# notice:
#
#   The MIT License (MIT)
#
#   Copyright (c) 2014, Jeremy Singer-Vine
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#   THE SOFTWARE.
#

import os
import re

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from venn.env import Env
from venn.utils import get_site_packages_dir

linebreak_pattern = re.compile(r"[\n\r]")


class PathFile(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.envs = self.load()

    def read_pathfile(self):
        if os.path.isfile(self.filepath):
            with open(self.filepath) as f:
                return f.read()
        else:
            return ""

    def load(self):
        raw = ""

        if os.path.isfile(self.filepath):
            with open(self.filepath) as f:
                raw = f.read()

        lines = [
            x.strip() for x in re.split(linebreak_pattern, raw) if x.strip()
        ]
        env_list = [Env.from_line(line) for line in lines]
        env_names = [env.name for env in env_list]
        envs = OrderedDict(zip(env_names, env_list))

        return envs

    def add_env(self, envname):
        sp_dir = get_site_packages_dir(envname)

        if not sp_dir:
            raise Exception("Could not find virtualenv named %s", envname)

        if envname in self.envs:
            del self.envs[envname]

        local_sp = os.path.split(self.filepath)[0]
        rel = os.path.relpath(sp_dir, local_sp)
        self.envs[envname] = Env(envname, rel)

    def check_env(self, envname):
        if not envname in self.envs:
            raise Exception("No virtualenv named %s", envname)

    def remove_env(self, envname):
        self.check_env(envname)
        del self.envs[envname]

    def pause_env(self, envname):
        self.check_env(envname)
        self.envs[envname].pause()

    def resume_env(self, envname):
        self.check_env(envname)
        self.envs[envname].resume()

    def to_string(self):
        lines = [env.to_string() for env in self.envs.values()]
        joined = "\n".join(lines)

        return joined + "\n"

    def save(self):
        with open(self.filepath, "w") as f:
            content = self.to_string()
            f.write(content)

    def ls(self):
        return [key for key, env in self.envs.items() if not env.paused]

    def ls_paused(self):
        return [key for key, env in self.envs.items() if env.paused]

    def get_binpaths(self):
        workon = os.environ["WORKON_HOME"]
        tmpl = os.path.join("{0}", "{1}", "bin")

        def to_binpath(envname):
            return tmpl.format(workon, envname)

        return [to_binpath(path) for path in self.ls()]
