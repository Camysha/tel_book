from data_create import name_data, surname_data, phone_data, adress_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"\n В каком формате записать данные\n\n" 
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{adress}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{adress}\n" 
    f"Выберете вариант: "))

    while var !=1 and var !=2:
        print ("неправильный ввод")
        var = int(input('введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{adress}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name};{surname};{phone};{adress}\n\n")

def print_data():
    print ('Вывожу данные из 1ого файла: \n')
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1])) #с помощью срезов добавляют условие что записывается каждая запись
                j = i
        print(''.join(data_first_list))

    print ('Вывожу данные из 2ого файла: \n')
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as f:
        data_second = f.readlines()
        print(*data_second) #распаковка списка


print_data()