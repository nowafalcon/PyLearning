# # Реализовать два небольших скрипта:
# # а) итератор, генерирующий целые числа, начиная с указанного,
# # б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый
# цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет
# прекращено.

from itertools import count, cycle

print('welcome1 Number for start, Enter to continue, q-to exit')
for i in count(int(input('Enter Number: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print('welcome2 Number for start, Enter to continue, q-to exit')
ini_lst = input('вводим список, числа вводить через пробел: ').split()
brbr = cycle(ini_lst)
quit = None
while quit != 'q':
    print(next(brbr), end='')
    quit = input()
