from pyDatalog import pyDatalog
from random import randrange

"""
посчитать сумму ряда 0-999999
среднее этого ряда
медиану случайных 1000000 чисел
их произведение
"""

pyDatalog.create_terms('sum_of_range, N, Sum_of_range, medium, arr, Medium, median, Median, prod, Prod')


sum_of_range[N] = N + sum_of_range[N-1]
sum_of_range[0] = 0
print(sum_of_range[999]==Sum_of_range)
print()


medium[N] = sum_of_range[N] / N
print(medium[999]==Medium)
print()


n = 1000
for i in range(n):
    arr[i] = randrange(1, 10)
arr.sort()

median[N] = arr[N/2] if n % 2 == 0 else (arr[(N+1)/2] + arr[N/2]) / 2
print(median[n]==Median)
print()


prod[N] = arr[N-1] * prod[N-1]
prod[1] = arr[0]
print(prod[n]==Prod)
print()
