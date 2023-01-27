# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# --------------------------------- 1 вариант ---------------------------------

def thesaurus(args):
    names_dict = {}
    for i in sorted(args):
        letter = i[0]
        
        if letter not in names_dict:
            names_dict[i] = [i]
        else:
            names_dict[i] += [i]
    
    return names_dict

print(thesaurus("Вика", "Анатолий", "Владимир", "Юля", "Катя", "Петя", "Артём"))

# --------------------------------- 2 вариант ---------------------------------

from itertools import groupby

def thesaurus(*args):
    if "" not in args:
        return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
    return "Error"

print(thesaurus("Вика", "Анатолий", "Владимир", "Юля", "Катя", "Петя", "Артём"))