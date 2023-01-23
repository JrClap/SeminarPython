#1 Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

from random import sample

n = int(input('Введите значение N - '))
def create_str (number):
    a = str('абв')
    lst_words = []
    for i in range(number):
        b = sample(a, k=len(a))
        lst_words.append(''.join(b))
    return ' '.join(lst_words)

s = create_str(n)
print('Генерируемая строка:', s)
print('Строка без <абв>:', s.replace('абв', ''))

