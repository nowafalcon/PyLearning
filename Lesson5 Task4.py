# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом
# английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
# текстовый файл.

rte = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Фифире'}
nfile = []
with open('./file_4.txt', 'r', encoding='utf-8') as ofile:
    for i in ofile:
        i = i.split(' ', 1)
        nfile.append(rte[i[0]] + ' ' + i[1])
    print(nfile)
ofile.close()
with open('./file_4_new.txt', 'w', encoding='utf-8') as newfile:
    newfile.writelines(nfile)
newfile.close()
