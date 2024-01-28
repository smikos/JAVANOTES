from check_file_exists import check_file_exists
from find_date_notes import find_date_notes


def print_filtered_notes():
    file_path = check_file_exists()
    if file_path == None:
        print("\nСожалеем, но списка с заметками не существует!\n")
    else:
        with open("notes_file.txt", "r", encoding="utf-8") as file:
            lines_qty = len(file.readlines())
            if lines_qty == 0:
                print("\nСожалеем, но в списке нет заметок.\n")
            else:
                choice = True
                while choice:
                    choice = int(
                        input(
                            "\nКакой список вы хотите вывести:\n"
                            "1. Вывести все заметки\n"
                            "2. Вывести только заметки от какой-то одной даты\n"
                            "3. Вернуться в основное меню\n"
                            "Введите номер выбранной команды и нажмите клавишу Enter: "
                        )
                    )
                    choice = check_choice_num(choice)
                    if choice == 1:
                        print_notes_list()
                        choice = False
                    elif choice == 2:
                        find_date_notes()
                        choice = False
                    elif choice == 3:
                        choice = False


def print_notes():
    file_path = check_file_exists()
    if file_path == None:
        print("\nСожалеем, но списка с заметками не существует!\n")
    else:
        with open("notes_file.txt", "r", encoding="utf-8") as file:
            lines_qty = len(file.readlines())
            if lines_qty == 0:
                print("\nСожалеем, но в списке нет заметок.\n")
            else:
                print_notes_list()


def print_notes_list():
    with open("notes_file.txt", "r", encoding="utf-8") as file:
        print("\nСписок всех заметок:\n")
        for line in file:
            print(
                f'ID: {line.split(";")[0]}; '
                f'Заголовок: {line.split(";")[1]}; '
                f'Заметка: {line.split(";")[2]}; '
                f'Сохранена: {line.split(";")[3]}'
            )


def check_choice_num(x):
    while x < 1 or x > 3:
        x = int(
            input(
                "\nВы ввели неправильный номер команды! "
                "Попробуйте еще раз.\n"
                "\nВыберите, что вы хотите сделать:\n"
                "1. Вывести список заметок\n"
                "2. Вывести только заметки от какой-то одной даты\n"
                "3. Выйти из приложения\n"
                "Введите номер выбранной команды и нажмите клавишу Enter: "
            )
        )
    return x
