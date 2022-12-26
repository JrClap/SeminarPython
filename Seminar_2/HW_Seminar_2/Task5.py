# 5. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

n = int(input('Введите значение N - '))
n_list = [*range(0, n)]
print('Список:', n_list)
import random
b = random.sample(n_list, n)
print('Список:', b)




