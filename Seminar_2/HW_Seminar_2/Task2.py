# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N в виде списка.

num_list = []
N = int(input('Введите длину списка - '))
for i in range(1, N + 1):
    if i > 2:
        num_list.append(i * num_list[i - 2])
    else:
        num_list.append(i * 1) 
    
print('Список значений:', num_list)