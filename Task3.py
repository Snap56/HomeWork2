# Задайте список из n чисел последовательности (1+1/n)n и выведите на экран их сумму

# Пример:

# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} 
# Сумма 9.06


import math


n = int(input('Введите число n : '))

dict = {a: math.pow((1+1/n), n) for a in range(1,n+1)}
print (dict)
sum = round(sum(dict[x] for x in dict), 2)
print(sum)