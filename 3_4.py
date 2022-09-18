# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input("Enter your number: "))
bnumber = ""
while number > 0:
    bnumber = str(number % 2) + bnumber
    number = number // 2
print(bnumber)
