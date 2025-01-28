import copy
import math

lst1 = [1,2,3]
lst2=lst1 #lst2 = [1,2,3]
print (lst1==lst2, lst1 is lst2)
lst1[1]=4
print (lst1==lst2, lst1 is lst2)
lst2=lst1
print (lst1==lst2, lst1 is lst2)
lst2[1]=7
print (lst1==lst2, lst1 is lst2)


grade = 5
o="O"
res="ITM"+o
if res == "ITMO":
    print("Правильный ответ!")
else:
    print("Неправильный ответ")
if res is "ITMO":
    print("You are correct!")
else:
    print("Wrong answer")

lst1 = [1, [9, 6, 5], 6]
# lst2=list(lst1)
lst2 = lst1[:]
# lst2=[1, [9, 6, 5], 6]
print(id(lst1), id(lst2))
lst1[0] = 5
lst1[1][2] = -7
print(lst1)
print(lst2)

lst1=[1, [9, 6, 5], 6]
lst2=copy.deepcopy(lst1)
#lst2=list(lst1)
#lst2=lst1[:]
#lst2=[1, [9, 6, 5], 6]
print(id(lst1),id(lst2))
lst1[0]=5
lst1[1][2]=-7
print(lst1)
print(lst2)

a=5
#del a
#del print
#(a)

'''
def print(a):
    pass
'''

res = print('Hello world!')


#print=10
#print+=10
#print(a)

import math
math.pi=4.0
print(f"pi = {math.pi:.6f}")

#from math import *
#from lesson02_my_lib import *

import math as m
import lesson02_my_lib as ml

print(m.pi, ml.pi)


#pi=4.0
#print(f"pi = {pi:.6f}")



def my_func():
   # import math
   # print(f"pi={math.pi:.6f}")
   import lesson02_my_lib
   print(f"pi={lesson02_my_lib.pi:.6f}")


my_func()