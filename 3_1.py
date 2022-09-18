# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
mylist = []
for i in range (5):
    mylist.append(randint(0,20))
print(mylist)
s = 0
for i in range(len(mylist)):
    if i % 2 != 0:
        s += mylist[i]
print(s)
