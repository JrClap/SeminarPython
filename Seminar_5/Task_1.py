# 1. Создайте список из N натуральных чисел(0 до N), упорядоченных по возрастанию. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

from random import choice

def create_list ():
    number = int(input('Введите длину списка - '))
    list1 = [i for i in range(number + 1)]
    list1.remove(choice(list1))
    print(list1)
    return list1

def find_number(lst):
    for i in range(1, len(lst)):
        if lst[i] - 1 != lst[i-1]:
            return lst[i] - 1
    return -1

print(find_number(create_list()))