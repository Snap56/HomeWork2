# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.



import math
import random


n = int(input('Введите число n : '))
list1 = []
for i in range(n):
    list1.append(random.randint(-n, n+1))
print(list1)
f = open('file.txt', 'r')
compos = 1
for i in f:
    compos *= list1[int(i)]
f.close()
print(compos)


