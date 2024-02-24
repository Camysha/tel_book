from logger import input_data, print_data
from change_base import change_data, del_data

def interface():
    print("Добрый день! Вы попали на специальный бот справочник от гикбрейнс \n 1 - запись данных \n 2 - ввод данных \n3 - изменение данных \n4 - удаление данных")

    command = int(input('введите число '))

    while command not in [1, 2, 3, 4]:
        print ("неправильный ввод")
        command = int(input('введите число '))
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        change_data()
    elif command == 4:
        del_data()