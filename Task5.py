

import random


N = int(input('Введите число N : '))
list = []
for i in range(N):
    list.append(random.randint(10, 22))
print(list)
list.reverse()
print(list)