f = open("1-1_Экзамен_Сакурако_data_input.txt", "r")
n=int(f.readline())
print(n)

i=0
while i <n:
    c = f.readline().split()
    # print(c[0], c[1])
    a = int(c[0])
    b = int(c[1])
    if(a==0):
        if(b%2==0):
            print(a,'  ',b, '  ', 'yes')
        else:
            print(a,'  ',b, '  ', 'no')
    else:
        if(a%2==0):
            print(a,'  ',b, '  ', 'yes')
        else:
            print(a,'  ',b, '  ', 'no')
    i+=1

f.close()