﻿# Упражнение №11
# Назовем последовательность чисел последовательностью k-боначчи, если каждый элемент этой последовательности является
# суммой k предыдущих членов последовательности. В частности, последовательность 2-боначчи является последовательностью
# Фибоначчи. Более формально, i-й элемент последовательности ki равен 1, если 0≤i≤k-1, и равен сумме k предыдущих
# членов последовательности ki−1+ki−2+…+ki−k при i≥k.
#
# Даны два числа k и n (k≥2, n≥0). Вычислите n-й член последовательности k-боначчи kn.
# Решите задачу в пять строк.
# Ввод 	   Вывод
# 3 6   	17
# 100 0 	1

A=[]
# ввести через пробел числа k и n
k,n=map(int,input().split())
i=0
while i<k: # i-й элемент последовательности ki равен 1, если 0≤i≤k-1
    A.append(1)
    i+=1
A.append(sum(A[:])) # k-ый элемент
i+1
while i<n: # k+1....... элементы
    # A.append(sum(A[len(A)-k :])) # сумма по срезу
    # замечаем, что вычисление можно упростить по формуле
    # A[i]=2*A[i-1]-A[i-k]
    A.append(2*A[i]-A[i-k])
    i+=1

print(A[n])