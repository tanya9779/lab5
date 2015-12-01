# Упражнение №6. Среднее арифметическое и среднеквадратическое отклонение
#   Для чисел из файла float_data.txt найдите:
#      1.  Среднее арифметическое всех чисел.
#      2.  Среднеквадратическое отклонение от среднего.
#      3.  Максимальное и минимальное число и их местоположение (первых при существовании равных им). Первое число считать идущим под номером 0.
in_file=open('float_data.txt')
f,M,D=0.0,0.0,0.0
max_n=0.0
min_n=100.0
i,n=0,0
x=[]
s=in_file.readline().rstrip()
while len(s)>0:
    f=float(s)
    x.append(f)
    M+=f
    if f>max_n:
        max_n=f
        max_pos=n
    if f<min_n:
        min_n=f
        min_pos=n
    n+=1
    s=in_file.readline().rstrip()
M=float(M/n)
print('SREDNEE',M)
for i in range(len(x)):
    D+=float((x[i]-M)**2)
print('OTKLONENIE',(D/(n-1))**0.5)
print('Max value ',"%.2f"%max_n,' in position ',max_pos)
print('Min value ',"%.2f"%min_n,' in position ',min_pos)
