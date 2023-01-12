# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

from random import randrange
num_list = []
N = int(input('Введите длину списка - '))
for i in range(1, N + 1):
    num_list.append(randrange (1, N, 1))
print(f'Исходный список: {num_list}')

new_list = []
[new_list.append(i) for i in num_list if i not in new_list]
print(f'Список из неповторяющихся элементов: {new_list}')
