"""Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
"""

import os
if os.path.exists(r"compito_5_1.txt"):
    os.remove("compito_5_1.txt")

x = open(rf"compito_5_1.txt", "x", encoding="utf-8")
str_temp = 0
while str_temp != '':
    str_temp = input(f"Input data: ")
    x.write(str_temp + "\n")

x.close()
