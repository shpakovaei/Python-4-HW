# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число: '))
list = []

for i in range(2,n + 1):
    if n % i == 0:
        count = 1
        for k in range(2,(i//2 + 1)):
            if(i % k == 0):
                count = 0
                break
        if(count == 1):
            print(i)
