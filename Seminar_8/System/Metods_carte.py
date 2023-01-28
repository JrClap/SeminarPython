
def coffee_read ():
    with open("Seminar_8\System\carte_coffee.txt", "r", encoding='utf-8') as f:
        print(f.read())

def coffee_replace ():
    with open("Seminar_8\System\carte_coffee.txt", "r", encoding='utf-8') as f1:
        old_data = f1.read()
        print(old_data)
    
    new_data = old_data.replace(input("Введите полное наименование позиции для замены:\n"), 
                                input("Введите изменения в текущую позицию:\n"))
    
    with open ("Seminar_8\System\carte_coffee.txt", "w", encoding='utf-8') as f2:
        f2.write(new_data)

def coffee_add ():
    with open("Seminar_8\System\carte_coffee.txt", "a+", encoding='utf-8') as f:
        f.write(input("Введите новую позицию по примеру: Название, объём мл - цена р.\n") + "\n")



def cocoa_read ():
    with open("Seminar_8\System\carte_cocoa.txt", "r", encoding='utf-8') as f:
        print(f.read())

def cocoa_replace ():
    with open("Seminar_8\System\carte_cocoa.txt", "r", encoding='utf-8') as f1:
        old_data = f1.read()
        print(old_data)
    
    new_data = old_data.replace(input("Введите полное наименование позиции для замены:\n"), 
                                input("Введите изменения в текущую позицию:\n"))
    
    with open ("Seminar_8\System\carte_cocoa.txt", "w", encoding='utf-8') as f2:
        f2.write(new_data)

def cocoa_add ():
    with open("Seminar_8\System\carte_cocoa.txt", "a+", encoding='utf-8') as f:
        f.write(input("Введите новую позицию по примеру: Название, объём мл - цена р.\n") + "\n")
