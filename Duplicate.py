lis=[1,2,2,3,3,5,4,6,3,4,7,5]
temp=[]
for i in lis:
    if i not in temp:
        temp.append(i)
print(temp)
temp.sort()
print("after sort:",temp)
