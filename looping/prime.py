n=int(input("enter nmbr"))
a=0
for i in range(2,n):
    if(n%i==0):
        a=1
    else:
        pass
if(a>0):
    print("not prime")
else:
    print("prime")