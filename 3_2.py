# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint
mylist = []
for i in range(8):
    mylist.append(randint(0, 20))
print(mylist)
mylist1 = []
p = 1
for i in range((len(mylist)+1)//2):
    p = mylist[i] * mylist[-i-1]
    mylist1.append(p)
print(mylist1)