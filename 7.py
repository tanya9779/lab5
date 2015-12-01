# Упражнение №7. Статистический анализ
# Для чисел из файла int_data.txt:
#   1. Найдите, сколько раз встречаеся каждое из чисел.
#   2. Выведите самое часто встречающееся число и самое редко встречающееся число.
#   3. Выведите, сколько всего различных чисел встречается в последовательности
n=0
max_n,min_n=0,100 # мах все равно больше 0, а min меньше 100
i=0
x=[] # это будет список длиной 1 млн
B=[]
for i in range(101): # счетчик встречаемости (число от 0 до 100)
    B.append(0)

in_file=open('int_data.txt')
s=in_file.readline().rstrip()
while len(s)>0:
    n=int(s)
    x.append(n)
    B[n]+=1
    s=in_file.readline().rstrip()
print('How often numbers contains in sequence:')
n=0
for i in range(101):
    print(str(i),'-->',str(B[i])) # число-->сколько раз встречается
    if B[i]>0:   # заодно посчитаем сколько разных чисел встречается в последовательности
        n+=1

print('Most often: ',str(B.index(max(B))),'    Less often: ',str(B.index(min(B))))
print('Total unique numbers in sequence: ',n)

