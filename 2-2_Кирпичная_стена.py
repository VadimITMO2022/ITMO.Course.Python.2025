import math
import time

t1=time.time()
f = open("2-2_Кирпичная_стена_data_input.txt", "r")
t=int(f.readline())  # t число списков
print(t)

for _ in range(t):
    c = [int(i) for i in f.readline().split()]  #  считывается список целочисленных элементов c
    stab=c[0] * (c[1]//2)  # устойчивость стены размера c[0] x c[1]
    print(c[0], c[1],'  ', stab)
t2=time.time()

MS_IN_SEC=1000
print('t= ', (t2-t1)*MS_IN_SEC, ' миллисекунд')

f.close()
