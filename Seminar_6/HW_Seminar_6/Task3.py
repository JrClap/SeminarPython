# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
#in: "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
#out: {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def alphabet(name):
    dictionary = {}
    for i in sorted(name_list):
        key = i[0].capitalize()
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(i)
    return dictionary

name_list = list(str(input('Введите имена сотрудников через пробел - ')).split())
print(alphabet(name_list))