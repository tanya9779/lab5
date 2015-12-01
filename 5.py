# Упражнение №5
#    При помощи модуля random и функции randint создайте файл int_data.txt с миллионом случайных 
#    чисел типа int в диапазоне от 0 до 100.
from random import *

outfile=open('int_data.txt','w')
for i in range(1000000):
    outfile.write(str(randint(0,100))+'\n')
outfile.close()

#    Также создайте файл float_data.txt с миллионом случайных чисел типа float в диапазоне 
#        от 0 до 100, имеющих два знака после десятичной точки.
outfile=open('float_data.txt','w')
for i in range(1000000):
    print("%.2f" % (random()*100),file=outfile)
outfile.close()
