# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# пределить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
# подсчет средней величины дохода сотрудников.

with open('./file_3.txt', 'r', encoding="utf-8") as my_file:
    sal = []
    lowest = []
    list = my_file.read().split('\n')
    for i in list:
        i = i.split()
        # print(i)
        if int(i[1]) < 20000:
            lowest.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20к: {lowest} \nCредний оклад {sum(map(int, sal)) / len(sal)}')