import os
import re
from sys import argv

NOTE_FOLDER_PATH = "C:\\Users\\Shane\\Dropbox\\Desktop\\Coding\\python\\notes\\note_folder\\"

def parse_argv() -> ("relative_path", "gvim_flags"):
    """ converts argv into a more usable format
    :returns: a tuple of the relative path name and the flags for gvim
    """
    _ = argv.pop(0)
    gvim_flags = []
    for arg in argv:
        if arg.startswith('-'):
            gvim_flags.append(arg)
    for flag in gvim_flags:
        argv.remove(flag)
    gvim_flags = " ".join(gvim_flags)
    length = len(argv)
    if length < 1:
        raise(Exception("Too few arguments"))
    relative_paths = []
    for arg in argv:
        if '.' not in arg:
            arg += ".txt"
        relative_paths.append(arg)
    return relative_paths, gvim_flags

def open_file(relative_paths: list, gvim_flags: str) -> None:
    """ Opens the file in gvim
    :relative_path: a list of relative paths
    :gvim_flags: flags to pass to gvim directly
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
        file_paths.append(file_path)
    os.system("gvim " + ' '.join(file_paths) + " " + gvim_flags)

def print_usage() -> None:
    """Print the correct usage of the command"""
    print(
            "Usage of command:\n" +
            "\tnote {relative path} {gvim flag(optional)}"
        )

def main():
    try:
        relative_path, gvim_flags = parse_argv()
    except Exception as e:
        print("Error: " + str(e))
        print_usage()
        return
    open_file(relative_path, gvim_flags)

if __name__ == "__main__":
    main()
