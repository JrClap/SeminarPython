
def staff_read ():
    with open("Seminar_8\System\staff.txt", "r", encoding='utf-8') as f:
        print(f.read())

def staff_replace ():
    with open("Seminar_8\System\staff.txt", "r", encoding='utf-8') as f1:
        old_data = f1.read()
        print(old_data)
    
    new_data = old_data.replace(input("Введите полное наименование позиции для замены:\n"), 
                                input("Введите изменения в текущую позицию:\n"))
    
    with open ("Seminar_8\System\staff.txt", "w", encoding='utf-8') as f2:
        f2.write(new_data)

def staff_add ():
    with open("Seminar_8\System\staff.txt", "a", encoding='utf-8') as f:
        f.write(input("Введите нового сотрудника по примеру: Фамилия Имя Отчество | Должность |\n") + "\n")

def staff_search ():
    x = str(input("Поиск: "))
    with open('Seminar_8\System\staff.txt', encoding='utf-8') as f:
        for line in f:
            if x in line:
                print(line, end='')

def staff_delete ():
    with open("Seminar_8\System\staff.txt", "w", encoding='utf-8') as f:
        f.write("")
