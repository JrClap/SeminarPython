# 2. Создайте список, в который попадают числа, описывающие возрастающую последовательность. Порядок элементов менять нельзя.

from random import choices

def create_list():
    n = int(input('Введите длину списка - '))
    lst = choices(range(n * 2), k=n)
    return lst

#print(create_list())

def sort_number (lists):
    lst = []
    for i in range(len(lists)):
        temp = lists[i]
        cortez_lst = [temp]
        for j in range(i + 1, len(lists)):
            if lists[j] > temp:
                temp = lists[j]
                cortez_lst.append(temp)
        if len(cortez_lst) > 1:
            lst.append(cortez_lst)
    return lst

a = create_list()
print(a)
print(sort_number(a))


