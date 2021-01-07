# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка,

my_f = open('test.txt', 'w', encoding="utf-8")
line = input('Введите текст: ')
while line:
    my_f.writelines(line+'\n')
    line = input('Введите текст: ')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()