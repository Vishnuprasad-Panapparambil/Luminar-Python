a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if((a>b>c)or(c>b>a)):
    print("b is the second largest")
elif((b>c>a)or(a>c>b)):
    print("c is the second largest")
elif((c>a>b)or(b>a>c)):
    print("a is the second largest")
else:
    pass
print("vishnu")