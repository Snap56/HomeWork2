# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

sum = 0
input_num = input('Введите число: ')

for i in input_num:
    if i.isdigit():
        sum += int(i)

print(sum)

