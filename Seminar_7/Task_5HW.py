# ** 5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)

from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def some_joke (n: int, repeat: bool = False) -> list:
    """
    Функция возвращает случайные шутки, собранны из трёх списков слов

    :param n: количество шуток
    :param repeat: уникальные/неуникальные
    :return: списко случайных шуток

    """
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    list_of_j = []
    list_min = min(no, adv, adj) # сортирует списки по количеству элементов в них

    for i in range(len(list_min) % n if repeat else n):
        num = randrange(len(list_min))
        list_of_j.append(f"{no.pop(num)} {adv.pop(num)}" if repeat
                        else f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")

    return list_of_j

print(some_joke(10, True))
print(help(some_joke))