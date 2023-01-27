# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.

from random import randint

lists = [randint(1, 20) for i in range(int(input('Введите количество элементов списка - ')))]
print(lists)
new_lists = [j for i, j in zip(lists, lists[1:]) if j > i]
print(new_lists)