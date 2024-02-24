from data_create import name_data, surname_data, phone_data, adress_data

def remove_empty_lines(file_name):
    with open(file_name, "r") as file:
        str = file.readlines()

    modified_str = []
    for i in str:
        if i.strip(): 
            modified_str.append(i)

    with open(file_name, "w") as file:
        for i in modified_str:
            file.write(i)

def change_data():
    remove_empty_lines("data_first_variant.csv")
    remove_empty_lines("data_second_variant.csv")
    var = int(input("Выберите вариант:\n1 - Изменить данные в первом файле\n2 - Изменить данные во втором файле\n"))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Выберите вариант:\n1 - Изменить данные в первом файле\n2 - Изменить данные во втором файле\n"))

    if var == 1:
        with open("data_first_variant.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()        

        print("Вы можете изменить следующие данные:")
        print(*data)

        str_number = int(input("Введите номер строки, которую хотите изменить: "))
        while str_number < 1 or str_number > len(data):
            print("Неправильный номер строки")
            str_number = int(input("Введите номер строки, которую хотите изменить: "))

        new_data = input("Введите новые данные: ") 

        data[str_number-1] = new_data + " \n"

        with open("data_first_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Изменения сохранены")

    elif var == 2:
        with open("data_second_variant.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()            

        print("Вы можете изменить следующие данные:")
        print(*data)

        str_number = int(input("Введите номер строки, которую хотите изменить: "))
        while str_number < 1 or str_number > len(data):
            print("Неправильный номер строки")
            str_number = int(input("Введите номер строки, которую хотите изменить: "))

        new_data = name_data() + "; " + surname_data() + "; " + phone_data() + "; " + address_data()

        data[str_number-1] = new_data + "\n"

        with open("data_second_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Изменения сохранены")


def del_data():
    var = int(input("Выберите вариант:\n1 - Удалить данные из первого файла\n2 - Удалить данные из второго файла\n"))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Выберите вариант:\n1 - Удалить данные из первого файла\n2 - Удалить данные из второго файла\n"))

    if var == 1:
        with open("data_first_variant.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()

        print("Вы можете удалить следующие данные:")
        print(*data)

        str_number = int(input("Введите номер строки, которую хотите удалить: "))
        while str_number < 1 or str_number > len(data):
            print("Неправильный номер строки")
            str_number = int(input("Введите номер строки, которую хотите удалить: "))

        del data[str_number-1]

        with open("data_first_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Данные удалены")

    elif var == 2:
        with open("data_second_variant.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()

        print("Вы можете удалить следующие данные:")
        print(*data)

        str_number = int(input("Введите номер строки, которую хотите удалить: "))
        while str_number < 1 or str_number > len(data):
            print("Неправильный номер строки")
            str_number = int(input("Введите номер строки, которую хотите удалить: "))

        del data[str_number-1]

        with open("data_second_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Данные удалены")