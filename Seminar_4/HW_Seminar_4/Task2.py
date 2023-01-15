# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите натуральное число - "))
def number_factors (n):
    i = 2
    lst = []
    old = n
    while i <= n:
        if n % i == 0:
            lst.append(i)
            n //= i
            i = 2
        else:
            i += 1
    print(f"Простые множители числа {old} приведены в списке: {lst}")

number_factors(num)