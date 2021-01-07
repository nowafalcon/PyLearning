# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
# средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

profit = {}
pr = {}
mlist = []
profav = 0
prof = 0
i = 0

with open('./file_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, llc, plus, minus = line.split()
        profit[name] = int(plus) - int(minus)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        profav = prof / i
        # print(f'Средняя прибыль {profav}')
    else:
        print(f'Средняя прибыль меньше нуля')
    pr = {'Сред прибыль': round(profav)}
    # profit.update(pr)
    mlist = [profit, pr]
    print(f'Прибыль по компаниям составит - {mlist}')
    # print(mlist)


with open('./file_7.json', 'w', encoding='utf-8') as write_js:
    json.dump(mlist, write_js)
    js_str = json.dumps(mlist)

file.close()
write_js.close()