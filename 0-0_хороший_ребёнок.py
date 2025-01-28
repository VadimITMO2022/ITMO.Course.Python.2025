import math
import time

t1=time.time()
f = open("0-0_хороший_ребёнок_data_input.txt", "r")
t=int(f.readline())  # t число списков
print(t)

for _ in range(t):
    n=int(f.readline())  #  число элементов в одном списке n
    c = [int(i) for i in f.readline().split()]  #  считывается список целочисленных элементов c
    i_min = c.index(min(c))  # номер первого минимального элемента списка i_min
    c[i_min] = c[i_min] + 1  # первый минимальный элемент списка увеличен на 1
    mult=math.prod(c)  # произведение элементов списка c
    print(n, '  ', mult)
t2=time.time()

MS_IN_SEC=1000
print('t= ', (t2-t1)*MS_IN_SEC, ' миллисекунд')

f.close()
