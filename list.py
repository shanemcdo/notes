import os
from sys import argv
from main import NOTE_FOLDER_PATH

def parse_argv() -> None or "folder_name":
    """ Parse argv into something more usable
    :returns: name of the folder to be searched or an empty string
    """
    _ = argv.pop(0)
    length = len(argv)
    if length == 0:
        return ""
    elif length > 1:
        raise(Exception("Too many arguments"))
    return os.path.normpath(argv[0])

def print_usage() -> None:
    """Print the correct usage of the command"""
    print(
            "Usage of command:\n"+
            "\tnls {file path(optional)}"
        )

def main():
    try:
        folder_name = parse_argv()
    except Exception as e:
        print("Error: " + str(e))
        print_usage()
        return
    os.system('ls ' + os.path.join(NOTE_FOLDER_PATH, folder_name))


if __name__ == "__main__":
    main()
