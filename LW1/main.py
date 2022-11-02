from random import randrange
from numpy import median
import math as math
from gmpy2 import mpz


s = ((0 + 999999) * (999999 + 1)) / 2
print("сумма ряда 0-999999: ", s)


avg = s / (999999 + 1)
print("среднее ряда 0-999999: ", avg)


arr = []
for i in range(1000000):
    arr.append(randrange(1, 10))
print("медиана среди 1000000 случайных чисел от 1 до 10: ", median(arr))


print("произведение ряда случайных чисел: ", mpz(math.prod(arr)))
