import os
import re
import subprocess
from sys import argv

NOTE_FOLDER_PATH = "C:\\Users\\Shane\\Dropbox\\Desktop\\Coding\\python\\notes\\note_folder\\"

def parse_argv() -> ("relative_path", "gvim_flags", int):
    """ converts argv into a more usable format
    :returns: a tuple of the relative path name and the flags for gvim and the number of rotations to encode
    """
    _ = argv.pop(0)
    relative_paths = []
    gvim_flags = ""
    next_arg_is_n = False
    n = 0
    for arg in argv:
        if arg == '--rotn':
            next_arg_is_n = True
        elif arg.startswith('-'):
            gvim_flags += arg + " "
        elif next_arg_is_n:
            n = int(arg)
            next_arg_is_n = False
        else:
            if '.' not in arg:
                arg += ".txt"
            relative_paths.append(arg)
    length = len(relative_paths)
    if length < 1:
        raise(Exception("Too few arguments"))
    return relative_paths, gvim_flags, n

def open_file(relative_paths: list, gvim_flags: str, n: int) -> None:
    """ Opens the file in gvim
    :relative_path: a list of relative paths
    :gvim_flags: flags to pass to gvim directly
    :n: spaces to rotate in ROTN
    :returns: None
    """
    file_paths = []
    for relative_path in relative_paths:
        if "\\" in relative_path or "/" in relative_path:
            lst = re.split(r" |\\|/", relative_path)
            file_name = lst.pop(-1)
            folder_name = "\\".join(lst) + "\\"
        else:
            folder_name = ""
            file_name = relative_path
        file_path = NOTE_FOLDER_PATH
        if folder_name != "":
            file_path += folder_name
            if os.path.exists(file_path):
                if not os.path.isdir(file_path):
                    raise(Exception("Folder name already in use by another file"))
            else:
                os.makedirs(file_path)
        file_path += file_name
        if n != 0 and os.path.exists(file_path):
            os.system("ROTN " + str(-n) + " -f " + file_path + " -o " + file_path)
        file_paths.append(file_path)
    p = subprocess.Popen(("gvim " + ' '.join(file_paths) + " " + gvim_flags).split())
    p.wait()
    if n != 0:
        os.system("ROTN " + str(n) + " -f " + file_path + " -o " + file_path)


def print_usage() -> None:
    """Print the correct usage of the command"""
    print(
            "Usage of command:\n" +
            "\tnote {relative path(s)} {gvim flag(optional)}\n" +
            "\t\tsee vim --help for info on flags\n" +
            "\t\tMore flags:\n" +
            "\t\t\t--rotn - next input is how many spaces rotated"
        )

def main():
    try:
        relative_path, gvim_flags, n = parse_argv()
    except Exception as e:
        print("Error: " + str(e))
        print_usage()
        return
    open_file(relative_path, gvim_flags, n)

if __name__ == "__main__":
    main()
