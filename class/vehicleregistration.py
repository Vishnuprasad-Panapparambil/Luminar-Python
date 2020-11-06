import re
lst1=[]
lst2=[]
x='[kl][0-9]{2}[a-z]{2}[0-9]{4}'
f=open("C:/Users/new/PycharmProject/luminartechnolab/class/vehiclenumbers","r")
for line in f:
    nmbr=line.rstrip("\n")

    n=re.fullmatch(x,nmbr)
    if(n==None):

        print("invalid")



    else:
        print("vlid")


