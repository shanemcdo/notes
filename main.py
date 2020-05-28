import os
import re
from sys import argv

NOTE_FOLDER_PATH = "C:\\Users\\Shane\\Dropbox\\Desktop\\Coding\\python\\notes\\note_folder\\"

def parse_argv() -> ("file_name", "folder_name"):
    """ converts argv into a more usable format
    :returns: a tuple of the file name and the folder name
    folder_name may be None
    """
    _ = argv.pop(0)
    length = len(argv)
    if length > 2:
        raise(Exception("Too many arguments"))
    elif length < 1:
        raise(Exception("Too few arguments"))
    elif length == 1:
        file_name = argv[0]
        folder_name = None
    elif length == 2:
        file_name, folder_name = argv
    if '.' not in file_name:
        file_name += ".txt"
    if "\\" in file_name or "/" in file_name:
        lst = re.split(r" |\\|/", file_name)
        file_name = lst.pop(-1)
        if folder_name != None:
            folder_name += "\\" + "\\".join(lst)
        else:
            folder_name = "\\".join(lst)
    return file_name, folder_name

def open_file(file_name, folder_name) -> None:
    """ Opens the file in gvim
    :file_name: The name of the file
    :folder_name: the name of the folder if none do not use folder
    :returns: None
    """
    file_path = NOTE_FOLDER_PATH
    if folder_name != None:
        file_path += folder_name + "\\"
        if os.path.exists(file_path):
            if not os.path.isdir(file_path):
                raise(Exception("Folder name already in use by another file"))
        else:
            os.makedirs(file_path)
    file_path += file_name
    os.system("gvim " + file_path)

def main():
    try:
        file_name, folder_name = parse_argv()
    except Exception as e:
        print("Error: " + str(e))
        return
    open_file(file_name, folder_name)

if __name__ == "__main__":
    main()
