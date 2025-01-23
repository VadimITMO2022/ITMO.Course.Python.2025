import math


# проверка совпадения всех элементов двух списков
def returnMatches(a, b):
    if(len(list(set(a) & set(b))) == len(a)):
        return True
    else:
        return False


# список целых чисел длинны n, которые являются квадратами других чисел
def numbers_squired(n):
    i = 10 ** (n - 1)
    num = []
    k = 0
    while i < 10 ** n:
        if (int(math.sqrt(i)) * 1.0 == math.sqrt(i)):
            a = list(str(i))
            num.append(a)
           # print(k,i, int(math.sqrt(i)), int(math.sqrt(i)) ** 2, a)
            k += 1
        i += 1
    return num

# список чисел длинны n, мультимножества которых совпадают
def resulting_list(n, num):
   # print(n,num,len(num))
    b = False
    kum=[]
    kk=0
    i1=0
    while i1 < len(num):
 #       if (num[i1] == ['1','6','3','8','4']):
        '''if (i1 == 28):
            print(i1, num[i1])
            input()
            '''
        kk=0
        i2=0
        while i2 < len(num):
           # print(i1,i2)
            if(returnMatches(num[i1],num[i2])):
               # print(i1,i2,num[i1],num[i2],returnMatches(num[i1],num[i2]))
                kum.append(num[i2])
                kk+=1
               # print(kk)
                if (kk == n):
                    b = True
                    break
            i2 += 1
        if(b):
            break
        kum.clear()
        i1+=1
    return kum

f = open("2-5_Математическое_задание_data_input.txt", "r")
t=int(f.readline())
print(t)

i=0
while i < t:
    n=int(f.readline())
    num = numbers_squired(n)
    kum = resulting_list(n, num)
    print("\n{}".format(n))
    m = 0
    while m < n:
        res = int(''.join(kum[m]))
        print(int(math.sqrt(res)), ' ', res)
        m += 1
    i+=1

f.close()






