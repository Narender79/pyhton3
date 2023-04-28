sta=int(input())
end=int(input())
for i in range(sta,end+1):
    if i>1:
        for j in (2,end+1):
            if(i%j==0):
                break
        else:
            print(i)