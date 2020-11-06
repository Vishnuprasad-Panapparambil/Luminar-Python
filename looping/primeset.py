l=int(input("enter lwr"))
u=int(input("enter upr"))

while(l<=u):
    a=0
    for i in range(2,l):
        if(l%i==0):
         a=1
        else:
            pass
    if(a>0):
        print(l,"not prime")
    else:
        print(l,"prime")
    l=l+1