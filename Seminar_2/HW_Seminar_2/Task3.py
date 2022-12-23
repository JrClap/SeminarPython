# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

num_list = []
N = int(input('Введите длину списка - '))
for i in range(1, N + 1):
    num_list.append((1 + 1 / i) ** i)
print('Список значений:', num_list)

dlina_list = len(num_list)
summa = 0
for i in range(dlina_list):
    summa = summa + num_list[i]
print('Сумма значений в списке равна:', round(summa, 3))
