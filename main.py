from sys import argv

note_folder_path = "C:\\Users\\Shane\\Dropbox\\Desktop\\Coding\\python\\notes\\note_folder\\"

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
    return file_name, folder_name

def main():
    try:
        file_name, folder_name = parse_argv()
    except Exception as e:
        print("Error: " + str(e))
        return

if __name__ == "__main__":
    main()
