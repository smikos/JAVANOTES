from print_notes import print_notes
from get_file_lines import get_file_lines
from check_ID import check_ID
from check_file_exists import check_file_exists


def delete_note():
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
                ID_to_delete = input(
                    "Введите ID-номер заметки, которую вы хотите удалить и нажмите клавишу Enter: "
                )
                indx = check_ID(ID_to_delete)
                if indx == None:
                    print("\nСожалеем, но заметки с таким ID нет в списке заметок.\n")
                else:
                    fl = get_file_lines()
                    del fl[int(indx)]
                    fl = [
                        f'{fl[i].split(";")[0]};'
                        f'{fl[i].split(";")[1]};'
                        f'{fl[i].split(";")[2]};'
                        f'{fl[i].split(";")[3]}'
                        for i in range(len(fl))
                    ]
                    with open(f"notes_file.txt", "w", encoding="utf-8") as file:
                        file.writelines(fl)

                    print("\nЗаметка успешно удалена!\n")
