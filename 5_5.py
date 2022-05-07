"""Создать (программно) текстовый файл, записать в него программно набор чисел
(random c comprenhension), разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
from random import randint
with open(rf"5_5.txt", "w+", encoding="utf-8") as f_num:
    nums = (randint(1, 1000) for i in range(2))
    for i in nums:
        f_num.write(f"{i} ")
    f_num.seek(0)
    s = 0
    x = f_num.read().split()
    for k in x:
        s += int(k)
        #print(f"{k} ", end='')
    print(f"\nSumma = {s}")

