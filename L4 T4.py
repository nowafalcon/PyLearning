# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести
# в порядке их следования в исходном списке. Для выполнения задания обязательно
# использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]


from random import randint

# mylst1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
mylst = [randint(-10, 10) for X in range(20)]
# unil1 = [el for el in mylst1 if mylst1.count(el) == 1]
unil = [el for el in mylst if mylst.count(el) == 1]
print(f'Orig {mylst} \nUnique {unil}')
# print(f'{mylst1} \n {unil1}')


# print(a := [randint(0, 9) for _ in range(20)], '\n', [i for i in a if a.count(i) == 1], sep="")
# Вариант с ДЗ
