from Reading_and_writing import *
from Metods_carte import *
from Metods_staff import *


def menu():
    print("☕ Coffee house _Sweet mug_\n")
    while True:
        type_num = input("Working with:"
                         "\n1 - 👥 Сотрудники"
                         "\n2 - 🧾 Меню"
                         "\n3 - 📅 График работы"
                         "\n4 - 📠 Контакты"
                         "\n5 - Выход\n")
        match type_num:
            case "1": 
                menu_staff()
            case "2":
                menu_carte()
            case "3":
                menu_work_schedule()
            case "4":
                menu_contact()
            case "5":
                print("Goodbye! See you soon sun!")
                break
            case _:
                print("The menu item is not recognized. Try again!")

def menu_staff ():
    while True:
        type_num = input("\nPlease, select one of the items:"
                         "\n1 - Список сотрудников"
                         "\n2 - Внести изменения"
                         "\n3 - Добавить сотрудника"
                         "\n4 - Найти сотрудника"
                         "\n5 - Удалить"
                         "\n6 - Назад\n")
        match type_num:
            case "1": 
                staff_read()
            case "2":
                staff_replace()
            case "3":
                staff_add()
            case "4":
                staff_search()
            case "5": 
                staff_delete()
            case "6":
                print()
                break
            case _:
                print("The menu item is not recognized. Try again!")

def menu_carte ():
    while True:
        type_num = input("\nPlease, select one of the items:"
                         "\n1 - Кофе"
                         "\n2 - Какао"
                         "\n3 - Чай"
                         "\n4 - Горячий шоколад"
                         "\n5 - Напитки и соки"
                         "\n6 - Десерты"
                         "\n7 - Выпечка"
                         "\n8 - Бутерброды"
                         "\n9 - Назад\n")
        match type_num:
            case "1": 
                menu_carte_coffee()
            case "2":
                menu_carte_cocoa()
            case "3":
                print("В процессе 3")
            case "4": 
                print("В процессе 4")
            case "5":
                print("В процессе 5")
            case "6":
                print("В процессе 6")
            case "7":
                print("В процессе 7")
            case "8":
                print("В процессе 8")
            case "9":
                print()
                break
            case _:
                print("The menu item is not recognized. Try again!")

def menu_carte_coffee():
    while True:
        type_num = input("\nPlease, select one of the items:"
                         "\n1 - Показать позиции"
                         "\n2 - Изменить позицию"
                         "\n3 - Добавить позицию"
                         "\n4 - Назад\n")
        match type_num:
            case "1":
                coffee_read() 
            case "2":
                coffee_replace()
            case "3":
                coffee_add()
            case "4":
                print()
                break
            case _:
                print("The menu item is not recognized. Try again!")

def menu_carte_cocoa():
    while True:
        type_num = input("\nPlease, select one of the items:"
                         "\n1 - Показать позиции"
                         "\n2 - Изменить позицию"
                         "\n3 - Добавить позицию"
                         "\n4 - Назад\n")
        match type_num:
            case "1":
                cocoa_read() 
            case "2":
                cocoa_replace()
            case "3":
                cocoa_add()
            case "4":
                print()
                break
            case _:
                print("The menu item is not recognized. Try again!")

def menu_work_schedule():
    while True:
        type_num = input("\nPlease, select one of the items:"
                         "\n1 - Показать график"
                         "\n2 - Редактировать график"
                         "\n3 - Удалить график"
                         "\n4 - Назад\n")
        match type_num:
            case "1": 
                readed()
            case "2":
                writed()
            case "3":
                deleted()
            case "4":
                print()
                break
            case _:
                print("The menu item is not recognized. Try again!")

def menu_contact():
    while True:
        type_num = input("\nPlease, select one of the items:"
                         "\n1 - Адрес"
                         "\n2 - Почта"
                         "\n3 - Контактный номер"
                         "\n4 - Назад\n")
        match type_num:
            case "1": 
                print("\nул. Будённого 28, Гродно 230023, Беларусь")
            case "2":
                print("\nchococo.office@gmail.com")
            case "3":
                print("\n+375 33 327 22 24 - МТС;" 
                    "\n+375 29 671 73 23 - А1;")
            case "4":
                print()
                break
            case _:
                print("The menu item is not recognized. Try again!")
