#1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,* приоритет операций стандартный.
#* Добавьте скобки, приоритет операций меняется.

#exp = "-2 + ( 4 / 2 - 7 + 8 * 7 ) * 3".split()
actions = {
"^": lambda x, y: str(float(x) ** float(y)),
"*": lambda x, y: str(float(x) * float(y)),
"/": lambda x, y: str(float(x) / float(y)),
"+": lambda x, y: str(float(x) + float(y)),
"-": lambda x, y: str(float(x) - float(y))
}

def cut (lst):
    new_list = []
    temp = 0
    while temp < len(lst):
        if lst[temp] == '(':
            end = lst.index(')')
            new_list.append(lst[temp + 1 : end])
            temp = end
        else:
            new_list.append(lst[temp])
            temp += 1
    return new_list

def calculat (f):
    for i, k in enumerate(f):
        if isinstance(k, list):
            f[i] = calculat(k)
    index_lst =[i for i, k in enumerate(f) if k in '*/']
    while index_lst:
        index_op = index_lst[0]
        a, b, c = f[index_op - 1 : index_op + 2]
        f.insert(index_op - 1, actions[b](a, c))
        del f [index_op : index_op + 3]
        index_lst =[i for i, k in enumerate(f) if k in '*/']
    while len(f) > 1:
        a, b, c = f[:3]
        del f[:3]
        f.insert(0, actions[b](a, c))
    return f[0]

user_input = input("Input - ").split()
print(calculat(cut(user_input)))