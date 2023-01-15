# 1. Вычислить число c заданной точностью d

from decimal import Decimal
a = float(input('Введите вещественное число - '))
b = float(input('Введите округление, в формате 0,0001 - '))
number_b = Decimal(str(b)).as_tuple().exponent*(-1)
print(round(a, number_b))
