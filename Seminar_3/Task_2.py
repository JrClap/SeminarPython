# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь. 
# Напишите программу, которая определит индекс второго вхождения строки в списке либо сообщит, что её нет.

from random import sample
def spisok (count, word = 'abc'):
    list_a = []
    for i in range(count):
        temp = sample(word, k=3)
        list_a.append(''.join(temp))
    return list_a

def index_find (word, list_b):
    if word in list_b and list_b.count(word) > 1:
        index_1 = list_b.index(word)
        print(list_b.index(word, index_1 + 1))
    else:
        print(-1)

list_1 = spisok(int(input('Введите количество повторений - ')))

print (list_1)

index_find (input('Введите индекс - '), list_1)