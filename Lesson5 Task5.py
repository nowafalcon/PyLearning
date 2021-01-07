# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open('./file_5.txt', 'w', encoding='utf-8') as my_file:
            line = input('Введите числа через пробел \n')
            my_file.writelines(line)
            my_nums = line.split()
            print(sum(map(int, my_nums)))
            my_file.close()
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print("В файле не только числа")


summary()
