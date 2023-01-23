#2 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.

with open("/Users/mrjrc/OneDrive/Desktop/SeminarPython/Seminar_5/HW_Seminar_5/encode.txt", 'r') as data:
    my_code = data.read()

print('Считанный текст для зашифровки:', my_code)

def code(txt): 
    coding = ""
    i = 0
    while i < len(txt):
        count = 1
        while i + 1 < len(txt) and txt[i] == txt[i + 1]:
            count += 1
            i += 1
        coding += str(count) + txt[i]
        i += 1
    return coding

with open("/Users/mrjrc/OneDrive/Desktop/SeminarPython/Seminar_5/HW_Seminar_5/decode.txt", 'w') as data1:
    data1.write(code(my_code))

with open("/Users/mrjrc/OneDrive/Desktop/SeminarPython/Seminar_5/HW_Seminar_5/decode.txt", 'r') as data1:
    my_decode = data1.read()

print('Зашифрованный текст:', my_decode)

def decode(txt):
    number = ''
    decoding = ''
    for i in range(len(txt)):
        if txt[i].isdigit():
            number += txt[i]
        else:
            decoding = decoding + txt[i] * int(number)
            number = ''
    return decoding

print('Расшифрованный текст:', decode(my_decode))

