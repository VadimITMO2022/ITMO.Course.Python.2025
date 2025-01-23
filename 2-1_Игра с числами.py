f = open("2-1_Игра_с_числами_data_input.txt", "r")
t=int(f.readline())
print(t)

i=0
while i <t:
    n = int(f.readline())
    if((n-1)%3==0 or (n+1)%3==0):
        print(n,'  ', 'First')
    else:
        print(n, '  ', 'Second')
    i+=1
f.close()