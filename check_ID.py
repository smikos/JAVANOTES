def check_ID(id):
    with open(f"notes_file.txt", "r", encoding="utf-8") as file:
        flag = False
        for index, line in enumerate(file):
            if line.split(";")[0] == id:
                indx = index
                flag = True

        if flag == False:
            indx = None

    return indx
