import os
from sys import argv
from main import NOTE_FOLDER_PATH

def parse_argv() -> ("file_name", "rm_args"):
    """ Parse argv into something more usable
    :returns: a tuple of file name and args to pass into rm command
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
    file_name = argv[0]
    return file_name, rm_args

def remove_file(file_name, rm_args) -> None:
    """ remove file selected with rm_args
    :file_name: file to remove 
    :rm_args: args to pass to rm
    """
    path = NOTE_FOLDER_PATH + file_name
    os.system("rm " + path + " " + rm_args)

def print_usage() -> None:
    """Print the correct usage of the command"""
    print(
            "Usage of command:\n"+
            "\tnd {file path} {flags(optional)}\n" +
            "\t\tSee rm --help for info on flags"
        )

def main():
    try:
        file_name, rm_args = parse_argv()
    except Exception as e:
        print("Error: " + str(e))
        print_usage()
        return
    remove_file(file_name, rm_args)


if __name__ == "__main__":
    main()
