"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
 название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста."""

import json
import re

with open(rf"5_7.txt", "r", encoding="utf-8") as f_num, \
        open("dict_j.json", "w", encoding="utf-8") as f_json:
    profit = 0
    summa = 0
    n = 0
    lista_firm = list()
    lista_profit = list()
    f_dict1 = list()
    f_dict2 = dict()
    f_list = list()
    righe = [i for i in f_num]
    for k in righe:
        z = re.findall('[0-9]+', k)  # список цифр
        profit = int(z[0]) - int(z[1])  # прибыль
        lista_firm.append(k[0:k.find(' ')])
        lista_profit.append(profit)
        if profit > 0:
            summa += profit
            n += 1
    f_dict1 = {l: m for l, m in zip(lista_firm, lista_profit)}
    f_dict2 = dict.fromkeys(["average_profit"], summa/n)
    f_list.append(f_dict1)
    f_list.append(f_dict2)
    json.dump(f_list, f_json)








