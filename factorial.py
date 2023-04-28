def fact(n):
    temp=1
    while(n>0):
        temp=temp*n
        n=n-1
    return temp


num=int(input())
if(num==0):
    print(1)
elif(num>0):
    print(fact(num))