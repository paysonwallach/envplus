
import os
import subprocess


def run_in_env(pf, args):
    env = os.environ.copy()
    paths = env["PATH"].split(":")
    bin_paths = pf.get_binpaths()
    new_paths = paths[:1] + bin_paths + paths[1:]
    env["PATH"] = ":".join(new_paths)
    sp = subprocess.Popen(args, env=env)
    out, err = sp.communicate()

    return out
