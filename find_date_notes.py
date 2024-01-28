import datetime


def find_date_notes():
    sum = 0
    flag = True
    
    while flag:
        try:
            string_date = input("\nВведите дату в формате dd/MM/yyyy: \n")
            user_date = datetime.datetime.strptime(string_date, "%d/%m/%Y").date()
            flag = False
        except ValueError:
            print("Формат даты неверный. Попробуйте еще раз!")

    with open(f"notes_file.txt", "r", encoding="utf-8") as file:
        print(f"\nСписок заметок c выбранной датой:\n")

        for line in file:
            line = line.rstrip("\n")
            line_date = datetime.datetime.strptime(
                line.split(";")[3], "%d.%m.%Y %H:%M:%S"
            ).date()
            if line_date == user_date:
                print(
                    f'ID: {line.split(";")[0]}; '
                    f'Заголовок: {line.split(";")[1]}; '
                    f'Заметка: {line.split(";")[2]}; '
                    f'Сохранена: {line.split(";")[3]}'
                )
                sum += 1
    if sum == 0:
        print("\nСожалеем, но заметки с такой датой нет в списке заметок.\n")
