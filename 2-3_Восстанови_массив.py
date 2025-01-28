import math
import time

t1=time.time()
f = open("2-3_Восстанови_массив_data_input.txt", "r")
t=int(f.readline())  # t число списков
print(t)

for _ in range(t):
    n=int(f.readline())  #  количество элементов в массиве n
    c = [int(i) for i in f.readline().split()]  #  считывается список целочисленных элементов c

    i_min = c.index(min(c))  # номер первого минимального элемента списка i_min
    c_min=c[i_min]

    if(i_min==0):
        newlist = [c_min]+c[:]
    elif(i_min==len(c)-1):
        newlist = c[:]+[c_min]
    else:
        newlist = c[:i_min] + [c_min] + c[i_min:]

    i_max = newlist.index(max(newlist))  # номер первого максимального элемента списка i_max
    if (i_max > 0 and i_max < len(newlist)-2 and newlist[i_max]==newlist[i_max+1]):
        newlist=newlist[:i_max+1]+[newlist[i_max+2]]+[newlist[i_max+2]]

    print(n, '  ', newlist)
t2=time.time()
MS_IN_SEC=1000
print('t= ', (t2-t1)*MS_IN_SEC, ' миллисекунд')

f.close()