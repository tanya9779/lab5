# Упражнение №10
# N кузнечиков стоят в ряд. Для каждого кузнечика задана числовая характеристика — длина его прыжка.
# Если длина прыжка кузнечика равна l, то он за один прыжок перепрыгивает через l других кузнечиков.
# Каждую секунду последний кузнечик прыгает к началу ряда, перепрыгивает через столько кузнечиков, чему
# равна длина его прыжка, и становится между двумя другими кузнечиками.
# В первой строке входных данных задана расстановка кузнечиков (длины их прыжков). Во второй строке входных
# данных задано число секунд t. Опеределите и выведите на экран расстановку кузнечиков через t секунд.
# Все длины прыжков — натуральные числа, меньшие, чем число кузнечиков в ряду.
# Решите задачу в четыре строки.
# Ввод 	Вывод
# 1 2 3 4 2 	4 1 2 2 3
# 2

# нужно ввести через пробел рассстановку кузнечиков
A = list(map(int, input().split()))
# ввести число секунд
n=int(input())
for i in range(n):
    A.insert(len(A)-A[-1]-1,A.pop())
print(' '.join(map(str, A)))
