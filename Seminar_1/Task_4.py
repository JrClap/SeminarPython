# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

number = float(input('Введите число - '))
newNumber = int(number * 10 % 10)
print(newNumber)  