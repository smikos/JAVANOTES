import datetime


def add_note():
    note_title = input("Введите заголовок заметки и нажмите клавишу Enter: ")
    note_text = input("Введите текст заметки и нажмите клавишу Enter: ")
    storage_date_time = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    note_ID = get_next_note_ID()

    with open("notes_file.txt", "a", encoding="utf-8") as file:
        file.write(f"{note_ID};{note_title};{note_text};{storage_date_time}\n")

    print("Заметка успешно сохранена!\n")


def get_next_note_ID():
    file = open("last_ID_file.txt", "r", encoding="utf-8")
    last_Id = file.read()
    next_id = int(last_Id) + 1
    file = open("last_ID_file.txt", "w")
    file.write(str(next_id))
    file.close
    return next_id
