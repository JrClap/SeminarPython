# 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random
num_list = []
N = int(input('Enter a list length - '))
for i in range(1, N + 1):
    num_list.append(round(random.uniform(0, 10), 2))
print(num_list)

new_num_list = [round(i % 1, 2) for i in num_list]
print('Max number:', max(new_num_list))
print('Min number:',min(new_num_list))
print('Numbers difference:', round(max(new_num_list) - min(new_num_list), 2))