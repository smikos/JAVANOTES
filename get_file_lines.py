def get_file_lines():
    with open("notes_file.txt", "r", encoding="utf-8") as file:
        file_lines = file.readlines()
    return file_lines
