# Задача 22: 

# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания 
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во
# элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint
number_1 = int(input('Введите кол-во элементов 1-го мнжества: '))
number_2 = int(input('Введите кол-во элементов 2-го мнжества: '))
mnog_1 = [randint(1, 10) for i in range(number_1)]
mnog_1 = set(mnog_1)
mnog_2 = [randint(1, 10) for i in range(number_2)]
mnog_2 = set(mnog_2)
print(f'Уникальные значения множества 1: {mnog_1}')
print(f'Уникальные значения множества 2: {mnog_2}')
mnog_3 = mnog_1.intersection(mnog_2)
mnog_3 = list(mnog_3)
for i in range(len(mnog_3) - 1):
    for j in range(len(mnog_3) - i - 1):
        if mnog_3[j] > mnog_3[j + 1]:
            temp = mnog_3[j]
            mnog_3[j] = mnog_3[j + 1]
            mnog_3[j + 1] = temp
print(f'Результат: {mnog_3}')