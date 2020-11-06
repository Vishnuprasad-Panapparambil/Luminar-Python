n=input("enter the name of student")
s1=int(input("enter the marks of science"))
m1=int(input("enter the marks of maths"))
e1=int(input("enter the marks of english"))
total=s1+m1+e1
print(m1)
print(total)
if(total>145):
    print("a+")
elif(total>=140):
    print("a")
elif(total>=135):
    print("b+")
elif (total >= 130):
    print("b")
else:
    print("failed")


