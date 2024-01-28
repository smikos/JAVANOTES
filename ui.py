from add_note import add_note
from print_notes import print_filtered_notes
from change_note import change_note
from delete_note import delete_note


def start_menu():
    print("Здравствуйте! Вы находитесь в приложении по управлению заметками!")
    command = None
    while command != 5:
        command = int(
            input(
                "\nВыберите, что вы хотите сделать:\n"
                "1. Создать заметку\n"
                "2. Вывести список заметок\n"
                "3. Редактировать заметку\n"
                "4. Удалить заметку\n"
                "5. Выйти из приложения\n"
                "Введите номер выбранной команды и нажмите клавишу Enter: "
            )
        )
        command = check_command_num(command)
        if command == 1:
            add_note()
        elif command == 2:
            print_filtered_notes()
        elif command == 3:
            change_note()
        elif command == 4:
            delete_note()
    print("Спасибо, что воспользовались нашими услугами\n" "Приходите к нам еще!")


def check_command_num(n):
    while n < 1 or n > 5:
        n = int(
            input(
                "Вы ввели неправильный номер команды! "
                "Попробуйте еще раз.\n"
                "Выберите, что вы хотите сделать:\n"
                "1. Создать заметку\n"
                "2. Вывести список заметок\n"
                "3. Редактировать заметку\n"
                "4. Удалить заметку\n"
                "5. Выйти из приложения\n"
                "Введите номер выбранной команды и нажмите клавишу Enter: "
            )
        )
    return n
