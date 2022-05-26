#!/usr/bin/env python3

import os
from sys import argv
from main import NOTE_FOLDER_PATH

def print_usage() -> None:
    """Print the correct usage of the command"""
    print(
            "Usage of command:\n"
            "\tnls A{file path(optional)} [flags]\n"
            "\t\tflags: flags to be passed into the ls program"
        )

def main():
    try:
        _ = argv.pop(0)
        folder_name = None
        flags = []
        for arg in argv:
            if arg.startswith('-'):
                flags.append(arg)
            elif folder_name is None:
                folder_name = arg
            else:
                raise RuntimeError('Too many arguments')
    except Exception as e:
        print("Error: " + str(e))
        print_usage()
        return
    path = NOTE_FOLDER_PATH
    if folder_name:
        path = os.path.join(path, folder_name)
    os.system(f'ls {" ".join(flags)} ' + path)


if __name__ == "__main__":
    main()
