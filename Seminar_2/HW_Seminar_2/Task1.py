a = input('Введите вещественное число - ')
a_list = list(a)
print(a_list)
a_list.remove('.')
print(a_list)
dlina_a_list = len(a_list)
sum = 0
for i in range(dlina_a_list):
    b = int(a_list[i])
    sum = sum + b
print(sum)