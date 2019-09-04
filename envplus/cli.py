#!/usr/bin/env python

import argparse
import os
import subprocess
import sys

import envplus.pathfile
import envplus.helpers

if "VIRTUAL_ENV" not in os.environ:
    raise Exception(
        "$VIRTUAL_ENV missing. It seems you're not currently in a virtualenv."
    )
else:
    pass


def run_in_env(pf, args):
    env = os.environ.copy()
    paths = env["PATH"].split(":")
    bin_paths = pf.get_binpaths()
    new_paths = paths[:1] + bin_paths + paths[1:]
    env["PATH"] = ":".join(new_paths)
    sp = subprocess.Popen(args, env=env)
    out, err = sp.communicate()

    return out


def cmd_add(pf, args):
    for env in args.envs:
        pf.add_env(env)
    pf.save()


def cmd_rm(pf, args):
    for env in args.envs:
        pf.remove_env(env)
    pf.save()


def cmd_pause(pf, args):
    for env in [env if len(args.envs) else pf.ls()
                for env in args.envs]:
        pf.pause_env(env)
    pf.save()


def cmd_resume(pf, args):
    for env in [env if len(args.envs) else pf.ls_paused()
                for env in args.envs]:
        pf.resume_env(env)
    pf.save()


def cmd_ls(pf, args):
    active = set(pf.ls())
    paused = set(pf.ls_paused())
    envs = (paused if args.paused else active) or \
        ((paused or active) if args.all else set())
    out = "".join(env + "\n" for env in envs)

    sys.stdout.write(out)


def cmd_cat(pf, args):
    sys.stdout.write(pf.to_string())


def cmd_edit(pf, args):
    run_in_env(pf, [os.environ["EDITOR"], pf.filepath])


def cmd_path(pf, args):
    sys.stdout.write(pf.filepath + "\n")


def cmd_run(pf, args):
    run_in_env(pf, [os.environ["SHELL"], "-c", "-i", " ".join(args.cmd)])


def parse_args():
    parser = argparse.ArgumentParser(
        description="Combine your virtualenvs.", prog="envplus")
    subparsers = parser.add_subparsers(
        title="Subcommands",
        dest="command"
    )

    # envplus add
    parser_add = subparsers.add_parser("add")
    parser_add.add_argument(
        "envs",
        nargs="+",
        help="virtualenvs to add to current virtualenv's path"
    )

    # envplus rm
    parser_rm = subparsers.add_parser("rm")
    parser_rm.add_argument(
        "envs",
        nargs="+",
        help="virtualenvs to remove from current virtualenv's path"
    )

    # envplus pause
    parser_pause = subparsers.add_parser("pause")
    parser_pause.add_argument(
        "envs",
        nargs="*",
        help="virtualenvs to pause. Defaults to all."
    )

    # envplus resume
    parser_resume = subparsers.add_parser("resume")
    parser_resume.add_argument(
        "envs",
        nargs="*",
        help="virtualenvs to resume. Defaults to all."
    )

    # envplus ls
    parser_ls = subparsers.add_parser("ls")
    parser_ls.add_argument(
        "--paused", "-p",
        action="store_true",
        help="Show paused virtualenvs instead of active ones."
    )
    parser_ls.add_argument(
        "--all", "-a",
        action="store_true",
        help="Show paused *and* active virtualenvs"
    )

    # envplus run
    parser_run = subparsers.add_parser("run")
    parser_run.add_argument(
        "cmd",
        nargs=argparse.REMAINDER,
        help="Command to run, with optional arguments."
    )

    # envplus path
    subparsers.add_parser("path")

    # envplus cat
    subparsers.add_parser("cat")

    # envplus edit
    subparsers.add_parser("edit")

    args = parser.parse_args()

    return args


def get_pathfile_path(pathfile_name="_envplus.pth"):
    sp_dir = envplus.helpers.get_site_packages_dir(os.environ["VIRTUAL_ENV"])
    pathfile_path = os.path.join(sp_dir, pathfile_name)

    return pathfile_path


def dispatch_command(args):
    commands = {
        "run": cmd_run,
        "add": cmd_add,
        "rm": cmd_rm,
        "pause": cmd_pause,
        "resume": cmd_resume,
        "ls": cmd_ls,
        "cat": cmd_cat,
        "path": cmd_path,
        "edit": cmd_edit,
    }
    pf = envplus.pathfile.PathFile(get_pathfile_path())

    commands[args.command](pf, args)


def main():
    args = parse_args()

    dispatch_command(args)


if __name__ == "__main__":
    main()
