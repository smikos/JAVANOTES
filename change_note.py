import datetime
from check_file_exists import check_file_exists
from print_notes import print_notes
from check_ID import check_ID
from get_file_lines import get_file_lines


def change_note():
    file_path = check_file_exists()
    if file_path == None:
        print("Сожалеем, но списка с заметками не существует!\n")
    else:
        with open("notes_file.txt", "r", encoding="utf-8") as file:
            lines_qty = len(file.readlines())
            if lines_qty == 0:
                print("\nСожалеем, но в списке нет заметок.\n")
            else:
                print_notes()
                ID_to_change = input(
                    "Введите ID-номер заметки, которую вы хотите исправить и нажмите клавишу Enter: "
                )

                indx = check_ID(ID_to_change)
                if indx == None:
                    print("\nСожалеем, но заметки с таким ID нет в списке заметок.\n")
                else:
                    note_title = input(
                        "Введите новый заголовок заметки и нажмите клавишу Enter: "
                    )
                    note_text = input(
                        "Введите новый текст заметки и нажмите клавишу Enter: "
                    )
                    storage_date_time = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
                    note_ID = ID_to_change

                    fl = get_file_lines()
                    fl[
                        int(indx)
                    ] = f"{note_ID};{note_title};{note_text};{storage_date_time}\n"

                    with open(f"notes_file.txt", "w", encoding="utf-8") as file:
                        file.writelines(fl)

                    print("Заметка успешно изменена и сохранена!\n")
