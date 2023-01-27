# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.

from random import sample

def more_then(num):
    my_list = sample(range(num * 3), num)
    print(my_list)
    return[my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]

print(more_then(int(input('Введите число '))))

# ----------------------- Вариант №2 -----------------------

from random import randint

def more_then(num):
    origin_list = [randint(0, 100) for _ in range(num)]
    print(origin_list)
    return[num for i, num in enumerate(origin_list[1:]) if num > origin_list[i]]

print(more_then(int(input('Введите число '))))