a=int(input("enter the upper"))
b=int(input("enter the lower"))
evensum=0
oddsum=0
while(b<a):
    if(b%2==0):
        print("b=",b)
        evensum=evensum+b
    else:
        print("b=", b)
        oddsum=oddsum+b
    b=b+1
print(evensum)
print(oddsum)