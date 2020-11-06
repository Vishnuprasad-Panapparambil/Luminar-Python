l=int(input("enter lwr"))
u=int(input("enter upr"))
sum=0
while(l<=u):
    a=0
    for i in range(2,l):
        if(l%i==0):
            a=1
        else:
            pass
    if (a > 0):
        pass
    else:
        sum=sum+l
    l=l+1
print("sum of prime=",sum)