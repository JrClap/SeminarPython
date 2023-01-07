# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample
a = int(input('Введите длину списка - '))
new_list = sample (range (1, a * 3), k=a)
print(new_list)

def summa_list (lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

summa_list(new_list)