# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

N = int(input('Введите количество элементов списка - '))

def find_multiples(number):
    lst = [i for i in range(20, N + 1) if i % 20 == 0 or i % 21 == 0]
    print(lst)

find_multiples(N)