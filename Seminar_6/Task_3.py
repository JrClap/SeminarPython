#1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,* приоритет операций стандартный.
#* Добавьте скобки, приоритет операций меняется.
#exp = -2 + ( 4 / 2 - 7 + 8 * 7 ) * 3

actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

def cut (Ls):
    lst = []
    temp = 0
    
    while temp < len(Ls):
        if Ls[temp] == '(':
            end = Ls.index(')')
            lst.append(Ls[temp + 1 : end])
            temp = end
        else:
            lst.append(Ls[temp])
        temp += 1
    
    return lst

def calculat (new_lst):
    for i, val in enumerate(new_lst):
        if isinstance(val, list):
            new_lst[i] = calculat(val)

    index_lst =[i for i, val in enumerate(new_lst) if val in '*/']
    
    while index_lst:
        index_op = index_lst[0]
        a, b, c = new_lst[index_op - 1: index_op + 2]
        new_lst.insert(index_op - 1, actions[b](a, c))
        del new_lst [index_op: index_op + 3]
        index_lst =[i for i, val in enumerate(new_lst) if val in '*/']
    
    while len(new_lst) > 1:
        a, b, c = new_lst[:3]
        del new_lst[:3]
        new_lst.insert(0, actions[b](a, c))
    
    return new_lst[0]

user_input = input("Input - ").split()
print(calculat(cut(user_input)))