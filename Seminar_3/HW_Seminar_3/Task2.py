# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import sample
a = int(input('Введите длину списка - '))
new_list = sample (range (1, a * 2), k=a)
print(new_list)

def mult_lst(lst):
    dlina = len(lst)//2
    if len(lst) % 2 != 0:
        new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(dlina)]
        new_lst.append(lst[len(lst)//2])
        print(new_lst)
    else:
        new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(dlina)]
        print(new_lst)

mult_lst(new_list)