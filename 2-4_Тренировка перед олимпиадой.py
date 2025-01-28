import math
import time

# проверка совпадения всех элементов двух списков
def newlist(c):
    s = sum(c)
    k_odd = 0
    i = 0
    while i < len(c):
        if (c[i] % 2 != 0):
            k_odd += 1
        i += 1
    if (k_odd % 2 != 0):
        s = s - 1
    return s


t1=time.time()


f = open("2-4_Тренировка_перед_олимпиадой_data_input.txt", "r")
t=int(f.readline())  # t количество наборов входных данных
print(t)

for _ in range(t):
    n=int(f.readline())  #  размер массива n
    c = [int(i) for i in f.readline().split()]  #  считывается список элементов массива c
#c=[7,13,11,19,1]
#print(c)
    c1=[]
    s=[]
    i=0
    while i < len(c):
       c1.append(c[i])
       if(len(c1)==1):
           s.append(c1[0])
       else:
           s.append(newlist(c1))
       i+=1
    print(s)

t2=time.time()

MS_IN_SEC=1000
print('t= ', (t2-t1)*MS_IN_SEC, ' миллисекунд')
