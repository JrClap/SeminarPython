# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

maxNumber = 0
for i in range(5):
    number = int(input('Введите число '))
    if number > maxNumber:
        maxNumber = number
print('Макисмальное число =', maxNumber)