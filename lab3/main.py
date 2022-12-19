from pyDatalog import pyDatalog
from random import randrange
import math

"""
посчитать сумму ряда 0-999999
среднее этого ряда
медиану случайных 1000000 чисел
их произведение
"""

pyDatalog.create_terms('sum_of_range, N, Sum_of_range, medium, arr, Medium, median, Median, prod, Prod, fact')


n = 1000000

sum_of_range[N] = (0 + N) * n/2
print(sum_of_range[n]==Sum_of_range)
print()


medium[N] = sum_of_range[N] / N
print(medium[n]==Medium)
print()


arr = []
for i in range(n):
    arr.append(randrange(1, 10))
arr.sort()


median = arr[n//2] if n%2==1 else (arr[n//2 - 1] + arr[n//2]) / 2
print(median==Median)
print()


fact[N] = N * fact[N-1]
fact[min(arr)] = min(arr)

prod = fact[max(arr)-min(arr)] ** (n / (max(arr)-min(arr)))
print(prod==Prod)
print()
