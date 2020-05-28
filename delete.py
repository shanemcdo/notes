import os
from sys import argv
from main import NOTE_FOLDER_PATH

def parse_argv() -> ("folder_name", "rm_args"):
    """ Parse argv into something more usable
    :returns: a tuple of folder name and args to pass into rm command
    """
    _ = argv.pop(0)
    rm_args = ""
    for item in argv:
        if item.startswith("-"):
            rm_args += item + " "
    for item in rm_args.split():
        argv.remove(item)
    if len(argv) > 1:
        raise(Exception("Too many arguments"))
    elif len(argv) < 1:
        raise(Exception("Too few arguments"))
    return argv[0], rm_args

def remove_file(folder_name, rm_args) -> None:
    pass

def main():
    try:
        folder_name, rm_args = parse_argv()
    except Exception as e:
        print("Error: " + str(e))
        return


if __name__ == "__main__":
    main()
