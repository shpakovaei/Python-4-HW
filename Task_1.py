# Вычислить число Пи c заданной точностью d

import math

d = input('Введите число: ')
num_d = len (str (d)) - 2
print(round(math.pi, num_d))