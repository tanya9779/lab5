﻿# Упражнение №16
# По данному числ N выведите первые N+1 строку треугольника Паскаля. Числа в строке разделяйте одним пробелом.
# Ввод 	Вывод
#4 	1
#  	1 1
#  	1 2 1
#  	1 3 3 1
#  	1 4 6 4 1

N=int(input())
A=[]
for i in range(N+1):
    for j in range(len(A)-1,0,-1): # в обратном порядке обходим список
        A[j]=A[j]+A[j-1]  # этот элемент становится суммой соседних
    A.append(1)
    print(" ".join(map(str,A))) # разделяем одним пробелом
