def readed ():
    with open("Seminar_8\System\work_schedule.txt", "r", encoding='utf-8') as f:
        print(f.read())

def writed ():
    with open("Seminar_8\System\work_schedule.txt", "r", encoding='utf-8') as expt:
        old_data = expt.read()
        print(old_data)
    x = int(input('Введите день, который хотите изменить - '))
    if x == 1:
        new_data = old_data.replace("1.Понедельник: 10:00 - 21:00", input("Введите в таком примере: Номер дня.День: чч:мм - чч:мм\n"))
        with open ("Seminar_8\System\work_schedule.txt", "w", encoding='utf-8') as f:
            f.write(new_data)
    elif x == 2:
        new_data = old_data.replace("2.Вторник: 09:00 - 21:00", input("Введите в таком примере: Номер дня.День: чч:мм - чч:мм\n"))
        with open ("Seminar_8\System\work_schedule.txt", "w", encoding='utf-8') as f:
            f.write(new_data)
    elif x == 3:
        new_data = old_data.replace("3.Среда: 09:00 - 21:00", input("Введите в таком примере: Номер дня.День: чч:мм - чч:мм\n"))
        with open ("Seminar_8\System\work_schedule.txt", "w", encoding='utf-8') as f:
            f.write(new_data)
    elif x == 4:
        new_data = old_data.replace("4.Четверг: 09:00 - 21:00", input("Введите в таком примере: Номер дня.День: чч:мм - чч:мм\n"))
        with open ("Seminar_8\System\work_schedule.txt", "w", encoding='utf-8') as f:
            f.write(new_data)
    elif x == 5:
        new_data = old_data.replace("5.Пятница: 09:00 - 23:00", input("Введите в таком примере: Номер дня.День: чч:мм - чч:мм\n"))
        with open ("Seminar_8\System\work_schedule.txt", "w", encoding='utf-8') as f:
            f.write(new_data)
    elif x == 6:
        new_data = old_data.replace("6.Суббота: 10:00 - 23:00", input("Введите в таком примере: Номер дня.День: чч:мм - чч:мм\n"))
        with open ("Seminar_8\System\work_schedule.txt", "w", encoding='utf-8') as f:
            f.write(new_data)
    elif x == 7:
        new_data = old_data.replace("7.Воскресенье: 10:00 - 22:00", input("Введите в таком примере: Номер дня.День: чч:мм - чч:мм\n"))
        with open ("Seminar_8\System\work_schedule.txt", "w", encoding='utf-8') as f:
            f.write(new_data)
    else:
        print("Попробуйте ещё раз🧐")

def deleted ():
    with open("Seminar_8\System\work_schedule.txt", "w", encoding='utf-8') as f:
        f.write("")