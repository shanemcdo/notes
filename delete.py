#!/usr/bin/env python3

import os
from sys import argv
from main import NOTE_FOLDER_PATH

def parse_argv() -> ("relative_paths", "rm_args"):
    """ Parse argv into something more usable
    :returns: a tuple of a list of relative_paths and args to pass into rm command
    """
    _ = argv.pop(0)
    rm_args = ""
    for item in argv:
        if item.startswith("-"):
            rm_args += item + " "
    for item in rm_args.split():
        argv.remove(item)
    if len(argv) < 1:
        raise(Exception("Too few arguments"))
    return [os.path.normpath(arg) for arg in argv], rm_args

def remove_file(relative_paths, rm_args) -> None:
    """ remove file selected with rm_args
    :relative_paths: paths to files to remove 
    :rm_args: args to pass to rm
    """
    paths = []
    for relative_path in relative_paths:
        path = os.path.join(NOTE_FOLDER_PATH, relative_path)
        if not os.path.exists(path):
            path += ".txt"
        paths.append(path)
    os.system("rm " + " ".join(paths) + " " + rm_args)

def print_usage() -> None:
    """Print the correct usage of the command"""
    print(
            "Usage of command:\n" +
            "\tnd {file path(s)} {flags(optional)}\n" +
            "\t\tSee rm --help for info on flags"
        )

def main():
    try:
        relative_paths, rm_args = parse_argv()
    except Exception as e:
        print("Error: " + str(e))
        print_usage()
        return
    remove_file(relative_paths, rm_args)


if __name__ == "__main__":
    main()
