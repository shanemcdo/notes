import os
from sys import argv
from main import NOTE_FOLDER_PATH

def parse_argv() -> None or "folder_name":
    _ = argv.pop(0)
    length = len(argv)
    if length == 0:
        return ""
    elif length > 1:
        raise(Exception("Too many arguments"))
    return argv[0]

def main():
    try:
        folder_name = parse_argv()
    except Exception as e:
        print("Error: " + str(e))
        return
    os.system('ls ' + NOTE_FOLDER_PATH + "\\" + folder_name)


if __name__ == "__main__":
    main()
