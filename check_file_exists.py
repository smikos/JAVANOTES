import os


def check_file_exists():
    file_path = "notes_file.txt"
    if os.path.exists("notes_file.txt"):
        return file_path
    else:
        file_path = None
