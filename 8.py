# Упражнение №8. Гистрограмма
# Требуется разбить все числа из файла float_data.txt на 20 интервалов, посчитать количество чисел,
# принадлежащих каждому интервалу, а затем вывести гистограмму распределения данных псевдослучайных
# чисел по этим интервалам.

import matplotlib.pyplot as plt

in_file=open('float_data.txt')
data=[]
for i in range(20):
    data.append(0)

s=in_file.readline().rstrip()
while len(s)>0:
    f=float(s)
    n=int(f)//5 # 0<n<19
    if n==20:
        n-=1 # так как 100.0//5=20 то будет ошибка выхода за границу списка
    data[n]+=1
    s=in_file.readline().rstrip()

plt.hist(data, bins=20)
plt.show()

