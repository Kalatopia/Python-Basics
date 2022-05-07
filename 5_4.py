"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

with open(rf"5_4.txt", "r", encoding="utf-8") as f_num, \
        open(rf"5_4_res.txt", "w",
             encoding="utf-8") as f_num_res:
    for i in f_num:
        len_num = len(i.split()[2]) + 1
        if int(i.split()[2]) == 1:
            print(i[0:len(i) - len_num] + ' один', file=f_num_res)
        elif int(i.split()[2]) == 2:
            print(i[0:len(i) - len_num] + ' два', file=f_num_res)
        elif int(i.split()[2]) == 3:
            print(i[0:len(i) - len_num] + ' три', file=f_num_res)
        elif int(i.split()[2]) == 4:
            print(i[0:len(i) - len_num] + ' четыре', file=f_num_res)
        elif int(i.split()[2]) == 5:
            print(i[0:len(i) - len_num] + ' пять', file=f_num_res)
        elif int(i.split()[2]) == 6:
            print(i[0:len(i) - len_num] + ' шесть', file=f_num_res)
        elif int(i.split()[2]) == 7:
            print(i[0:len(i) - len_num] + ' семь', file=f_num_res)
        elif int(i.split()[2]) == 8:
            print(i[0:len(i) - len_num] + ' восемь', file=f_num_res)
        elif int(i.split()[2]) == 9:
            print(i[0:len(i) - len_num] + ' девять', file=f_num_res)
        elif int(i.split()[2]) == 10:
            print(i[0:len(i) - len_num] + ' десять', file=f_num_res)
        elif int(i.split()[2]) == 11:
            print(i[0:len(i) - len_num] + ' одиннадцать', file=f_num_res)
        elif int(i.split()[2]) == 100:
            print(i[0:len(i) - len_num] + ' сто', file=f_num_res)
        elif int(i.split()[2]) == 1000:
            print(i[0:len(i) - len_num] + ' тысяча', file=f_num_res)
        else:
            print(i, end='', file=f_num_res)
