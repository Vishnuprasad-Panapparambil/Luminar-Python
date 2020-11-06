list=[]
st={"hi",3,"rp"}
print(st)
len=int(input("enter the length of list"))
for i in range(0,len):
    num=int(input())
    list.append(num)
print(list)

lower=0
upper=len-1
f = list[lower]
while(lower<upper):

    if(list[lower]==f):
        pass
    elif((list[lower]!=f)&(f>0)):
        print("least +ve integer missing is",f)
        break
    lower=lower+1
    f=f+1
