import time
import math

t1=time.time()
f = open("1-2_Лёша_и_разбиение_массива.txt", "r")

for _ in range(4):
    n=int(f.readline())  #  число элементов в массиве n
    c = [int(i) for i in f.readline().split()]  #  считывается список целочисленных элементов массива c

    print()
    print(n)

    start=[]
    finish=[]


    if n == 1:
        if c[0] != 0:
            start.append(1)
            finish.append(1)
            print('Yes')
        else:
            print('No')
    else:

        k = 0
        i = 0
        while i < n:
            if c[i] != 0:
                start.append(i+1)
                finish.append(i+1)
               # print('pp1',i, n, start, finish)
                k += 1
            else:
                finish.pop()
                finish.append(i + 1)
               # print('pp2',i, n, start, finish)
            i+=1

           # print('pp3', i, n, k, start, finish)




       # print('****',n,k, len(start), len(finish))
       # print(start,finish)
        print('Yes')
        i=0
        while i<k:
           print(start[i], finish[i])
           i+=1


    '''
    arb=[]
    arb[0][0]=c[0]
    sum(c[1:])
    print(n, '  ', sum(c))
    '''
t2=time.time()

MS_IN_SEC=1000
print('t= ', (t2-t1)*MS_IN_SEC, ' миллисекунд')

f.close()
