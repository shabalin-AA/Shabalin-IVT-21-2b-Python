from pyDatalog import pyDatalog
from random import randrange
import math
from gmpy2 import mpz

"""
посчитать сумму ряда 0-999999
среднее этого ряда
медиану случайных 1000000 чисел
их произведение
"""

pyDatalog.create_terms('sum_of_range, N, A, Sum_of_range, medium, arr, Medium, median, Median, prod, Prod, fact')


sum_of_range[N] = (0 + N) / 2
print(sum_of_range[999]==Sum_of_range)
print()


medium[N] = sum_of_range[N] / N
print(medium[999]==Medium)
print()


n = 1000000
arr = []
for i in range(n):
    arr.append(randrange(1, 10))
arr.sort()

median = arr[n//2] if n%2==0 else (arr[(n+1)//2] + arr[n//2]) / 2
print(median==Median)
print()

fact[N] = N * fact[N-1]
fact[1] = 1

prod = fact[max(arr) - min(arr)] ** (n / (max(arr) - min(arr)))
print(prod==Prod)
print()

print((math.prod(arr)))
