# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти = '))

if number > 4 or number < 1:
    print('Такой номер четверти отсутствует, введи значение от 1 до 4')
if number == 1:
    print('Диапозон возможных координат x > 0, y > 0')
if number == 2:
    print('Диапозон возможных координат x < 0, y > 0')
if number == 3:
    print('Диапозон возможных координат x < 0, y < 0')
if number == 4:
    print('Диапозон возможных координат x > 0, y < 0')