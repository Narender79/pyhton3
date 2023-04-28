def max(x,y,z):
    if x>y and x>z:
        greater=x
    elif y>x and y>z:
        greater=y
    else:
        greater=z
    return greater

num1=int(input())
num2=int(input())
num3=int(input())
print(max(num1,num2,num3))