len=int(input("enter the length of the list"))
lst=[]
for i in range (0,len):
    a=int(input("enter the list values"))
    lst.append(a)
l=0
u=len-1
r=int(input("enter the sum"))
while(l<u):
    a=lst[l]+lst[u]
    if(a==r):
        print(lst[l],lst[u])
    else:
        pass
    l=l+1
    u=u-1