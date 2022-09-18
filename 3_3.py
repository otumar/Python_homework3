# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

mylist = [1.1, 1.2, 3.1, 5, 10.01]
print(mylist)
mymax = mylist[0] % 1
mymin = mylist[0] % 1
d = 0
for i in range(1, len(mylist)):
    if mylist[i] % 1 > mymax:
        mymax = round(mylist[i] % 1, 3)
    if 0 < mylist[i] % 1 < mymin:
        mymin = round(mylist[i] % 1, 3)
d = mymax - mymin
print(f"The max value of the fractional part is {mymax}")
print(f"The min value of the fractional part is {mymin}")
print(f"The difference between the max and min values is {d}")
